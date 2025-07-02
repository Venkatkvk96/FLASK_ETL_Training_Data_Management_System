import pandas as pd
import pymysql
import smtplib
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pandas.io.sql")
from email.message import EmailMessage
from email.utils import formatdate
from email.mime.application import MIMEApplication

# --- DB Connection ---
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",  # 🔁 Replace with your MySQL password
    database="training"
)

# --- Fetch Today's Training Data ---
query = """
SELECT Training_Date, Department, Course, Training_Mode, Training_Hours
FROM Employee_Details
WHERE Training_Date = '2025-06-20';
"""

df = pd.read_sql(query, connection)
connection.close()

# --- Prepare Email ---
msg = EmailMessage()
msg['Subject'] = "📊 Daily Training Report"
msg['From'] = "syrma.venkat@gmail.com"         # 🔁 Your email
msg['To'] = "venkatkvk96@gmail.com"             # 🔁 Recipient(s)
msg['Date'] = formatdate(localtime=True)

# Handle empty data
if df.empty:
    msg.set_content("No training sessions recorded today.")
    msg.add_alternative(f"""
    <html><body>
    <p>Hello Team,</p>
    <p>No training sessions were recorded for today.</p>
    <p>Regards,<br>Your Automated Training System</p>
    </body></html>
    """, subtype='html')
else:
    # Save to Excel
    file_path = "daily_training_report.xlsx"
    df.to_excel(file_path, index=False)

    html_table = df.to_html(index=False)
    msg.set_content("Attached is the daily training summary.")
    msg.add_alternative(f"""
    <html><body>
    <p>Hello Team,</p>
    <p>Here is the training summary for today:</p>
    {html_table}
    <p>Regards,<br>Your Automated Training System</p>
    </body></html>
    """, subtype='html')

    # Attach Excel
    with open(file_path, 'rb') as f:
        part = MIMEApplication(f.read(), Name="Training_Report.xlsx")
        part['Content-Disposition'] = 'attachment; filename="Training_Report.xlsx"'
        msg.attach(part)

# --- Send Email (Gmail SMTP) ---
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login("syrma.venkat@gmail.com", "rexfyqxitgqfylqp")  # 🔁 Use Gmail app password
    server.send_message(msg)

print("✅ Email sent successfully.")
