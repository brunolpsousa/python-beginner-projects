from email.message import EmailMessage

# Import email and password variables from a passwd.py file
from passwd import email, password
import ssl
import smtplib

email_sender = email
email_password = password

email_receiver = "test@mail.com"

subject = "Just a mail"
body = """
When you receive an email, please read it.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
