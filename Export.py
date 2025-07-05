import mysql.connector
import pandas as pd
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

# Connect to MySQL using config values
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

# Query and export to CSV
query = "SELECT * FROM employee_details"
df = pd.read_sql(query, conn)
df.to_csv("employee_details.csv", index=False)

print("✅ Exported to employee_details.csv successfully.")
