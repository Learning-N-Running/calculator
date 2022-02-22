#내 정보- 내 정보 확인

from tkinter import *
from tkinter.font import *
from UserInfoDB import find_username_email


def openFrame(frame):
    frame.tkraise()

#identify_frame 함수
def identify_button_func():
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
    if identify_pw_entry.get() == login_password:
        username,email = find_username_email(login_id)
        print('yes')
        print(username,email)
        window.geometry('480x240')
        openFrame(watch_my_info_frame)
        Label(watch_my_info_frame, text = username,font=font2).grid(row = 1, column = 2, pady = 10)
        Label(watch_my_info_frame, text = login_id,font=font2).grid(row = 2, column = 2, pady = 10)
        Label(watch_my_info_frame, text = email,font=font2).grid(row = 3, column = 2, pady = 10)

    else:
        print('no')


window = Tk()
window.title("내 정보 확인")
window.geometry("360x240")


#설정들
font1=Font(family="맑은 고딕", size=20)
font2=Font(family="맑은 고딕", size=15)

#비밀번호 확인 프레임(identify_frame)
identify_frame = Frame(window)
identify_frame.grid(row=0, column=0, sticky="nsew")

Label(identify_frame, text = "비밀번호 재확인",font=font1).grid(row = 0, column = 1, padx = 5, pady = 10)
Label(identify_frame, text = "개인정보 보호를 위해\n 비밀번호를 다시 확인합니다.").grid(row = 1, column = 1, padx = 10, pady = 10)
Label(identify_frame, text = "비밀번호: ").grid(row = 2, column = 0, padx = 5, pady = 10)

identify_pw_entry =Entry(identify_frame,width=30,show='*')
identify_pw_entry.grid(row = 2, column = 1, pady = 10)

indentify_button=Button(identify_frame, text="확인", command=identify_button_func)
indentify_button.grid(row=3, column=1, padx=10, pady=10,ipadx=10)


#내 정보 확인 프레임
watch_my_info_frame = Frame(window)
watch_my_info_frame.grid(row=0, column=0, sticky="nsew")
Label(watch_my_info_frame, text = "    ").grid(row = 0, column = 0, padx = 5, pady = 10)
Label(watch_my_info_frame, text = "    ").grid(row = 1, column = 0, padx = 5, pady = 10)

# Label(watch_my_info_frame, text = "내 정보",font=font1).grid(row = 0, column = 2, padx = 5, pady = 10)
Label(watch_my_info_frame, text = "Name:",font=font2).grid(row = 1, column = 1,padx=5, pady = 10)
Label(watch_my_info_frame, text = "ID:",font=font2).grid(row = 2, column = 1,padx=5, pady = 10)
Label(watch_my_info_frame, text = "Email:",font=font2).grid(row = 3, column = 1,padx=5, pady = 10)



openFrame(identify_frame)


window.mainloop()