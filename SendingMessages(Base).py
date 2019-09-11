#coding: utf-8
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import sys

def smtpall():
	smtpObj = smtplib.SMTP('smtp.yandex.ru', 587, "[10.100.100.195]")
	smtpObj.ehlo(name="10.100.100.195")
	smtpObj.set_debuglevel(1)
	smtpObj.starttls()
	smtpObj.login(username, password)
	smtpObj.sendmail(username, tomail, multi_msg.as_string())
	{}
	smtpObj.quit()

#to mail
tomail = 'mail@mail.ru'

#password
file1 = open('pa.txt')
for pa in file1:
    password = pa.strip()
#username
file2 = open('lo.txt')
for us in file2:
    username = us.strip()
mail_subj = 'Тестовое письмо'
text = input('Введите текст письма: ')
multi_msg = MIMEText(text,'plain','utf-8')
multi_msg['From'] = Header(username)
multi_msg['To'] = Header(tomail)
multi_msg['Subject'] =  Header(mail_subj)
 



'''
#message
tes = input('Введите текст письма: ')
text = tes
msg = MIMEText(text,'','utf-8')
FROM = username
TO = tomail
SUBJECT = "This is no spam"


body = "\r\n".join(("From: %s" % FROM,"To: %s"% TO, "Subject: %s" % SUBJECT,"", text))
msg = body
'''
try_count = input('Введите колличество отправок(1-5): ')

if try_count == '1':
	for i in range(1):
		smtpall()
	print("Сообщение отправлено")
	try_count = input('Введите колличество отправок(1-5) иди (0) для выхода: ')

elif try_count == '2':
	for i in range(2):
		smtpall()
	print("Сообщение отправлено")
	try_count = input('Введите колличество отправок(1-5) иди (0) для выхода: ')

elif try_count == '3':
	for i in range(3):
		smtpall()
	print("Сообщение отправлено")
	try_count = input('Введите колличество отправок(1-5) иди (0) для выхода: ')

elif try_count == '4':
	for i in range(4):
		smtpall()
	print("Сообщение отправлено")
	try_count = input('Введите колличество отправок(1-5) иди (0) для выхода: ')

elif try_count == '5':
	for i in range(5):
		smtpall()
	print("Сообщение отправлено")
	try_count = input('Введите колличество отправок(1-5) иди (0) для выхода: ')

else:
	sys.exit()
	print('Выход из программы')
			





