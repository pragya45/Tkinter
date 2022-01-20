from tkinter import *

def button_click():
    base=float(entry1.get())
    height=float(entry2.get())
    area=1/2 * base * height
    entry3.insert(10,area)

root=Tk()
root.geometry("644x434")
root.title('Area of triangle and circle')
root.configure(bg="light pink")
entry1=StringVar
entry2=StringVar


l=Label(root, text='Calculator to find area of triangle',bd=25,relief=SUNKEN,bg="powder blue",font="comicsansms 14 bold")
l.place(x=200,y=0)

#Declaring label for base and height in root
base_label1=Label(root, text='Enter base',font=('Verdans',16))
base_label1.place(x=150,y=100)
height_label1=Label(root, text='Enter height',font=('Verdans',16))
height_label1.place(x=150,y=150)
area_triangle_label=Label(root, text='Area of triangle is',font=('Verdans',16))
area_triangle_label.place(x=150,y=300)



#creating entry box in root
entry1=Entry(root, font=('Verdans',14), width=12)
entry1.place(x=350,y=100)
entry2=Entry(root, font=('Verdans',14), width=12)
entry2.place(x=350,y=150)
entry3=Entry(root, font=('Verdans',14), width=12)
entry3.place(x=350,y=300)


#button to calculate
calc_button=Button(root,text='Calculate',bd=20,fg="blue",bg="powder blue",command=button_click).place(x=300,y=200)

root.mainloop()
