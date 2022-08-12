from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import webbrowser
import time 
def btnclick(number):
  global val
  val=val + str(number)
  data.set(val)
def btnclear():
  global val
  val=" "
  data.set(" ")
def btnequal():
  global val
  sub=str(eval(val))
  data.set(sub)
def haggu():
  webbrowser.open("https://wing2rah.blogspot.com/?m=1")
  time.sleep(3)
  messagebox.showinfo("FROM RAHUL...."," THANK U...hope u enjoy it..")
def cancel():
    ansx=messagebox.askyesno("rahul","do you want to exit")
    if ansx:
        rahul.destroy()
def info():
     messagebox.showinfo("rahul","this is rahul's calculator")
    
     ans=messagebox.askyesno("rahul","do u want more ?")
     if ans:
         naam=simpledialog.askstring("rahul","what is your name?")
         messagebox.showinfo("rahul",naam + "   please go to my blog")
         messagebox.showinfo("rahul","press rahul to go to my blog")

rahul=Tk()
rahul.title("welcome to calculator")
rahul.geometry("30x15+50+30")
rahul["bg"]="#98FF98"
val=" "
data=StringVar()
display=Entry(rahul,textvariable=data , justify="center", bg="cyan",bd=10,font=("windsong",16))

display.grid(row=0 , columnspan=3)

btn7=Button(rahul,text="7",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(7),activebackground="#C2DFFF")
btn7.grid(row=1, column=0)
btn8=Button(rahul,text="8",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(8),activebackground="#F433FF")
btn8.grid(row=1, column=1)
btn9=Button(rahul,text="9",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(9),activebackground="#6960EC")
btn9.grid(row=1, column=2)
btn4=Button(rahul,text="4",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(4),activebackground="#E42217")
btn4.grid(row=2, column=0)
btn5=Button(rahul,text="5",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(5),activebackground="#E238EC")
btn5.grid(row=2, column=1)
btn6=Button(rahul,text="6",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(6),activebackground="#A74AC7")
btn6.grid(row=2, column=2)
btn1=Button(rahul,text="1",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(1),activebackground="#93FFE8")
btn1.grid(row=3, column=0)
btn2=Button(rahul,text="2",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(2),activebackground="#52D017")
btn2.grid(row=3, column=1)
btn3=Button(rahul,text="3",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(3),activebackground="#F63C8A")
btn3.grid(row=3, column=2)
btnzero=Button(rahul,text="0",bg="light yellow",font=("ariel",10,"bold"),bd=8,height=2,width=3,command=lambda:btnclick(0),activebackground="#C12267")
btnzero.grid(row=4 , column=1)
btnmin=Button(rahul,text="-",bg="magenta",font=("ariel",10,"bold"),bd=15,height=2,width=3,command=lambda:btnclick('-'),activebackground="#E4287C")
btnmin.grid(row=5 , column=1)
btnsum=Button(rahul,text="+",bg="magenta",font=("ariel",10,"bold"),bd=15,height=2,width=3,command=lambda:btnclick('+'),activebackground="#FD0017")
btnsum.grid(row=6 , column=0)
btneql=Button(rahul,text="EQUAL",bg="light green",font=("ariel",10,"bold"),bd=20,height=3,width=5,command=btnequal,activebackground="#FCDFFF")
btneql.grid(row=6 , column=1)
btnmul=Button(rahul,text="*",bg="magenta",font=("ariel",10,"bold"),bd=15,height=2,width=3,command=lambda:btnclick('*'),activebackground="#48CCCD")
btnmul.grid(row=6 , column=2)
btndiv=Button(rahul,text="÷",bg="magenta",font=("ariel",10,"bold"),bd=15,height=2,width=3,command=lambda:btnclick('/'),activebackground="#A74AC7")
btndiv.grid(row=7 , column=1)
btnp=Button(rahul,text="Rahul...",font=("ariel",10,"bold"),bg="#FFFF00",fg="blue",activebackground="#0020C2",borderwidth=5,bd=5,width=15,height=1,command=haggu)
btnp.grid(row=11, column=1)
btnc=Button(rahul,text="clear",fg="purple",bg="cyan",font=("ariel",12,"bold"),bd=25,height=3,width=5,command=btnclear,activebackground="red")
btnc.grid(row=10, column=1)
btni=Button(rahul,text="?",fg="purple",bg="yellow",height=1,width=1,bd=15,activebackground="cyan",command=info)
btni.grid(row=10,column=0)
btnx=Button(rahul,text="X",fg="purple",bg="yellow",height=1,width=1,bd=15,activebackground="cyan",command=cancel)
btnx.grid(row=10,column=2)
rahul.mainloop()
