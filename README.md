Email Sender using Python and SMTP

This project allows you to send emails using Python and SMTP via Gmail. It utilizes the smtplib library for email communication and dotenv for managing environment variables securely.

Features

Sends emails using Python.

Uses SMTP with Gmail for email delivery.

Environment variables for secure credential management.

Prerequisites

Python 3.x installed.

A Gmail account.

Enable "Less Secure Apps" access in your Google account (or set up an App Password for better security).

Installation

Clone the repository:

git clone https://github.com/your-username/email-sender.git
cd email-sender

Install required dependencies:

pip install -r requirements.txt

Create a .env file in the project directory and add your email credentials:

EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-email-password

Usage

Run the Python script to send an email:

python send_email.py

If configured correctly, an email will be sent to the specified recipient.

Configuration

Modify receiver_email, subject, and body in send_email.py to customize the email content.

Ensure SMTP settings are correctly configured:

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

Security Considerations

Never share your email password directly in the code. Use environment variables instead.

Consider using an App Password instead of your actual Gmail password for better security.

If using a corporate or custom domain email, ensure SMTP settings are correctly configured.

License

This project is open-source and available under the MIT License.

Contributing

Feel free to open issues or submit pull requests for improvements!

✅ Happy Coding! 🚀
