import tkinter as tk
from tkinter import *
from account import *

import email_test as et
from UserInfoDB import userUpdate

def btnLogin():
    print("login")

def openFrame(frame):
    frame.tkraise()

def printall():
    global userId,userName,password,sendTo
    userId=userId_entry.get()
    userName = userName_entry.get()
    password = password_entry.get()
    sendTo = sendTo_entry.get()
    print(userId,userName,password,sendTo)

def new_userUpdate():
    global userId,userName,password,sendTo
    userId=userId_entry.get()
    userName = userName_entry.get()
    password = password_entry.get()
    sendTo = sendTo_entry.get()
    userUpdate(userId,userName,password,sendTo)

def new_sendEmail():
    global sendTo
    sendTo = sendTo_entry.get()
    et.sendEmail(sendTo)


window = tk.Tk()
window.title("Nado GUI")
window.geometry("640x480") # 가로 * 세로
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

window.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

login_frame = Frame(window)
join_frame = Frame(window)

login_frame.grid(row=0, column=0, sticky="nsew")
join_frame.grid(row=0, column=0, sticky="nsew")

#login frame
user_id, login_password = StringVar(), StringVar()

Label(login_frame, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
Label(login_frame, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
Entry(login_frame, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
Entry(login_frame, textvariable = login_password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
Button(login_frame, text = "Login", command = btnLogin).grid(row = 2, column = 0, padx = 10, pady = 10)
Button(login_frame, text = "join", command = lambda:[openFrame(join_frame)]).grid(row = 2, column = 1, padx = 10, pady = 10)

#join frame
Label(join_frame, text="name").grid(row=0, column=0, padx=10, pady=10)
userName_entry = Entry(join_frame)
userName_entry.grid(row=0, column=1, padx=10, pady=10)

Label(join_frame, text="id").grid(row=1, column=0, padx=10, pady=10)
userId_entry = Entry(join_frame)
userId_entry.grid(row=1, column=1, padx=10, pady=10)

Label(join_frame, text="pw").grid(row=2, column=0, padx=10, pady=10)
password_entry = Entry(join_frame)
password_entry.grid(row=2, column=1, padx=10, pady=10)

Label(join_frame, text="email").grid(row=3, column=0, padx=10, pady=10)
sendTo_entry = Entry(join_frame, width = 30)
sendTo_entry.grid(row=3, column=1, padx=10, pady=10)





Button(join_frame, text="인증", command=lambda:[new_sendEmail()]).grid(row=3, column=2, padx=10, pady=10)

Button(join_frame, text="이전으로", command=lambda:[openFrame(login_frame)]).grid(row=4, column=0, padx=10, pady=10)
# Button(join_frame, text="complete", command=lambda:[openFrame(room)]).grid(row=4, column=1, padx=10, pady=10)
Button(join_frame, text="complete", command=lambda:[new_userUpdate()]).grid(row=4, column=1, padx=10, pady=10)

#출력 버튼은 userId등이 entry에 저장이 되는지 확인하기 위해 임의로 만든 버튼
Button(join_frame, text="출력", command=lambda:[printall()]).grid(row=4, column=2, padx=10, pady=10)

openFrame(login_frame)

window.mainloop()