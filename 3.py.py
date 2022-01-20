from tkinter import *
from tkinter import messagebox

def reset_entry():
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')
    BMI.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    BMI.insert(10,bmi)

root = Tk()
root.title('BMI CALCULATOR')
root.geometry('400x350')
root.resizable(0,0)
root.config(bg='blue')

var = IntVar()
weightvalue=StringVar()
heightvalue=StringVar()
resultvalue=StringVar()



frame=LabelFrame(root,width=350,height=300,text='BMI CALCULATOR', bg="powder blue",relief=RAISED,font="Times 16 bold")
frame.place(x=30,y=20)

height_lb = Label(frame,text="Enter Height (cm)  ",font="Times 11 italic",bg="powder blue")
height_lb.place(x=50 ,y=60)

weight_lb = Label(frame,text="Enter Weight (kg)  ",font="Times 11 italic",bg="powder blue")
weight_lb.place(x=50 ,y=120)

result_label= Label(frame,text='Result',font="Times 11 italic",bg="powder blue")
result_label.place(x=50 ,y=160)


height_tf = Entry(frame, textvariable=heightvalue)
height_tf.place(x=180 ,y=60)

weight_tf = Entry(frame,textvariable=weightvalue)
weight_tf.place(x=180 ,y=120)

BMI = Entry(frame,textvariable=resultvalue)
BMI.place(x=180 ,y=160)


cal_btn = Button(frame,text='Calculate',command=calculate_bmi,font="Times 11 italic",bg="powder blue")
cal_btn.place(x=30,y=220)

reset_btn = Button(frame,text='Reset',command=reset_entry,font="Times 11 italic",bg="powder blue")
reset_btn.place(x=120,y=220)

exit_btn = Button(frame,text='Exit',command=lambda:root.destroy(),font="Times 11 italic",bg="powder blue")
exit_btn.place(x=210,y=220)

root.mainloop()
