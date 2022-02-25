##그룹 찾기 했을 때 나오는 창
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter.ttk import Labelframe
from tkinter.font import *



class searchgroup:
    def __init__(self,newin):
        self.newin = newin
        self.newin.title("그룹 찾기")
        self.newin.geometry("640x480")
        self.newin.resizable(False,False)

        

if __name__ =="__main__":
    root = Tk()
    root.title('원래 거')
    root.geometry('300x300')
    win = Toplevel(root)
    sg_win = searchgroup(win)    
    root.mainloop()