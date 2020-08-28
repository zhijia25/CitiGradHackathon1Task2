#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import csv
from email.mime.text import MIMEText
from email.utils import formataddr

def sendEmail(websiteName):
    my_sender = '1622898550@qq.com'  # Sender's email account
    my_pass = 'xxxxxxxxxxxxxxxxxx'  # Sender's mailbox password
    ret = True
    try:
        clientList = []
        with open('.\clientList.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                clientList.append(line)
                if line[0].isdigit():
                    my_user = line[2]
                    msg = MIMEText('Dear '+line[1]+',\n\n        Sorry to inform'\
                          ' you that the website \"'+ websiteName +'\" failed to access.\n\nBest wishes\nGroup 13', 'plain', 'utf-8')
                    msg['From'] = formataddr(["Group 13", my_sender])  # sender’s email nickname and sender’s email account
                    msg['To'] = formataddr(["FK", my_user])  # recipient's email nickname, recipient's email account
                    msg['Subject'] = "Website \"" + websiteName + "\" request failed [Remind from Group 13]"  # Email Subject

                    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # The SMTP server in the sender's mailbox, the port is 25
                    server.login(my_sender, my_pass)  # Sender's email account and email password
                    server.sendmail(my_sender, [my_user, ], msg.as_string())  # Sender's email account, recipient's email account, sending email
                    server.quit()  # Close the connection
    except Exception:
        ret = False
    return ret

# Test
ret = sendEmail('www.xxx.com')

if ret:
    print("Email sent successfully")
else:
    print("Email failed to send")

