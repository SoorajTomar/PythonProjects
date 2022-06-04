import tkinter as tk
from tkinter import *
from tkinter import  messagebox
def f():
    if(radio1.get()==1):
        radio2.set(0) and radio3.set(0)
    elif(radio2.get()==1):
        radio1.set(0) and radio3.set(0)
    elif(radio3.get()==1):
        radio1.set(0) and radio2.set(0)
def hello1():
    if(v1.get()==1):
        msg = messagebox.showinfo( "Acknowledgment","Form Submitted Successfully")
    else:
        msg = messagebox.showinfo("Acknowledgment", "Form not Submitted Successfully since you did not accept T&C")
root=tk.Tk()
root.title('Form')
root.geometry('320x250')
l1=tk.Label(root,text="Full Name")
l1.grid(row=0)
t1=tk.Entry(root)
t1.grid(row=0,column=1)
l2=tk.Label(root,text="Email")
l2.grid(row=1)
t2=tk.Entry(root)
t2.grid(row=1,column=1)
l3=tk.Label(root,text="Password")
l3.grid(row=2)
t3=tk.Entry(root)
t3.grid(row=2,column=1)
l4=tk.Label(root,text="Gender")
l4.grid(row=3)
radio1=IntVar()
radio2=IntVar()
radio3=IntVar()
rb1=Radiobutton(root,text='Male',variable=radio1,command=f)
rb1.grid(row=4,column=1)
rb2=Radiobutton(root,text='Female',variable=radio2,command=f)
rb2.grid(row=5,column=1)
rb3=Radiobutton(root,text='Other',variable=radio2,command=f)
rb3.grid(row=6,column=1)
l5=tk.Label(root,text="Salary")
v1=IntVar()
cb=tk.Checkbutton(root,text='I Accept the Terms and Conditions', variable=v1,onvalue=1, offvalue=0)
cb.grid(row=7,column=1)
b1=tk.Button(root, text='Submit',command=hello1)
b1.grid(row=8,column=1)

root.mainloop()