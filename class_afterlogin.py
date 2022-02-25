from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.ttk import Labelframe
from tkinter.font import *

from sqlite3 import IntegrityError

from UserInfoDB import getGroupInfo, insertData, init_db_when_start, insertParticipation
from UserInfoDB import find_username_email,find_user_group
from watch_my_info import *
from change_pw import *
from group_room import *


def openFrame(frame):
    frame.tkraise()

class make_group_class():
    def __init__(self,parent,user_group):
        self.user_group = user_group
        self.group_button = Button(parent.group_list_scrollable_frame,text=self.user_group,width=53,height= 6,font=parent.font2,command = lambda :[self.group_button_func(parent)]).pack()

    def group_button_func(self,parent):
        parent.window.destroy()
        self.gr_win = grouproom(str(self.user_group))
        self.gr_win.window.mainloop()


class after_log:  #after_login.py를 클래스화 한 것
    def __init__(self) :
        self.window = Tk()
        self.window.title("계산기")
        self.window.geometry("640x480")
        self.window.resizable(False,False)

        self.menu = Menu(self.window)

        self.user_group_list = find_user_group()

        #기본 설정
        self.font1=Font(family="맑은 고딕", size=30)
        self.font2=Font(family="맑은 고딕", size=15)

        #메뉴 
        self.menu_info = Menu(self.menu,tearoff=0)
        self.menu_info.add_command(label="내 정보 확인",command=self.CheckMyInfo)
        self. menu_info.add_command(label="비밀번호 변경",command=self.ChangePW)
        self.menu.add_cascade(label="내정보",menu=self.menu_info)

        #그룹 추가, 찾기 프레임
        self.frame_addsearch_group = Frame(self.window)
        self.frame_addsearch_group.pack(fill="x",padx = 5,pady=10)

        self.btn_add_group=Button(self.frame_addsearch_group,padx=5,pady=5,width=12,text="그룹 추가",command=self.addGroup)
        self.btn_add_group.pack(side="left")

        self.btn_search_group=Button(self.frame_addsearch_group,padx=5,pady=5,width=12,text="그룹 찾기",command=self.SearchGroup)
        self.btn_search_group.pack(side="right")


        #그룹들 프레임
        self.frame_group = LabelFrame(self.window,text="내 그룹",relief="solid",bd=1)
        self.frame_group.pack(fill='both',expand=True,padx=10,pady=10)


        self.group_list_container = ttk.Frame(self.frame_group)
        self.group_list_container.pack(side='left',fill='both',expand=True)

        self.group_list_canvas = Canvas(self.group_list_container) 
        self.group_list_canvas.pack(side='left',fill='both',expand=True)


        self.group_list_scrollbar = ttk.Scrollbar(self.group_list_container,orient="vertical",command=self.group_list_canvas.yview)
        self.group_list_scrollbar.pack(side='right',fill='y')
        self.group_list_scrollable_frame = ttk.Frame(self.group_list_canvas)

        self.group_list_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.group_list_canvas.configure(
                scrollregion= self.group_list_canvas.bbox("all")
            )
        )
        self.group_list_canvas.create_window((0,0),window=self.group_list_scrollable_frame,anchor='nw')
        self.group_list_canvas.configure(yscrollcommand=self.group_list_scrollbar.set)

        # for i in range(10):
        #     Button(group_list_scrollable_frame, text="Sample Group button{}".format(i),width=53,height= 6,font=font2).pack()

        for user_group in self.user_group_list:
            globals()['self.{}_group_class'.format(user_group)] = make_group_class(self,user_group)
        
        self.window.config(menu=self.menu)
    
    def CheckMyInfo(self):
        print("내 정보를 확인합니다.")
        self.win_cmi = Toplevel(self.window)
        self.cmi = watchmyinfo(self.win_cmi)
        self.cmi.second()

    def ChangePW(self):
        self.win_cpw = Toplevel(self.window)
        self.cpw = changepw(self.win_cpw)

    def insert_and_check_group(self,gName, gPW):
        self.gName = gName
        self.gPW = gPW
        blank_list = [' '*n for n in range(1,11)]
        blank_list.append('')
        if self.gName in blank_list:
            msgbox.showinfo('부적절한 그룹 이름','그룹 이름을 다시 입력해주세요.')
            self.add_menu.tkraise()
        else:
            if self.gPW in blank_list:
                msgbox.showinfo('부적절한 비밀번호','비밀번호를 다시 입력해주세요.')
                self.add_menu.tkraise()
            else:
                try:
                    insertData(self.gName, self.gPW)
                    # add_menu.destroy()
                    # insertGroupIntoList()
                    self.add_group_complete()
                    # insertParticipation()

                except IntegrityError:
                    msgbox.showerror(title="error", message="중복되는 ID 입니다.")
                    self.add_menu.tkraise()


    def callback(self,*args):
        a = self.pw_var.get()
        b = self.pw_check_var.get()
        blank_list = [' '*n for n in range(1,11)]
        blank_list.append('')
        if a in blank_list or b in blank_list:
            self.lb_var.set("다시 입력하세요.")
        else:
            if a==b:
                self.lb_var.set("비밀번호가 일치합니다.")
            else:
                self.lb_var.set("다시 입력하세요.")
    
    def add_group_complete(self): #모임 추가화면에서 확인 눌렀을 때 마지막으로 실행되는 함수
        msgbox.showinfo("그룹 추가","그룹이 정상적으로 추가되었습니다.")
        self.group_name = self.groupName.get()

        self.window.destroy()
        ##여기 아래 두줄은 클래스로 고쳐주자.
        globals()['{}_gr'.format(str(self.group_name))] = grouproom(str(self.group_name))
        globals()['{}_gr'.format(str(self.group_name))].window.mainloop()

    
    def addGroup(self):
        # global add_menu,groupName,groupPw
        self.add_menu = Toplevel(self.window)
        self.add_menu.geometry("400x400")
        self.add_menu.title("그룹을 추가합니다.")
        
        Label(self.add_menu, padx=40, pady=20, text="그룹 이름").grid()
        self.groupName = Entry(self.add_menu)
        self.groupName.grid(row=0, column=1)

        # global pw_var
        self.pw_var = StringVar()
        # global pw_check_var
        self.pw_check_var = StringVar()
        # global lb_var
        self.lb_var = StringVar()

        Label(self.add_menu, padx=80, pady=30, text="비밀번호").grid()
        # global groupPw
        self.groupPw = Entry(self.add_menu, textvariable=self.pw_var)
        self.groupPw.grid(row=1, column=1)

        Label(self.add_menu, padx=40, pady=30, text="비밀번호 확인").grid()
        # global groupPw_check
        self.groupPw_check = Entry(self.add_menu, textvariable=self.pw_check_var)
        self.groupPw_check.grid(row=2, column=1)

        self.pw_check_var.trace('w', self.callback)
        self.pw_var.trace('w',self.callback)

        self.check_label = Label(self.add_menu, pady=10, textvariable=self.lb_var, fg="red", justify=LEFT)
        self.check_label.grid(row=3, columnspan=2)

        Button(self.add_menu, padx=30, pady=10, text="확인", command=lambda:[self.insert_and_check_group(self.groupName.get(), self.groupPw.get())]).grid(row=4, column=0)
        Button(self.add_menu, padx=30, pady=10, text="취소", command=self.add_menu.destroy).grid(row=4, column=1)
        # Button(add_menu, padx=30, pady=5, text="확인", command=add_group_complete).grid(row=5, column=0)
        # Button(add_menu, padx=30, pady=5, text="취소").grid(row=5, column=1)

        # add_menu.bind("<Keys>", checkPassword)

    def SearchGroup(self):
        print("그룹을 찾습니다")

    # def insertGroupIntoList(self):
    #     self.group_name = getGroupInfo()[-1][0]
    #     self.line = Button(group_list_scrollable_frame,text=group_name,width=53,height= 6,font=font2)
    #     globals()['group_{}_button'.format(group_name)] = line
    #     globals()['group_{}_button'.format(group_name)].pack()









# window.config(menu=menu)
# window.mainloop()

k = after_log()

k.window.mainloop()