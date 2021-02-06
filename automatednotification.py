#!/usr/bin/env python
# coding: utf-8

import requests 
import smtplib, ssl
import datetime

from bs4 import BeautifulSoup 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from keys import pwd

URL = "http://url.com"
raw = requests.get(URL) 
soup = BeautifulSoup(raw.content, 'html5lib')  

sender_email = "email@gmail.com"
receiver_email = ['email1@gmail.com','email2@gmail.com', 'email3@gmail.com']
password = pwd

date = datetime.datetime.now()
timestamp = date.strftime("%d-%b-%Y (%H:%M:%S.%f)")

subject = "Outstanding Customer DRs as of " + timestamp
message["Subject"] = subject
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

message.attach(MIMEText(soup.prettify(), "html"))

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
