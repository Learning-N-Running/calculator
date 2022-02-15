from tkinter import *

# def openFrame(frame):
#     frame.tkraise()

# window = Tk()
# window.title("frame")
# window.geometry("600x600")

# frame1 = Frame(window)
# frame2 = Frame(window)

# frame1.grid(row=0, column=0, sticky="nsew")
# frame2.grid(row=0, column=0, sticky="nsew")

# btnToFrame2 = Button(frame1, text="f2", command=lambda:[openFrame(frame2)])

# btnToFrame2.pack()
# openFrame(frame1)

# window.mainloop()

# import frame_class

# f1 = frame_class.SampleApp()
window = Tk()
room = Frame(window).pack()
Button(room, text="room").pack()

afterLogin = Frame(room).pack()
Button(afterLogin, text="afterLogin").pack()
window.mainloop()
