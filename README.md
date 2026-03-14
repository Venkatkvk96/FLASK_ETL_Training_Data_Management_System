# Training HR Training Data Automated System

This project demonstrates a simple data system designed to manage and automate HR training data.

The idea behind this project is to show how workplace data can evolve from scattered records into a structured and automated system.

This repository is part of the story series: "Solving Real Workplace Problems with Data Systems".



# Project Overview



The system allows users to upload training data files and automatically store them in a MySQL database. Instead of manually inserting records, the application handles the process through a simple web interface.





## Tech Stack:

|Component|Technology Used|
|-|-|
|Web Interface|Flask (Python)|
|ETL Processing|Python (Pandas, CSV)|
|Database|MySQL|
|Email Reports|smtplib / email|
|Version Control|Git \& GitHub|



## Project Structure:

* Config.py
* FLASK with ETL.py
* Templates

  * Uploads.html (For FLASK upload webpage)
* static (optional for any picture to upload in webpage like logo etc)
* Daily\_training\_email.py
* Export.py (To export the file to local drive from the database)



## Features:

* Upload training data via a Flask web page
* Clean and transform CSV using Python ETL
* Store data in MySQL database
* Automatically send daily email summary of training data to respective persons





# How It Works:

* User uploads a training data file
* Flask processes the file
* Data is inserted into the MySQL table
* The database becomes ready for reporting and analysis



# Learning Purpose:



This project was created to demonstrate how HR data systems can be built step-by-step:



* Data structure design
* Database schema creation
* Data loading
* Automation through a web interface

