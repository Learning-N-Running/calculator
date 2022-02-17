import email
import tkinter as tk
from tkinter import *
from tokenize import blank_re
from account import *
import tkinter.messagebox as msgbox

import email_test as et
from UserInfoDB import userUpdate

def openFrame(frame):
    frame.tkraise()

#login frame 함수
def btnLogin():
    global real_userId,real_password
    real_userId = login_userId_entry.get()
    real_password = login_password_entry.get()
    print(real_userId,real_password)
    print("login")


#join frame 함수
def get_uups():
    global userId,userName,password,sendTo
    userId=userId_entry.get()
    userName = userName_entry.get()
    password = password_entry.get()
    sendTo = sendTo_entry.get()

def new_userUpdate():
    get_uups()
    userUpdate(userId,userName,password,sendTo)
    openFrame(login_frame)

def check_all_info(): #이메일 확인 전에 모든 정보를 다 입력했나 확인하는 것
    get_uups()
    global ready_send_certification_num
    blank_list = [' '*n for n in range(1,11)]
    blank_list.append('')
    ready_send_certification_num=False
    if userName in blank_list:
        msgbox.showwarning("경고","이름을 입력해주세요.")
    else:
        if userId in blank_list:
            msgbox.showwarning("경고","ID를 입력해주세요.")
        else:
            if password in blank_list:
                msgbox.showwarning("경고","비밀번호를 입력해주세요.")
            else:
                if sendTo in blank_list:
                    msgbox.showwarning("경고","email을 입력해주세요.")
                else:
                    ready_send_certification_num = True

def new_sendEmail():
    global ready_send_certification_num
    ready_send_certification_num=False
    check_all_info()
    if ready_send_certification_num==True:
        global certification_entry,sendTo
        sendTo = sendTo_entry.get()
        et.sendEmail(sendTo)
        if et.correct_email==True:
            Label(join_frame, text="인증번호 입력").grid(row=5, column=0, padx=10, pady=10)
            certification_entry = Entry(join_frame)
            certification_entry.grid(row=5, column=1, padx=10, pady=10)

            Button(join_frame, text="확인", command=lambda:[check_certnum()]).grid(row=5, column=2, padx=10, pady=10)

        else:
            not_prop_email_label = Label(join_frame, text="적절한 이메일 형식이 아닙니다.")
            not_prop_email_label.grid(row=4, column=1, padx=10, pady=10)
            not_prop_email_label.after(2000,not_prop_email_label.destroy)


def check_certnum(): #인증번호 대조
    global certification_num
    certification_num = certification_entry.get()
    if int(certification_num) == int(et.cert_num):
        Button(join_frame, text="complete", command=lambda:[new_userUpdate()]).grid(row=7, column=1, padx=10, pady=10)
    else:
        cannot_certificate_label = Label(join_frame, text="잘못된 인증번호입니다. \n인증번호를 확인한 다음 다시 입력해주세요.")
        cannot_certificate_label.grid(row=6, column=1, padx=10, pady=10)
        cannot_certificate_label.after(2000,cannot_certificate_label.destroy)


            

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
login_userId_entry, login_password_entry = StringVar(), StringVar()

Label(login_frame, text = "User ID : ").grid(row = 0, column = 0, padx = 10, pady = 10)
Label(login_frame, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
Entry(login_frame, textvariable = login_userId_entry).grid(row = 0, column = 1, padx = 10, pady = 10)
Entry(login_frame, textvariable = login_password_entry, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
Button(login_frame, text = "Login", command = btnLogin).grid(row = 2, column = 0, padx = 10, pady = 10)
Button(login_frame, text = "join", command = lambda:[openFrame(join_frame)]).grid(row = 2, column = 1, padx = 10, pady = 10)

#join frame
Label(join_frame, text="이름").grid(row=0, column=0, padx=10, pady=10)
userName_entry = Entry(join_frame)
userName_entry.grid(row=0, column=1, padx=10, pady=10)

Label(join_frame, text="ID").grid(row=1, column=0, padx=10, pady=10)
userId_entry = Entry(join_frame)
userId_entry.grid(row=1, column=1, padx=10, pady=10)

Label(join_frame, text="비밀번호").grid(row=2, column=0, padx=10, pady=10)
password_entry = Entry(join_frame)
password_entry.grid(row=2, column=1, padx=10, pady=10)

Label(join_frame, text="email").grid(row=3, column=0, padx=10, pady=10)
sendTo_entry = Entry(join_frame, width = 30)
sendTo_entry.grid(row=3, column=1, padx=10, pady=10)


Button(join_frame, text="인증번호 받기", command=lambda:[new_sendEmail()]).grid(row=3, column=2, padx=10, pady=10)

Button(join_frame, text="이전으로", command=lambda:[openFrame(login_frame)]).grid(row=7, column=0, padx=10, pady=10)





openFrame(login_frame)

window.mainloop()