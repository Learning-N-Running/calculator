from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.ttk import Labelframe
from tkinter.font import *

from sqlite3 import IntegrityError

from UserInfoDB import getGroupInfo, insertData, init_db_when_start, insertParticipation
from UserInfoDB import find_username_email
from watch_my_info import *
from change_pw import *
from group_room import *


window = Tk()
window.title("계산기")
window.geometry("640x480")

menu = Menu(window)


#함수 정리
def openFrame(frame):
    frame.tkraise()
    

def CheckMyInfo():
    print("내 정보를 확인합니다.")
    win_cmi = Toplevel(window)
    cmi = watchmyinfo(win_cmi)
    cmi.second()

def ChangePW():
    win_cpw = Toplevel(window)
    cpw = changepw(win_cpw)

def insert_and_check_group(gName, gPW):
    try:
        insertData(gName, gPW)
        insertGroupIntoList()
        add_group_complete()

    except IntegrityError:
        msgbox.showerror(title="error", message="중복되는 ID 입니다.")
        add_menu.tkraise()

def callback(*args):
    a = pw_var.get()
    b = pw_check_var.get()
    blank_list = [' '*n for n in range(1,11)]
    blank_list.append('')
    if a in blank_list or b in blank_list:
        lb_var.set("다시 입력하세요.")
    else:
        if a==b:
            lb_var.set("비밀번호가 일치합니다.")
        else:
            lb_var.set("다시 입력하세요.")
    
def add_group_complete(): #모임 추가화면에서 확인 눌렀을 때
    # insertData(groupName.get(), groupSite.get(), groupPw.get()) #여기서 그룹번호를 return하게 만들기
    msgbox.showinfo("그룹 추가","그룹이 정상적으로 추가되었습니다.")
    group_name = groupName.get()

    window.destroy()
    gr = grouproom(str(group_name))

    gr.window.mainloop()

    
def addGroup():
    global add_menu,groupName,groupSite,groupPw
    add_menu = Toplevel(window)
    add_menu.geometry("400x400")
    add_menu.title("그룹을 추가합니다.")
    
    Label(add_menu, padx=40, pady=20, text="그룹 이름").grid()
    groupName = Entry(add_menu)
    groupName.grid(row=0, column=1)

    global pw_var
    pw_var = StringVar()
    global pw_check_var
    pw_check_var = StringVar()
    global lb_var
    lb_var = StringVar()

    Label(add_menu, padx=80, pady=30, text="비밀번호").grid()
    global groupPw
    groupPw = Entry(add_menu, textvariable=pw_var)
    groupPw.grid(row=1, column=1)

    Label(add_menu, padx=40, pady=30, text="비밀번호 확인").grid()
    global groupPw_check
    groupPw_check = Entry(add_menu, textvariable=pw_check_var)
    groupPw_check.grid(row=2, column=1)

    pw_check_var.trace('w', callback)

    check_label = Label(add_menu, pady=10, textvariable=lb_var, fg="red", justify=LEFT)
    check_label.grid(row=3, columnspan=2)

    Button(add_menu, padx=30, pady=10, text="확인", command=lambda:[insert_and_check_group(groupName.get(), groupPw.get())]).grid(row=4, column=0)
    Button(add_menu, padx=30, pady=10, text="취소", command=add_menu.destroy).grid(row=4, column=1)
    # Button(add_menu, padx=30, pady=5, text="확인", command=add_group_complete).grid(row=5, column=0)
    # Button(add_menu, padx=30, pady=5, text="취소").grid(row=5, column=1)

    # add_menu.bind("<Keys>", checkPassword)

    
def addList(frame):
    group_list = getGroupInfo()
    for i in range(len(group_list)):
        Label(frame, text=group_list[i], width=50, padx=10, pady=10, background="ivory").pack(expand=True, side="top")
        Button(frame, text="입장", width=50, padx=10, pady=10).pack(expand=True)

def SearchGroup():
    print("그룹을 찾습니다")

def insertGroupIntoList():
    group_list.insert(END, getGroupInfo()[-1])


#메뉴 
menu_info = Menu(menu,tearoff=0)
menu_info.add_command(label="내 정보 확인",command=CheckMyInfo)
menu_info.add_command(label="비밀번호 변경",command=ChangePW)
menu.add_cascade(label="내정보",menu=menu_info)

#그룹 추가, 찾기 프레임
frame_addsearch_group = Frame(window)
frame_addsearch_group.pack(fill="x",padx = 5,pady=10)

btn_add_group=Button(frame_addsearch_group,padx=5,pady=5,width=12,text="그룹 추가",command=addGroup)
btn_add_group.pack(side="left")

btn_search_group=Button(frame_addsearch_group,padx=5,pady=5,width=12,text="그룹 찾기",command=SearchGroup)
btn_search_group.pack(side="right")

#그룹들 프레임
frame_group = LabelFrame(window,text="내 그룹",relief="solid",bd=1)
frame_group.pack(fill='both',expand=True,padx=10,pady=10)

group_scrollbar = Scrollbar(frame_group)
group_scrollbar.pack(side='right',fill='y')

group_list = Listbox(frame_group,selectmode='single', yscrollcommand=group_scrollbar.set)
#height값을 줘야할지 말아야할지 고민
group_list.pack(side='left', fill='both',expand=True)

for i in getGroupInfo():
    group_list.insert(END, i)

group_scrollbar.config(command=group_list.yview)



window.config(menu=menu)
window.mainloop()