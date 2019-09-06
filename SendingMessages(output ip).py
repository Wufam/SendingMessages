#!/usr/bin/python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import sys
import subprocess

ask = subprocess.check_output(["curl", "smart-ip.net/myip"])
ask= ask.strip()
ask = ask.decode("utf-8")


def smtpall():
	multi_msg = MIMEText(text,'plain','utf-8')
	multi_msg['From'] = Header(username)
	multi_msg['To'] = Header(tomail)
	multi_msg['Subject'] =  Header(mail_subj)
	smtpObj = smtplib.SMTP('smtp.mail.ru', 587, "[your ip_in]")
	smtpObj.ehlo(name="your ip_in")
	#smtpObj.set_debuglevel(1) #debug
	smtpObj.starttls()
	smtpObj.login(username, password)
	smtpObj.sendmail(username, tomail, multi_msg.as_string())
	{}
	print("Сообщение отправлено")
	smtpObj.quit()

#to mail
tomail = 'who@mail.ru'

username = 'your@mail.ru'
password = 'your password'

mail_subj = 'Твой IP'
text = ask
multi_msg = MIMEText(text,'plain','utf-8')
multi_msg['From'] = Header(username)
multi_msg['To'] = Header(tomail)
multi_msg['Subject'] =  Header(mail_subj)

if __name__ == "__main__":
	start = smtpall()
