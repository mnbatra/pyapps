from tkinter import *
from backend import Database

class LibApp:
    def __init__(self):
        self.database=Database("books.db")
        self.window=Tk()
        self.window.wm_title("Library App 1.0")

        self.a1=Label(self.window,text="Title")
        self.a1.grid(row=0,column=0)

        self.a2_value=StringVar()
        self.a2=Entry(self.window,width=8,textvariable=self.a2_value)
        self.a2.grid(row=0,column=1)

        self.a3=Label(self.window,text="Author")
        self.a3.grid(row=0,column=2)

        self.a4_value=StringVar()
        self.a4=Entry(self.window,width=8,textvariable=self.a4_value)
        self.a4.grid(row=0,column=3)

        self.b1=Label(self.window,text="Year")
        self.b1.grid(row=1,column=0)

        self.b2_value=StringVar()
        self.b2=Entry(self.window,width=8,textvariable=self.b2_value)
        self.b2.grid(row=1,column=1)

        self.b3=Label(self.window,text="ISBN")
        self.b3.grid(row=1,column=2)

        self.b4_value=StringVar()
        self.b4=Entry(self.window,width=8,textvariable=self.b4_value)
        self.b4.grid(row=1,column=3)

        self.c=Scrollbar(self.window)
        self.c.grid(row=2,column=2,rowspan=6)

        self.c1=Listbox(self.window, height=6, width=30)
        self.c1.grid(row=2,column=0,rowspan=6, columnspan=2)
        self.c1.bind('<<ListboxSelect>>',self.get_selected_row)

        self.c1.configure(yscrollcommand=self.c.set)
        self.c.configure(command=self.c1.yview)

        self.c2=Button(self.window,text="View All",width=10,command=self.view_command)
        self.c2.grid(row=2,column=3)

        self.d1=Button(self.window,text="Search Entry",width=10,command=self.search_command)
        self.d1.grid(row=3,column=3)

        self.e1=Button(self.window,text="Add Entry",width=10,command=self.add_command)
        self.e1.grid(row=4,column=3)

        self.f1=Button(self.window,text="Update",width=10,command=self.update_command)
        self.f1.grid(row=5,column=3)

        self.g1=Button(self.window,text="Delete",width=10,command=self.del_command)
        self.g1.grid(row=6,column=3)

        self.h1=Button(self.window,text="Close",width=10,command=self.window.destroy)
        self.h1.grid(row=7,column=3)

        self.window.mainloop()

    def view_command(self):
        self.c1.delete(0,END)
        [self.c1.insert(END,item) for item in self.database.view()]

    def search_command(self):
        self.c1.delete(0,END)
        for item in self.database.search(self.a2_value.get(),self.a4_value.get(),self.b2_value.get(),self.b4_value.get()):
            self.c1.insert(END,item)

    def add_command(self):
        self.c1.delete(0,END)
        self.database.insert(self.a2_value.get(),self.a4_value.get(),self.b2_value.get(),self.b4_value.get())
        self.c1.insert(END,(self.a2_value.get(),self.a4_value.get(),self.b2_value.get(),self.b4_value.get()))

    def del_command(self):
        self.database.delete(selected_item[0])
        self.c1.delete(0,END)
        [self.c1.insert(END,item) for item in self.database.view()]

    def update_command(self):
        self.database.update(self.a2_value.get(),self.a4_value.get(),self.b2_value.get(),self.b4_value.get(),selected_item[0])
        self.c1.delete(0,END)
        [self.c1.insert(END,item) for item in self.database.view()]


    def get_selected_row(self,event):
        try:
            global selected_item
            index=self.c1.curselection()[0]
            selected_item=self.c1.get(index)
            self.a2.delete(0,END)
            self.a2.insert(0,selected_item[1])
            self.a4.delete(0,END)
            self.a4.insert(0,selected_item[2])
            self.b2.delete(0,END)
            self.b2.insert(0,selected_item[3])
            self.b4.delete(0,END)
            self.b4.insert(0,selected_item[4])
        except IndexError:
            pass
