from tkinter import *
window=Tk()

def conv2():
    grams=float(a2_value.get())*1000
    pounds=float(a2_value.get())*2.20462
    ounces=float(a2_value.get())*35.274
    b1.delete("1.0",END)
    b1.insert(END,str(grams) +" grams")
    b2.delete("1.0",END)
    b2.insert(END,str(pounds) + " lbs")
    b3.delete("1.0",END)
    b3.insert(END,str(ounces) + " oz")

a1=Label(window,text="     KG    ",fg="black",bg="white")
a1.grid(row=0,column=0)

a2_value=StringVar()
a2=Entry(window,textvariable=a2_value)
a2.grid(row=0,column=1)

a3=Button(window,text="Convert", height=0,width=8, command=conv2)
a3.grid(row=0,column=2)

b1=Text(window,height=1,width=20)
b1.grid(row=1,column=0)

b2=Text(window,height=1,width=20)
b2.grid(row=1,column=1)

b3=Text(window,height=1,width=20)
b3.grid(row=1,column=2)


window.mainloop()
