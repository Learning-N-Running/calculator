import tkinter as tk
from tkinter import *
from account import *
import tkinter.messagebox as msgbox
from tkinter.font import *

import email_test as et
from UserInfoDB import confirm_id_dup, userUpdate,login_check,init_db_when_start,find_id,find_email,Create_temp_pw

def openFrame(frame):
    frame.tkraise()

#login frame 함수
def btnLogin():
    global real_userId,real_password
    real_userId = login_userId_entry.get()
    real_password = login_password_entry.get()
    login_password,ready_login_check= login_check(real_userId)
    if ready_login_check==True and login_password==real_password:
        success_login_response = msgbox.showinfo("로그인 성공","로그인되었습니다.")
        with open('login_info.txt','w') as f:
            id_line = 'id: '+ str(real_userId) + ' \n'
            pw_line = 'pw: '+ str(login_password) +' \n'
            f.write(id_line)
            f.write(pw_line)
        if success_login_response=='ok':
            window.destroy()
            import AfterLogIn

    elif ready_login_check==True and login_password!=real_password:
        fail_login_label = Label(login_frame, text="비밀번호를 잘못 입력하셨습니다.")
        fail_login_label.grid(row = 4, column = 1, padx = 10, pady = 10)
        fail_login_label.after(2000,fail_login_label.destroy)    
            
    elif ready_login_check==False and login_password ==0:
        no_id_label = Label(login_frame, text="입력하신 ID는 존재하지 않습니다.")
        no_id_label.grid(row = 5, column = 1,padx = 10, pady = 10) 
        no_id_label.after(2000,no_id_label.destroy)


def btnJoin():
    window.title("계산기")
    window.geometry("640x480")
    login_userId_entry.delete(0,'end')
    login_password_entry.delete(0,'end')
    openFrame(join_frame)

def btnFindID():
    login_userId_entry.delete(0,'end')
    login_password_entry.delete(0,'end')
    window.title("ID 찾기")
    window.geometry("700x300")
    openFrame(find_id_frame)

def btnFindPW():
    login_userId_entry.delete(0,'end')
    login_password_entry.delete(0,'end')
    window.title("PW 찾기")
    window.geometry("700x300")
    openFrame(find_pw_frame)

#join frame 함수
def get_uups():
    global userId,userName,password,sendTo
    userId=userId_entry.get()
    userName = userName_entry.get()
    password = password_entry.get()
    sendTo = sendTo_entry.get()

def new_userUpdate():
    check_all_info()
    global id_dup_switch
    if ready_send_certification_num==True:
        response = confirm_id_dup(userId)
        if response == False:
            msgbox.showinfo("아이디 중복","동일한 ID가 이미 존재합니다.\n \n다른 ID로 회원가입해주세요.")
            id_dup_switch = 'dup'
        elif response==userId:
            id_dup_switch = 'usable'

        if id_dup_switch=='usable':
            userUpdate(userId,userName,sendTo,password)

            userName_entry.delete(0,'end')
            userId_entry.delete(0,'end')
            password_entry.delete(0,'end')
            sendTo_entry.delete(0,'end')
            certification_entry.delete(0,'end')
            input_certnum_label.destroy()
            certification_entry.destroy()
            cert_num_ok_button.destroy()
            check_certnum_complete_button.destroy()

            openFrame(login_frame)
        else:
            certification_entry.delete(0,'end')
            input_certnum_label.destroy()
            certification_entry.destroy()
            cert_num_ok_button.destroy()
            check_certnum_complete_button.destroy()
    else:
        certification_entry.delete(0,'end')
        input_certnum_label.destroy()
        certification_entry.destroy()
        cert_num_ok_button.destroy()
        check_certnum_complete_button.destroy()

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
                    # print(userName,userId,sendTo,password)

