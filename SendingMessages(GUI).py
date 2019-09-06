#coding: utf-8

from tkinter import *
import sys
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header


def smtpall():
	texxx = window.get()
	tomail = texxx
	text_pisma=window2.get(1.0, 'end')
	mail_subj = window3.get()
	multi_msg = MIMEText(text_pisma,'plain','utf-8')
	multi_msg['From'] = Header(username)
	multi_msg['To'] = Header(tomail)
	multi_msg['Subject'] =  Header(mail_subj)		
	smtpObj = smtplib.SMTP('smtp.mail.ru', 587, "[192.168.1.9]")
	smtpObj.ehlo(name="192.168.1.9")
	#smtpObj.set_debuglevel(1) #debug
	smtpObj.starttls()
	smtpObj.login(username, password)
	smtpObj.sendmail(username, tomail, multi_msg.as_string())
	{}
	print("Сообщение отправлено")
	smtpObj.quit()


def repeating():
	selection = var.get()
	if selection == 0:
		smtpall()
	elif selection == 1:
		for i in range(5):
			smtpall()
	elif selection == 2:
		for i in range(10):
			smtpall()
	elif selection == 3:
		for i in range(30):
			smtpall()
	else:
		pass

def allin():
	global enter_passwd
	global enter_email
	enter_passwd = text_auth_pass.get()
	enter_email = text_auth_mail.get()
	root_auth.close = root_auth.destroy()	

enter_passwd = ""
enter_email = ""


#окно авторизации
mycolor = "gray"
root_auth = Tk()
root_auth.geometry("250x250")
root_auth.title("Авторизация")
root_auth.configure(bg=mycolor)

# Далее такой же стандарт как и в следующем, Label - ввод
text_global = Label(root_auth, text = "Выполните вход", bg= mycolor, font = "arial 14")
text_global.place(x = 20, y = 10)

text_label_auth = Label(root_auth, text = "Email", bg = mycolor)
text_label_auth.place(x = 50 , y = 60)

text_label_pass = Label(root_auth, text = "Password", bg = mycolor)
text_label_pass.place(x = 50 , y = 110)

text_auth_mail = Entry(root_auth)
text_auth_mail.place(x = 50 , y = 80)

button_enter = Button(root_auth, text = "Вход", command = allin)
button_enter.place(x = 50 , y = 170)

text_auth_pass = Entry(root_auth, show = "*")
text_auth_pass.place(x = 50, y = 130)

button_cancel = Button(root_auth, text = "Выход", command = exit)
button_cancel.place(x = 150 , y = 170)


root_auth.mainloop()

#Uname and password нужны для авторизации на самом серваке

username = enter_email.strip()
password = enter_passwd.strip()
#print(username) #приверка ввода Логина
#print(password) #Проверка ввода пароля

# Если поля пусты авторизации выход
if enter_email == "":
	sys.exit()
elif enter_passwd == "":
	sys.exit()

##############################Основное окно

'''GUI оболочка'''
mycolor = "gray"
root = Tk()							
root.title("Smtp ver.2.0")
root.geometry ("350x400")
root.resizable(width = False, height = False)
root.configure(bg=mycolor)

#, height = -5

window = Entry(root, width = 40, bd = 4)   # Окно ввода
window.place(x = 40, y = 20)

text_window = Label(root, text = "Email адрес:", bg = mycolor)  # Текст над окном "ввода"
text_window.place(x = 120, y = -1)


window2 = Text(root,width = 30, height = 5, bd = 4)    # Окно ввода 2
window2.place(x = 40, y = 120)


text_window2 = Label(root, text = "Текст сообщения:", bg = mycolor)    # Текст над окном ввода 2
text_window2.place(x = 100, y = 100)


window3 = Entry(root,width = 40, bd = 4)    # Окно ввода 3
window3.place(x = 40, y = 70)


text_window3 = Label(root, text = "Тема сообщения:", bg = mycolor)    # Текст над окном ввода 3
text_window3.place(x = 100, y = 46)


#Кнопка
button1 = Button(root, text = 'Отправить', command = repeating)
button1.place(x = 40, y = 220, width = "100")
button2 = Button(root, text = 'Выход', command = exit)
button2.place(x = 190, y = 220, width = "100")

									#Radiobutton + текст
text_radiobutton = Label(root, text = "Колличество:", bg = mycolor)
text_radiobutton.place(x = 30, y = 280)

var = IntVar()
var.set(0)
R0 = Radiobutton(root, text = "1", variable = var, value = 0, bg = mycolor)
R1 = Radiobutton(root, text = "5", variable = var, value = 1, bg = mycolor)
R2 = Radiobutton(root, text = "10", variable = var, value = 2, bg = mycolor)
R3 = Radiobutton(root, text = "30", variable = var, value = 3, bg = mycolor)
R0.place(x = 30, y = 300)
R1.place(x = 30, y = 320)
R2.place(x = 30, y = 340)
R3.place(x = 30, y = 360)

root.mainloop()						# Вывод основного окна


