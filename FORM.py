from tkinter import*
root=Tk()
def display():
    print("USER_Name:"+ent1.get())
    print("YOUR EMAIL:"+ent2.get())
    print("YOUR CONTACT:"+ent3.get())
l1=Label(root,text="Enter Name")
l1.grid(row=0,column=0)
ent1=Entry(root)
ent1.grid(row=0,column=1)
l2=Label(root,text="Enter Email")
l2.grid(row=1,column=0)
ent2=Entry(root)
ent2.grid(row=1,column=1)
l3=Label(root,text="Enter contact")
l3.grid(row=2,column=0)
ent3=Entry(root)
ent3.grid(row=2,column=1)
l4=Label(root,text="Hobbies")
l4.grid(row=3,column=0)

def var_states():
    print("H1:%d,\nH2:%d,\n3:%d"%(var1.get(),var2.get(),var3.get()))
var1=IntVar()
c1=Checkbutton(root,text="H1",command=var_states,variable=var1)
var2=IntVar()
c2=Checkbutton(root,text="H2",command=var_states,variable=var2)
var3=IntVar()
c3=Checkbutton(root,text="H3",command=var_states,variable=var3)

c1.grid(row=3,column=1)
c2.grid(row=3,column=2)
c3.grid(row=3,column=4)

b=Button(root,text="Submit",command=display)
b.grid(row=5,column=0)



