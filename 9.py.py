from tkinter import*
root=Tk()
root.title("Simple Interest")
root.geometry("500x300")

def calculate():
    prin=int(principalentry.get())
    rat=int(rateentry.get())
    tim=int(timeentry.get())
    amount=(prin*rat*tim)/100
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)

principal=Label(root,text="Prinicpal:",font="arial 15").place(x=50,y=20)

time=Label(root,text="Time:",font="arial 15").place(x=50,y=90)
rate=Label(root,text="Rate:",font="arial 15").place(x=50,y=160)

interest=Label(root,text="Interest:",font="arial 15")
interest.place(x=50,y=20)

principalvalue=StringVar()
timevalue=StringVar()
ratevalue=StringVar()
principalentry=Entry(root,textvariable=principalvalue,font="arial 20",width=8)
timeentry=Entry(root,textvariable=timevalue,font="arial 20",width=8)
rateentry=Entry(root,textvariable=ratevalue,font="arial 20",width=8)

principalentry.place(x=200,y=20)
timeentry.place(x=200,y=160)
rateentry.place(x=200,y=90)

Button(text="Calculate",font="arial 15",command=calculate).place(x=350,y=20)
Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=90)


root.mainloop()