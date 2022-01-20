from tkinter import *
 
def calculate():
 
  if valRadio.get() == 1:
    res = (int(e1.get()) ) ** 3 #volume of cube
  elif valRadio.get() == 2:
    res = int(e1.get()) * int(e2.get()) *int(e3.get()) #volume of cuboid
  else:
    res ="check radio button"
  myText.set(res)
 
 
root =Tk()
root.title("volume of cube and cuboid")     # Add a title
root.configure(bg="powder blue")
root.maxsize(width=350, height=380)
root.minsize(width=350, height=380)
 
valRadio =IntVar()
myText=StringVar()
e1 =StringVar()
e2 =StringVar()
e3 =StringVar()
 
l=LabelFrame(root,text="CUBE AND CUBOID VOLUME CALCULATOR",width=480,height=480,bd=10,padx=50,pady=30)
l.grid(row=0,columnspan=6,padx=20,pady=20)
l2=Label(l, text="Length :" ).grid(row=1,column = 0,pady=15)
l3=Label(l, text="Width :").grid(row=2,column=0,pady=15)
l4=Label(l, text="height :").grid(row=3,column=0,pady=15)
result=Label(l,text="(result)", textvariable=myText).grid(row=6,column=0,pady=15)
 
r1 =Radiobutton(l,text="Volcube",variable=valRadio, value=1).grid(row=4, column=0)
r2 =Radiobutton(l,text="Volcuboid",variable=valRadio, value=2).grid(row=4, column=1)
 
ea=Entry(l,textvariable = e1).grid(row=1, column=1)
eb=Entry(l,textvariable = e2).grid(row=2, column=1)
ec=Entry(l,textvariable = e3).grid(row=3, column=1)
 
b =Button(l,text="Calculate", command=calculate,width=15).grid(row=5, columnspan=2)
 
root.mainloop()