from tkinter import *
root=Tk()
def callback():
     print("You Clicked!")
b=Button(root, text="OK",command=callback,bg="red",fg="Green")
b.pack()
