from app import celery, app

from celery.schedules import crontab


import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@celery.task
def send_mail(subject, text, html, recipients, attachments=[]):
    sender = os.environ.get('MAIL_USERNAME')
    receiver = ",".join(recipients)
    password = os.environ.get('MAIL_PASSWORD')
    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f'Sender Full Name <{sender}>'
    message["To"] = receiver

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(os.environ.get('MAIL_SERVER'), os.environ.get('MAIL_PORT'), context=context) as server:
        server.login(sender, password)
        server.sendmail(
            sender, receiver, message.as_string())