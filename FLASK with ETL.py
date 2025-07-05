from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
import csv
import os
from dateutil import parser # Smart date parser
import config

# --- 1. Flask App Configuration ---

app = Flask(__name__)
app.config.from_object(config)
mysql = MySQL(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# --- 2. ETL Functions ---

# 2.1 Extract data from uploaded CSV file
def extract_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        return list(reader)

# 2.2 Transform data (clean/format dates)
def transform_data(data):
    transformed = []
    for row in data:
        try:
            # Convert various date formats to YYYY-MM-DD (for MySQL)
            parsed_date = parser.parse(row[4])
            row[4] = parsed_date.strftime("%Y-%m-%d")
            transformed.append(row)
        except Exception as e:
            print(f"Skipped row due to invalid date: {row[4]} --> {e}")
            continue  # Skip row if date can't be parsed
    return transformed

# 2.3 Load data into MySQL
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

# --- 3. Flask Routes ---

@app.route('/')
def form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or request.files['file'].filename == '':
        flash('No file selected.')
        return redirect('/')

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Run ETL process
    raw_data = extract_data(filepath)
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)

    flash('File uploaded and data inserted successfully!')
    return redirect('/')

# --- 4. Run Flask App ---

if __name__ == '__main__':
    app.run(debug=True)
