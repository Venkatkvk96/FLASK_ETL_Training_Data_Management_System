# 1. Import Block:

from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
import csv
import os

# 2. App Configuration Block:

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY'] = 'your_secret_key'

mysql = MySQL(app)

# 3. Route Block - Upload form page:

@app.route('/')
def form():
    return render_template('upload.html')

# 4. Route Block – Handle CSV Upload and Insert into MySQL:

@app.route('/upload', methods=['POST'])
def upload_file():

    # 4.1 Check if file is selected:

    if 'file' not in request.files or request.files['file'].filename == '':
        flash('No file selected.')
        return redirect('/')

    # 4.2 Save Uploaded file:

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # 4.3 Read CSV and insert/update data in database:

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        cur = mysql.connection.cursor()
        for row in reader:
            cur.execute("""
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
            """, row)
        mysql.connection.commit()
        cur.close()

        # 4.4 Show success message and redirect:

        flash('File uploaded and data inserted successfully!')
    return redirect('/')

# 5. Run the Flask App Block:

if __name__ == '__main__':
    app.run(debug=True)
