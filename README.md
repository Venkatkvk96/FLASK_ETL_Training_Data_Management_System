# Training Data Management System using Flask & ETL

This project is built to manage employee training data. It includes a web interface to upload training CSV files, processes the data using ETL logic in Python, stores it in MySQL, and sends automated email reports. The system is also ready for automation using Apache Airflow.

## 🚀 Features

- Upload training data via a Flask web page
- Clean and transform CSV using Python ETL
- Store data in MySQL database
- Send daily email summary of training data
- Ready for automation using Airflow (DAGs)

## 🛠️ Tech Stack

| Component       | Technology Used     |
|-----------------|---------------------|
| Web Interface   | Flask (Python)      |
| ETL Processing  | Python (Pandas, CSV)|
| Database        | MySQL               |
| Email Reports   | smtplib / email     |
| Version Control | Git & GitHub        |

## 📂 Project Structure

> Config.py (For MYSQL connection)
> FLASK with ETL.PY (For FLASK with ETL Code)
> Templates > Uploads.html (For FLASK upload webpage)
> Daily_training_email.py (To send a automatic email)


## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Venkatkvk96/Training-data.git
   cd Training-data

