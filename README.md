# Training Data Management System using Flask & ETL

This project is built to manage employee training data. It includes a web interface to upload training CSV files, processes the data using ETL logic in Python, stores it in MySQL, and sends automated email reports. The system is also ready for automation using Apache Airflow.

## 🚀 Features

- Upload training data via a Flask web page
- Clean and transform CSV using Python ETL
- Store data in MySQL database
- Automatically send daily email summary of training data
  

## 🛠️ Tech Stack

| Component       | Technology Used     |
|-----------------|---------------------|
| Web Interface   | Flask (Python)      |
| ETL Processing  | Python (Pandas, CSV)|
| Database        | MySQL               |
| Email Reports   | smtplib / email     |
| Version Control | Git & GitHub        |

## 📂 Project Structure

> Config.py (To retrive all the secured file using username and password)
> FLASK with ETL.PY (For FLASK with ETL Code)
> Templates > Uploads.html (For FLASK upload webpage)
> Daily_training_email.py (To send a automatic email)
> Export.py (To export the file to local drive from the database)

