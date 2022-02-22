from tkinter import *
from tkinter.font import *


def openFrame(frame):
    frame.tkraise()

class changepw:
    def __init__(self):
        self.window = Tk()
        self.window.title("비밀번호 변경")
        self.window.geometry("480x320")

        #설정들
        self.font1=Font(family="맑은 고딕", size=20)
        self.font2=Font(family="맑은 고딕", size=15)

        self.recent_pw_var = StringVar()
        self.recent_pw_status_var = StringVar()
        self.new_pw_var = StringVar()
        self.new_pw_check_Var = StringVar()

        #window 내의 기능들
        Label(self.window, text = "    ").grid(row = 0, column = 0, padx = 5, pady = 10)
        Label(self.window, text = "    ").grid(row = 1, column = 0, padx = 5, pady = 10)

        Label(self.window, text = "현재 비밀번호").grid(row = 1, column = 1, padx = 5, pady = 10)
        self.present_pw_entry =Entry(self.window, textvariable=self.recent_pw_var).grid(row = 1, column = 2, pady = 10)
        self.check_present_pw_label = Label(self.window, textvariable=self.recent_pw_status_var).grid(row = 1, column = 3, pady = 10)

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
            self.new_pw_label =Label(self.window, text = "새 비밀번호 설정")
            self.new_pw_label.grid(row = 2, column = 1, padx = 5, pady = 10)
            self.new_pw_entry =Entry(self.window, textvariable=self.new_pw_var,show='*')
            self.new_pw_entry.grid(row = 2, column = 2, pady = 10)
            
            self.new_pw_check_label =Label(self.window, text = "새 비밀번호 확인")
            self.new_pw_check_label.grid(row = 3, column = 1, padx = 5, pady = 10)
            self.new_pw_check_entry =Entry(self.window, textvariable=self.new_pw_check_Var,show='*')
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
                self.change_pw_button = Button(self.window, padx=30, pady=5, text="변경")
                self.change_pw_button.grid(row=4, column=2)
            else:
                try:
                    self.change_pw_button.destroy()
                except:
                    pass

if __name__=="__main__":
    a = changepw()
    a.window.mainloop()