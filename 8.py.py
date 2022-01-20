from tkinter import *
#declaration of root
root=Tk()
root.geometry("1020x1040")

a=Label(root, text="Principal:")
a.place(x=30,y=50)
e1=Entry(root)
e1.place(x=100,y=50)
b=Label(root, text="Rate")
b.place(x=30,y=90)
e2=Entry(root)
e2.place(x=100,y=90)
c=Label(root, text="Time")
c.place(x=30,y=130)
e3=Entry(root)
e3.place(x=100,y=130)

def click():
    x=int(e1.get())
    y=int(e2.get())
    z=int(e3.get())
    si=(x)/100
    l1=Label(root, text=("The simple interest is:",si))
    l1.place(x=240,y=290)

b1=Button(root, text="Calculate", command=click)
b1.place(x=240,y=250)

root.mainloop()