
from tkinter import*

def delete():
     select=listbox.curselection()
     index=select[0]
     listbox.delete(index)

def add():
    name=entry1.get()
    telephone=entry2.get()
    name.set("")
    telephone.set("")
    listbox.insert(END, name+ ': ' +telephone)
    if name=="":
        labelError=Label(frame1, text="Name is empty", fg="red")
        labelError.grid(columnspan=2)
    if telephone=="":
        labelError2=Label(frame1, text="Telephone is empty", fg="red")
        labelError2.grid(columnspan=2)

def save():
    list1=list(listbox.get(0,END))
    f=open("output.txt", "w")
    f.writelines(str(list1))
    f.close()

wn=Tk()
wn.geometry("350x300")
wn.title("Phone list")

frame1=Frame(wn)
frame2=Frame(wn)
frame1.pack()
frame2.pack()

label2=Label(frame1, text="Name:", font="Calibre 12")
label2.grid(row=1, column=0)
label3=Label(frame1, text="Phone:", font="Calibre 12")
label3.grid(row=2, column=0)

name=StringVar()
entry1=Entry(frame1,textvariable=name)
entry1.grid(row=1, column=1)

telephone=StringVar()
entry2=Entry(frame1,textvariable=telephone)
entry2.grid(row=2, column=1)

scrollbar=Scrollbar(frame2, orient=VERTICAL)

listbox=Listbox(frame2, selectmode=EXTENDED, yscrollcommand=scrollbar.set,width=40)
listbox.grid(row=3, columnspan=3)

scrollbar.config(command=listbox)


button1=Button(frame2, text="Add", width=15, height=1, command=add)
button1.grid(row=5, column=0)

button2=Button(frame2, text="Delete",  width=15, height=1, command=delete)
button2.grid(row=5, column=1)

button3=Button(frame2, text="Update",  width=15, height=1, command=save)
button3.grid(row=5, column=2)

wn.mainloop()