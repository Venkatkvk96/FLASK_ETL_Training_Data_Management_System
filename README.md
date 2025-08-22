# Training Data Management System using Flask & ETL

This project is built to manage employee training data. It includes a web interface to upload training CSV files, processes the data using ETL logic in Python, stores it in MySQL, and sends automated email reports.


## Tech Stack:

| Component       | Technology Used     |
|-----------------|---------------------|
| Web Interface   | Flask (Python)      |
| ETL Processing  | Python (Pandas, CSV)|
| Database        | MySQL               |
| Email Reports   | smtplib / email     |
| Version Control | Git & GitHub        |


## Project Structure:

- Config.py 
- FLASK with ETL.py 
- Templates
    - Uploads.html (For FLASK upload webpage)
- static (optional for any picture to upload in webpage like logo etc)
- Daily_training_email.py 
- Export.py (To export the file to local drive from the database)


## Features:

- Upload training data via a Flask web page
- Clean and transform CSV using Python ETL
- Store data in MySQL database
- Automatically send daily email summary of training data to respective persons

