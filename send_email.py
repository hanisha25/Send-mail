import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# ✅ Correct way to fetch environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# SMTP Settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email Details
receiver_email = "nambaruhanisha@gmail.com"  # Change to actual recipient's email
subject = "Test Email via SMTP"
body = "Hello! This is a test email sent using Python and SMTP."

# Create Email
msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Debugging: Print environment variables (for testing only)
print("EMAIL_ADDRESS:", EMAIL_ADDRESS)  
print("EMAIL_PASSWORD:", EMAIL_PASSWORD)  

# Send Email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure the connection
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")