def new_sendEmail():
    global ready_send_certification_num,input_certnum_label,certification_entry,cert_num_ok_button
    ready_send_certification_num=False
    check_all_info()
    if ready_send_certification_num==True:
        global certification_entry,sendTo
        sendTo = sendTo_entry.get()
        et.sendEmail(sendTo)
        if et.correct_email==True:
            input_certnum_label = Label(join_frame, text="인증번호 입력")
            input_certnum_label.grid(row=5, column=0, padx=10, pady=10)
            certification_entry = Entry(join_frame)
            certification_entry.grid(row=5, column=1, padx=10, pady=10)
            cert_num_ok_button = Button(join_frame, text="확인", command=lambda:[check_certnum()])
            cert_num_ok_button.grid(row=5, column=2, padx=10, pady=10)

        else:
            not_prop_email_label = Label(join_frame, text="적절한 이메일 형식이 아닙니다.")
            not_prop_email_label.grid(row=4, column=1, padx=10, pady=10)
            not_prop_email_label.after(2000,not_prop_email_label.destroy)


def check_certnum(): #인증번호 대조
    global certification_num,check_certnum_complete_button
    certification_num = certification_entry.get()
    if int(certification_num) == int(et.cert_num):
        check_certnum_complete_button=Button(join_frame, text="complete", command=lambda:[new_userUpdate()])
        check_certnum_complete_button.grid(row=7, column=1, padx=10, pady=10)
    else:
        cannot_certificate_label = Label(join_frame, text="잘못된 인증번호입니다. \n인증번호를 확인한 다음 다시 입력해주세요.")
        cannot_certificate_label.grid(row=6, column=1, padx=10, pady=10)
        cannot_certificate_label.after(2000,cannot_certificate_label.destroy)

def go_back():
    userName_entry.delete(0,'end')
    userId_entry.delete(0,'end')
    password_entry.delete(0,'end')
    sendTo_entry.delete(0,'end')
    try:
        certification_entry.delete(0,'end')
        input_certnum_label.destroy()
        certification_entry.destroy()
        cert_num_ok_button.destroy()
        check_certnum_complete_button.destroy()
    except:
        pass
    openFrame(login_frame)

def new_confirm_id_dup():
    global userId,id_dup_switch
    userId=userId_entry.get()
    response = confirm_id_dup(userId)
    if response == False:
        msgbox.showinfo("아이디 중복","동일한 ID가 이미 존재합니다.\n \n다른 ID로 회원가입해주세요.")
        id_dup_switch = 'dup'
    elif response==userId:
        msgbox.showinfo("아이디 사용 가능","사용 가능한 ID입니다.")
        id_dup_switch = 'usable'

#find_id_frame 함수
def find_id_goback_func():
    find_id_email_entry.delete(0,'end')
    window.title("계산기")
    window.geometry("640x480")
    openFrame(login_frame)

def find_id_find_button_func():
    id_list = find_id(find_id_email_entry.get())
    blank_list = [' '*n for n in range(1,11)]
    blank_list.append('')
    if find_id_email_entry.get() in blank_list:
        msgbox.showwarning("빈칸 입력","등록하신 이메일을 입력하세요.")
        find_id_email_entry.delete(0,'end')
    else:
        if id_list==[]:
            msgbox.showwarning("등록되지 않은 이메일","등록되지 않은 이메일입니다.")
            find_id_email_entry.delete(0,'end')
        else:
            et.sendEmail_find_id(find_id_email_entry.get(),id_list)
            msgbox.showinfo("ID 전송","{}로 ID를 보냈습니다.\n확인해주세요.".format(find_id_email_entry.get()))
            find_id_email_entry.delete(0,'end')
            window.title("계산기")
            window.geometry("640x480")
            openFrame(login_frame)

#find_pw_frame 함수
def find_pw_goback_func():
    find_pw_inputid_entry.delete(0,'end')
    window.title("계산기")
    window.geometry("640x480")
    openFrame(login_frame)

def find_pw_find_button_func():
    blank_list = [' '*n for n in range(1,11)]
    blank_list.append('')
    if find_pw_inputid_entry.get() in blank_list:
        msgbox.showerror("빈칸 입력","ID를 입력하세요")
        find_pw_inputid_entry.delete(0,'end')
    else:
        email_finded = find_email(find_pw_inputid_entry.get())
        if email_finded==None:
            msgbox.showerror("존재하지 않는 ID",'존재하지 않는 ID입니다.')
            find_pw_inputid_entry.delete(0,'end')
        else:
            response = msgbox.askokcancel('비밀번호 찾기 확인','회원님의 비밀번호가 임시비밀번호로 변경됩니다.\n정말 비밀번호를 찾으시겠습니까?')
            if response==True:
                result = et.sendEmail_find_pw(find_pw_inputid_entry.get(),email_finded)
                msgbox.showinfo("임시 비밀번호 전송"," {}로\n임시 비밀번호를 보내드렸습니다.\n로그인 후 비밀번호를 변경해주세요.".format(email_finded))
                Create_temp_pw(find_pw_inputid_entry.get(),result)
                find_pw_inputid_entry.delete(0,'end')
                window.title("계산기")
                window.geometry("640x480")
                openFrame(login_frame)
            else:
                pass


