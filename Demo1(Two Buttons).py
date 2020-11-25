from tkinter import *
root = Tk()
def callback():
     print("You Clicked Left Button....i.e (One)")
def callback2():
     print("You Clicked Right Button....i.e (Two)")
button1= Button(root,text="ONE",command=callback,bg="Green",fg="RED")
button2= Button(root,text="TWO",command=callback2,bg="Red",fg="Green")
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
