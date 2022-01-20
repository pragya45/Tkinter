from tkinter import *
PI=3.14
def button_click():
    r=float(entry1.get())
    area=PI*r*r
    entry3.insert(10,area)

root=Tk()
root.geometry("644x434")
root.title('Area of circle')
root.configure(bg="light pink")
entry1=StringVar
entry2=StringVar


l=Label(root, text='Calculator to find area of circle',bd=25,relief=SUNKEN,bg="powder blue",font="comicsansms 14 bold")
l.place(x=200,y=0)

#Declaring label for base and height in root
radius_label1=Label(root, text='Enter radius',font=('Verdans',16))
radius_label1.place(x=150,y=100)
area_circle_label=Label(root, text='Area of circle is',font=('Verdans',16))
area_circle_label.place(x=150,y=300)



#creating entry box in root
entry1=Entry(root, font=('Verdans',14), width=12)
entry1.place(x=350,y=100)
entry3=Entry(root, font=('Verdans',14), width=12)
entry3.place(x=350,y=300)


#button to calculate
calc_button=Button(root,text='Calculate',bd=20,fg="blue",bg="powder blue",command=button_click).place(x=300,y=200)

root.mainloop()
