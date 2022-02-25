from http.client import ResponseNotReady
from tkinter import *
from tkinter.font import *
import tkinter.messagebox as msgbox
from UserInfoDB import change_pw

#문제사항 해결하려면 AfterLogin-내정보-비밀번호변경 들어가기

def openFrame(frame):
    frame.tkraise()

class changepw:
    def __init__(self,newin):
        self.newin = newin
        self.newin.title("비밀번호 변경")
        self.newin.geometry("480x320")


        #설정들
        self.font1=Font(family="맑은 고딕", size=20)
        self.font2=Font(family="맑은 고딕", size=15)

        self.recent_pw_var = StringVar()
        self.recent_pw_status_var = StringVar()
        self.new_pw_var = StringVar()
        self.new_pw_check_Var = StringVar()

        #window 내의 기능들
        Label(self.newin, text = "    ").grid(row = 0, column = 0, padx = 5, pady = 10)
        Label(self.newin, text = "    ").grid(row = 1, column = 0, padx = 5, pady = 10)

        Label(self.newin, text = "현재 비밀번호").grid(row = 1, column = 1, padx = 5, pady = 10)
        self.present_pw_entry =Entry(self.newin, textvariable=self.recent_pw_var,show='*').grid(row = 1, column = 2, pady = 10)
        self.check_present_pw_label = Label(self.newin, textvariable=self.recent_pw_status_var).grid(row = 1, column = 3, pady = 10)

        with open('login_info.txt','r') as f:
            self.datas= f.readlines()
            for data in self.datas:
                data.strip()
                if data.startswith('id'):
                    self.login_id = data.split()[1]
                elif data.startswith('pw'):
                    self.login_password = data.split()[1]
                    break

        self.recent_pw_var.trace('w',self.first_callback)
    
    def first_callback(self,*args):
        c = self.recent_pw_var.get()
        d = self.login_password
        if c==d:
            self.recent_pw_status_var.set("새 비밀번호 설정 가능")
            self.new_pw_label =Label(self.newin, text = "새 비밀번호 설정")
            self.new_pw_label.grid(row = 2, column = 1, padx = 5, pady = 10)
            self.new_pw_entry =Entry(self.newin, textvariable=self.new_pw_var,show='*')
            self.new_pw_entry.grid(row = 2, column = 2, pady = 10)
            
            self.new_pw_check_label =Label(self.newin, text = "새 비밀번호 확인")
            self.new_pw_check_label.grid(row = 3, column = 1, padx = 5, pady = 10)
            self.new_pw_check_entry =Entry(self.newin, textvariable=self.new_pw_check_Var,show='*')
            self.new_pw_check_entry.grid(row = 3, column = 2, pady = 10)

            self.new_pw_check_Var.trace('w',self.second_callback)
            self.new_pw_var.trace('w',self.second_callback)
        else:
            self.recent_pw_status_var.set("새 비밀번호 설정 불가")
            try:
                self.new_pw_label.destroy()
                self.new_pw_entry.destroy()
                self.new_pw_check_label.destroy()
                self.new_pw_check_entry.destroy()
            except:
                pass

    def second_callback(self,*args):
        a = self.new_pw_var.get()
        b = self.new_pw_check_Var.get()

        blank_list = [' '*n for n in range(1,11)]
        blank_list.append('')
        if a in blank_list or b in blank_list:
            pass
        else:
            if a==b:
                self.change_pw_button = Button(self.newin, padx=30, pady=5, text="변경",command=self.new_change_pw)
                self.change_pw_button.grid(row=4, column=2)
            else:
                try:
                    self.change_pw_button.destroy()
                except:
                    pass
                
    def new_change_pw(self):
        response = msgbox.askokcancel("비밀번호 변경 확인","정말 비밀번호를 변경하시겠습니까?")
        if response==True:
            change_pw(self.recent_pw_var.get(),self.new_pw_var.get())
            with open('login_info.txt','w') as f:
                id_line = 'id: '+ str(self.login_id) + ' \n'
                pw_line = 'pw: '+ str(self.new_pw_var.get()) +' \n'
                f.write(id_line)
                f.write(pw_line)
            msgbox.showinfo("알림","비밀번호가 정상적으로 변경되었습니다.")
            self.newin.destroy()
