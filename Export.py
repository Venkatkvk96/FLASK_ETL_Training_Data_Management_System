import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="training"
)

query = "SELECT * FROM employee_details"
df = pd.read_sql(query, conn)
df.to_csv("employee_details.csv", index=False)