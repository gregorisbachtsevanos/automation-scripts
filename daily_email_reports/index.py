import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email account credentials
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    receiver_email = "receiver_email@example.com"

    # Email content
    subject = "Daily Report"
    body = """
    Hi,

    This is your daily report.

    Best regards,
    Your Automation Script
    """

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily at 8 AM
schedule.every().day.at("08:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
