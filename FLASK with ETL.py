from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
import os
import csv
import pandas as pd
from dateutil import parser
from werkzeug.utils import secure_filename
import config

# 1. Flask App Configuration

app = Flask(__name__)
app.config.from_object(config)
mysql = MySQL(app)

# Ensure Upload Folder Exists
def ensure_upload_folder(app):
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 2. ETL Functions


def extract_data(filepath):
    _, ext = os.path.splitext(filepath.lower())

    if ext == '.csv':
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header if present
            return list(reader)
    elif ext in ('.xls', '.xlsx'):
        df = pd.read_excel(filepath)
        return df.values.tolist()
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def transform_data(data):
    transformed = []
    for row in data:
        try:
            # Safe check before trying to parse date
            if len(row) > 4 and row[4] and isinstance(row[4], str):
                parsed_date = parser.parse(row[4])
                row[4] = parsed_date.strftime("%Y-%m-%d")
                transformed.append(row)
            else:
                print(f"Skipped row due to missing or invalid date format: {row}")
        except Exception as e:
            print(f"Skipped row due to parsing error: {row[4]} --> {e}")
            continue
    return transformed


def load_data(rows):
    cur = mysql.connection.cursor()
    query = """
        INSERT INTO Employee_Details (
            Employee_ID, Employee_Name, Department, Gender, Training_Date,
            Training_Category, Course, Training_Mode, No_of_Training_session, Training_Hours
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
            Employee_Name=VALUES(Employee_Name),
            Department=VALUES(Department),
            Gender=VALUES(Gender),
            Training_Date=VALUES(Training_Date),
            Training_Category=VALUES(Training_Category),
            Course=VALUES(Course),
            Training_Mode=VALUES(Training_Mode),
            No_of_Training_session=VALUES(No_of_Training_session),
            Training_Hours=VALUES(Training_Hours);
    """
    for row in rows:
        cur.execute(query, row)
    mysql.connection.commit()
    cur.close()

# 3. Flask Routes

@app.route('/')
def form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or request.files['file'].filename == '':
        flash('No file selected.')
        return redirect('/')

    file = request.files['file']
    filename = secure_filename(file.filename)
    ensure_upload_folder(app)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # Run ETL process
        raw_data = extract_data(filepath)
        cleaned_data = transform_data(raw_data)
        load_data(cleaned_data)
        flash('File uploaded and data inserted successfully!')
    except Exception as e:
        flash(f'Error processing file: {e}')

    return redirect('/')

# 4. Run Flask App

if __name__ == '__main__':
    app.run(debug=True)