window = tk.Tk()
window.title("계산기")
window.geometry("640x480") # 가로 * 세로
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

window.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

init_db_when_start()

login_frame = Frame(window)
join_frame = Frame(window)
find_id_frame = Frame(window)
find_pw_frame = Frame(window)


login_frame.grid(row=0, column=0, sticky="nsew")
join_frame.grid(row=0, column=0, sticky="nsew")
find_id_frame.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)
find_pw_frame.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)
#login frame
Label(login_frame, text = "User ID : ").grid(row = 0, column = 0, padx = 10, pady = 10)
Label(login_frame, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)

login_userId_entry =Entry(login_frame)
login_userId_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

login_password_entry = Entry(login_frame, show='*')
login_password_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

Button(login_frame, text = "Login", command = btnLogin).grid(row = 2, column = 0, padx = 10, pady = 10)
Button(login_frame, text = "join", command = btnJoin).grid(row = 2, column = 1, padx = 10, pady = 10)
Button(login_frame, text = "ID 찾기",command=btnFindID).grid(row = 3, column = 0, padx = 10, pady = 10)
Button(login_frame, text = "PW 찾기",command=btnFindPW).grid(row = 3, column = 1, padx = 10, pady = 10)

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

Button(join_frame, text="ID 중복 확인", command=new_confirm_id_dup).grid(row=1, column=2, padx=10, pady=10)

Button(join_frame, text="인증번호 받기", command=lambda:[new_sendEmail()]).grid(row=3, column=2, padx=10, pady=10)

Button(join_frame, text="이전으로", command=go_back).grid(row=7, column=0, padx=10, pady=10)


#find id frame
font1=Font(family="맑은 고딕", size=30)
font2=Font(family="맑은 고딕", size=15)
Label(find_id_frame,text="ID 찾기",font=font1).pack(pady=10)

find_id_email_frame = Frame(find_id_frame)
find_id_email_frame.pack(padx=10)

Label(find_id_email_frame,text="가입시 사용한 이메일:",font=font2).pack(pady=10,side='left')

find_id_email_entry = Entry(find_id_email_frame,font=font2,width=40)
find_id_email_entry.pack(padx=5,side='left')

find_id_find_button = Button(find_id_frame,text="찾기",font=font2,command=lambda:[find_id_find_button_func()],width=10)
find_id_find_button.pack(pady=10)

find_id_go_back_button = Button(find_id_frame,text="이전으로",font=font2,command=lambda:[find_id_goback_func()])
find_id_go_back_button.pack(pady=10, side="left",fill='x',expand=True)


#find_pw_frame
font1=Font(family="맑은 고딕", size=30)
font2=Font(family="맑은 고딕", size=15)

Label(find_pw_frame,text="비밀번호 찾기",font=font1).pack(pady=10)

find_pw_inputid_frame = Frame(find_pw_frame)
find_pw_inputid_frame.pack(padx=10)

Label(find_pw_inputid_frame,text="ID:",font=font2).pack(pady=10,side='left')

find_pw_inputid_entry = Entry(find_pw_inputid_frame,font=font2,width=20)
find_pw_inputid_entry.pack(padx=5,side='left')

find_pw_find_button = Button(find_pw_frame,text="찾기",font=font2,command=lambda:[find_pw_find_button_func()],width=10)
find_pw_find_button.pack(pady=10)

find_pw_go_back_button = Button(find_pw_frame,text="이전으로",command=lambda:[find_pw_goback_func()],font=font2)
find_pw_go_back_button.pack(pady=10, side="left",fill='x',expand=True)






openFrame(login_frame)

window.mainloop()
