from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.ttk import Labelframe

from UserInfoDB import getGroupInfo, insertData


window = Tk()
window.title("계산기")
window.geometry("640x480")

menu = Menu(window)

#함수 정리
def CheckMyInfo():
    print("내 정보를 확인합니다.")

def ChangePW():
    response = msgbox.askokcancel("비밀번호 변경 확인","비밀번호를 변경하시겠습니까?")
    if response==1: #확인
        print("비밀번호를 변경합니다.")

def callback(*args):
    a = pw_var.get()
    b = pw_check_var.get()

    if a==b:
        lb_var.set("success")
        return

def addGroup():
    global add_menu
    add_menu = Toplevel(window)
    add_menu.geometry("400x400")
    add_menu.title("모임을 추가합니다.")
    
    Label(add_menu, padx=40, pady=20, text="모임 이름").grid()
    groupName = Entry(add_menu)
    groupName.grid(row=0, column=1)

    Label(add_menu, padx=40, pady=20, text="지역").grid()
    groupSite = Entry(add_menu)
    groupSite.grid(row=1, column=1)

    global pw_var
    pw_var = StringVar()
    global pw_check_var
    pw_check_var = StringVar()
    global lb_var
    lb_var = StringVar()

    Label(add_menu, padx=40, pady=20, text="비밀번호").grid()
    global groupPw
    groupPw = Entry(add_menu, textvariable=pw_var)
    groupPw.grid(row=2, column=1)

    Label(add_menu, padx=40, pady=20, text="비밀번호 확인").grid()
    global groupPw_check
    groupPw_check = Entry(add_menu, textvariable=pw_check_var)
    groupPw_check.grid(row=3, column=1)

    pw_check_var.trace('w', callback)

    check_label = Label(add_menu, textvariable=lb_var, background="ivory")
    check_label.grid()

    Button(add_menu, padx=30, pady=5, text="확인", command=lambda:[insertData(groupName.get(), groupSite.get(), groupPw.get())]).grid(row=5, column=0)
    Button(add_menu, padx=30, pady=5, text="취소").grid(row=5, column=1)

    # add_menu.bind("<Keys>", checkPassword)

def addList(frame):
    group_list = getGroupInfo()
    for i in range(len(group_list)):
        Label(frame, text=group_list[i], width=50, padx=10, pady=10, background="ivory").pack(expand=True, side="top")
        Button(frame, text="입장", width=50, padx=10, pady=10).pack(expand=True)

def SearchGroup():
    print("그룹을 찾습니다")

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

group_list = Listbox(frame_group,selectmode='single',yscrollcommand=group_scrollbar.set)
#height값을 줘야할지 말아야할지 고민
group_list.pack(side='left', fill='both',expand=True)

group_scrollbar.config(command=group_list.yview)



window.config(menu=menu)
window.mainloop()