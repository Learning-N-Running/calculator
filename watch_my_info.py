from tkinter import *
from tkinter.font import *
import tkinter.messagebox as msgbox
from UserInfoDB import find_username_email

#문제사항 해결하려면 AfterLogin-내정보-내정보확인 들어가기

def openFrame(frame):
    frame.tkraise()

class watchmyinfo:
    def __init__(self,newin):
        self.newin = newin
        self.newin.title("내 정보 확인")
        self.newin.geometry("360x240")

        #설정들
        self.font1=Font(family="맑은 고딕", size=20)
        self.font2=Font(family="맑은 고딕", size=15)

        #비밀번호 확인 프레임(identify_frame)
        self.identify_frame = Frame(self.newin)
        self.identify_frame.grid(row=0, column=0, sticky="nsew")

        Label(self.identify_frame, text = "비밀번호 재확인",font=self.font1).grid(row = 0, column = 1, padx = 5, pady = 10)
        Label(self.identify_frame, text = "개인정보 보호를 위해\n 비밀번호를 다시 확인합니다.").grid(row = 1, column = 1, padx = 10, pady = 10)
        Label(self.identify_frame, text = "비밀번호: ").grid(row = 2, column = 0, padx = 5, pady = 10)
        

        self.identify_pw_entry =Entry(self.identify_frame,width=30,show='*')
        self.identify_pw_entry.grid(row = 2, column = 1, pady = 10)

        #내 정보 확인 프레임(watch_my_info_frame)
        self.watch_my_info_frame = Frame(self.newin)
        self.watch_my_info_frame.grid(row=0, column=0, sticky="nsew")
        Label(self.watch_my_info_frame, text = "    ").grid(row = 0, column = 0, padx = 5, pady = 10)
        Label(self.watch_my_info_frame, text = "    ").grid(row = 1, column = 0, padx = 5, pady = 10)
        Label(self.watch_my_info_frame, text = "Name:",font=self.font2).grid(row = 1, column = 1,padx=5, pady = 10)
        Label(self.watch_my_info_frame, text = "ID:",font=self.font2).grid(row = 2, column = 1,padx=5, pady = 10)
        Label(self.watch_my_info_frame, text = "Email:",font=self.font2).grid(row = 3, column = 1,padx=5, pady = 10)
        
        openFrame(self.identify_frame)

    #identify_frame 함수
    def identify_button_func(self):
        global login_id,login_password,username,email
        with open('login_info.txt','r') as f:
            datas= f.readlines()
            for data in datas:
                data.strip()
                if data.startswith('id'):
                    login_id = data.split()[1]
                elif data.startswith('pw'):
                    login_password = data.split()[1]
                    break
        if self.identify_pw_entry.get() == login_password:
            username,email = find_username_email(login_id)
            print('yes')
            print(username,email)
            self.newin.geometry('480x240')
            openFrame(self.watch_my_info_frame)
            Label(self.watch_my_info_frame, text = username,font=self.font2).grid(row = 1, column = 2, pady = 10)
            Label(self.watch_my_info_frame, text = login_id,font=self.font2).grid(row = 2, column = 2, pady = 10)
            Label(self.watch_my_info_frame, text = email,font=self.font2).grid(row = 3, column = 2, pady = 10)

        else:
            response = msgbox.showwarning("경고","비밀번호를 잘못 입력하셨습니다.")
            if response=='ok':
                self.identify_pw_entry.delete(0,'end')
                self.newin.tkraise()
    
    def second(self):
        self.indentify_button=Button(self.identify_frame, text="확인", command=self.identify_button_func)
        self.indentify_button.grid(row=3, column=1, padx=10, pady=10,ipadx=10)