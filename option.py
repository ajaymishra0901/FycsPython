
from tkinter import *
root=Tk()
v=IntVar()
v.set(0)
lang_list=[("Python",0),("Java",1),("c",2),("DOT nET",3),("PHP",4,)]
def ShowChoice():
    print("Hey,your selected choice is:",v.get())
l=Label(root,text="Select Your Favourite Proramming Language:")
l.pack()
for txt,val in lang_list:
    r=Radiobutton(root,text=txt,variable=v,command=ShowChoice,value=val)
    r.pack()

