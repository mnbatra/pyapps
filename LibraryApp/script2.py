from tkinter import *
import backend
import sqlite3
window=Tk()

def create_table():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert_value(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library VALUES("?,?,?,?,?")" ,(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library")
    rows=cur.fetchall()
    conn.close()
    return rows

def del_value(isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library WHERE isbn = %s",(item,))
    conn.commit()
    conn.close()

def update(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET title=%s,author=%s,year=%s  WHERE item=%s",(title,author,year,isbn))
    conn.commit()
    conn.close()

def ins_list():
    c1.insert()

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

c1=Listbox(window, height=6, width=30, xscrollcommand=c)
c1.grid(row=2,column=0,rowspan=6, columnspan=2)

c2=Button(window,text="View All",width=10,command='')
c2.grid(row=2,column=3)

d1=Button(window,text="Search Entry",width=10,command='')
d1.grid(row=3,column=3)

e1=Button(window,text="Add Entry",width=10,command='')
e1.grid(row=4,column=3)

f1=Button(window,text="Update",width=10,command='')
f1.grid(row=5,column=3)

g1=Button(window,text="Delete",width=10,command='')
g1.grid(row=6,column=3)

h1=Button(window,text="Close",width=10,command=window.destroy)
h1.grid(row=7,column=3)

window.mainloop()
