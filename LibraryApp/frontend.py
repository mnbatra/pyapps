from tkinter import *
import backend

window=Tk()
window.wm_title("Library App 1.0")

def view_command():
    c1.delete(0,END)
    [c1.insert(END,item) for item in backend.view()]

def search_command():
    c1.delete(0,END)
    for item in backend.search(a2_value.get(),a4_value.get(),b2_value.get(),b4_value.get()):
        c1.insert(END,item)

def add_command():
    c1.delete(0,END)
    backend.insert(a2_value.get(),a4_value.get(),b2_value.get(),b4_value.get())
    c1.insert(END,(a2_value.get(),a4_value.get(),b2_value.get(),b4_value.get()))

def del_command():
    backend.delete(selected_item[0])
    c1.delete(0,END)
    [c1.insert(END,item) for item in backend.view()]

def update_command():
    backend.update(a2_value.get(),a4_value.get(),b2_value.get(),b4_value.get(),selected_item[0])
    c1.delete(0,END)
    [c1.insert(END,item) for item in backend.view()]


def get_selected_row(event):
    try:
        global selected_item
        index=c1.curselection()[0]
        selected_item=c1.get(index)
        a2.delete(0,END)
        a2.insert(0,selected_item[1])
        a4.delete(0,END)
        a4.insert(0,selected_item[2])
        b2.delete(0,END)
        b2.insert(0,selected_item[3])
        b4.delete(0,END)
        b4.insert(0,selected_item[4])
    except IndexError:
        pass

a1=Label(window,text="Title")
a1.grid(row=0,column=0)

a2_value=StringVar()
a2=Entry(window,width=8,textvariable=a2_value)
a2.grid(row=0,column=1)

a3=Label(window,text="Author")
a3.grid(row=0,column=2)

a4_value=StringVar()
a4=Entry(window,width=8,textvariable=a4_value)
a4.grid(row=0,column=3)

b1=Label(window,text="Year")
b1.grid(row=1,column=0)

b2_value=StringVar()
b2=Entry(window,width=8,textvariable=b2_value)
b2.grid(row=1,column=1)

b3=Label(window,text="ISBN")
b3.grid(row=1,column=2)

b4_value=StringVar()
b4=Entry(window,width=8,textvariable=b4_value)
b4.grid(row=1,column=3)

c=Scrollbar(window)
c.grid(row=2,column=2,rowspan=6)

c1=Listbox(window, height=6, width=30)
c1.grid(row=2,column=0,rowspan=6, columnspan=2)
c1.bind('<<ListboxSelect>>',get_selected_row)

c1.configure(yscrollcommand=c.set)
c.configure(command=c1.yview)

c2=Button(window,text="View All",width=10,command=view_command)
c2.grid(row=2,column=3)

d1=Button(window,text="Search Entry",width=10,command=search_command)
d1.grid(row=3,column=3)

e1=Button(window,text="Add Entry",width=10,command=add_command)
e1.grid(row=4,column=3)

f1=Button(window,text="Update",width=10,command=update_command)
f1.grid(row=5,column=3)

g1=Button(window,text="Delete",width=10,command=del_command)
g1.grid(row=6,column=3)

h1=Button(window,text="Close",width=10,command=window.destroy)
h1.grid(row=7,column=3)

window.mainloop()
