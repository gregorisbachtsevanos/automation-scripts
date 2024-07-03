import imaplib
import email
from email.header import decode_header

# Define your email credentials and IMAP server details
username = 'your_email@example.com'
password = 'your_password'
imap_server = 'imap.example.com'

# Connect to the server and login
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)

# Select the mailbox you want to check
mail.select('inbox')

# Search for emails based on criteria
status, messages = mail.search(None, '(FROM "specific_sender@example.com")')

# Convert messages to a list of email IDs
email_ids = messages[0].split()

# Process each email
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    subject, encoding = decode_header(msg['Subject'])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else 'utf-8')
    
    # Check if subject matches and move email to specific folder
    if 'specific_keyword' in subject:
        mail.store(email_id, '+X-GM-LABELS', 'SpecificFolder')
        mail.store(email_id, '+FLAGS', '\\Deleted')

# Expunge the emails marked for deletion
mail.expunge()

# Logout
mail.logout()
