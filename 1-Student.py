import tkinter as tk
from tkinter import *
from tkinter import  messagebox
def f():
    if(radio1.get()==1):
        radio2.set(0)
    elif(radio2.get()==1):
        radio1.set(0)
def hello1():
 msg = messagebox.showinfo( "Confirmation","Inserted Sucessfully")
def hello2():
 msg = messagebox.showinfo( "Confirmation","Updated Sucessfully")
def hello3():
 msg = messagebox.showinfo( "Confirmation","Deleted Sucessfully")
def hello4():
 msg = messagebox.showinfo( "Confirmation","Select Button")
root=tk.Tk()
root.title('tk')
root.geometry('300x200')
l1=tk.Label(root,text="Regno")
l1.grid(row=0)
t1=tk.Entry(root)
t1.grid(row=0,column=1)
l2=tk.Label(root,text="Name:")
l2.grid(row=1)
t2=tk.Entry(root)
t2.grid(row=1,column=1)
v = StringVar(root, value='CSE')
l3=tk.Label(root,text="Dept")
l3.grid(row=2)
t3=tk.Entry(root,textvariable=v)
t3.grid(row=2,column=1)
l4=tk.Label(root,text="Gender")
l4.grid(row=3)
radio1=IntVar()
radio2=IntVar()
rb1=Radiobutton(root,text='Male',variable=radio1)
rb1.grid(row=3,column=1)
rb2=Radiobutton(root,text='Female',variable=radio2)
rb2.grid(row=3,column=2)
l5=tk.Label(root,text="Age")
l5.grid(row=4)
spin = Spinbox(root,from_=15,to=20)
spin.grid(row=4,column=1)
b1=tk.Button(root, text='Insert',command=hello1)
b1.grid(row=5,column=0)
b2=tk.Button(root, text='Update',command=hello2)
b2.grid(row=5,column=1)
b3=tk.Button(root, text='Delete',command=hello3)
b3.grid(row=6,column=0)
b4=tk.Button(root, text='Select',command=hello4)
b4.grid(row=6,column=1)
root.mainloop()

