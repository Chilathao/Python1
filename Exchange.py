from tkinter import *
import tkinter.messagebox as Msg
def B2K():
    chBath=bath.get()
    chRate=rate.get()
    if bath.get()=='':
        Msg.showinfo("Infor","Enter bath please!...",icon='warning')
        txt1.focus_set()
    elif rate.get()=='':
        Msg.showinfo("Infor", "Enter rate please!...", icon='warning')
        txt2.focus_set()
    elif chBath.isalpha():
        Msg.showinfo("Infor", "Enter bath is number only please!...", icon='warning')
        txt1.focus_set()
    elif chRate.isalpha():
        Msg.showinfo("Infor", "Enter rate is number only please!...", icon='warning')
        txt2.focus_set()
    else:
        b = int(bath.get())
        r = int(rate.get())
        k = b * r
        kip.set(f'{k:,} kip')
def ALLClear():
    bath.set('')
    rate.set('')
    kip.set('')
    txt1.focus()

root = Tk()
root.title('Hello Python')
root.geometry('500x400')
bath=StringVar()
rate=StringVar()
kip=StringVar()

lb1 = Label(root, font=('Times New Roman', 16),text='Bath to Kip')
lb1.place(x=200,y=10)

lb2 = Label(root, font=('Times New Roman', 16),text='Enter Bath')
lb2.place(x=50,y=50)
txt1=Entry(root, font=('Times New Roman', 16),textvariable=bath)
txt1.place(x=150,y=50)

lb3 = Label(root, font=('Times New Roman', 16),text='Enter Rate')
lb3.place(x=50,y=100)
txt2=Entry(root, font=('Times New Roman', 16),textvariable=rate)
txt2.place(x=150,y=100)

btn1=Button(root,font=('Times New Roman', 16),width=10,text='Exchange',command=B2K)
btn1.place(x=120, y= 150)
btn3=Button(root,font=('Times New Roman', 16),width=10,text='Clear',command=ALLClear)
btn3.place(x=280, y= 150)

lb4 = Label(root, font=('Times New Roman', 16),text='Total :')
lb4.place(x=50,y=200)
txt3=Entry(root, font=('Times New Roman', 16),textvariable=kip)
txt3.place(x=150,y=200)

root.mainloop()