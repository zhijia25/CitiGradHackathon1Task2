#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import csv
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1622898550@qq.com'  # 发件人邮箱账号
my_pass = 'xxxxxxxxxxxx'  # 发件人邮箱密码


def mail():
    ret = True
    try:
        clientList = []
        with open('.\clientList.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                clientList.append(line)
                if line[0].isdigit():
                    my_user = line[2]
                    msg = MIMEText('Dear '+line[1], 'plain', 'utf-8')
                    msg['From'] = formataddr(["From CITI", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                    msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                    msg['Subject'] = "CITI"  # 邮件的主题，也可以说是标题

                    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
                    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
                    server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                    server.quit()  # 关闭连接


    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

ret = mail()# 收件人邮箱账号

if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")