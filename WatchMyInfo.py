#내 정보- 내 정보 확인

from tkinter import *
from tkinter.font import *

#함수
def openFrame(frame):
    frame.tkraise()

def identify_button_func():
    print('내 정보 확인 페이지로 이동합니다.')


window = Tk()
window.title("내 정보 확인")
window.geometry("360x240")


#설정들
font1=Font(family="맑은 고딕", size=20)

#비밀번호 확인 프레임(identify_frame)
identify_frame = Frame(window)
identify_frame.grid(row=0, column=0, sticky="nsew")

Label(identify_frame, text = "비밀번호 재확인",font=font1).grid(row = 0, column = 1, padx = 5, pady = 10)
Label(identify_frame, text = "개인정보 보호를 위해\n 비밀번호를 다시 확인합니다.").grid(row = 1, column = 1, padx = 10, pady = 10)
Label(identify_frame, text = "비밀번호: ").grid(row = 2, column = 0, padx = 5, pady = 10)

identify_pw_entry =Entry(identify_frame,width=30)
identify_pw_entry.grid(row = 2, column = 1, pady = 10)

indentify_button=Button(identify_frame, text="확인", command=identify_button_func)
indentify_button.grid(row=3, column=1, padx=10, pady=10,ipadx=10)


openFrame(identify_frame)


window.mainloop()