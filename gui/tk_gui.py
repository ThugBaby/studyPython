# /usr/bin/ env python3
# -*-coding:utf-8-*-
import tkinter as tk
windows=tk.Tk()
windows.title("my windows")
windows.geometry("500x500")
var=tk.StringVar()
l=tk.Label(windows,textvariable=var,bg='green',font=('Arial',12),width=15,
           height=2)
on_hit=False
l.pack()
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set("")
b=tk.Button(windows,text='hit me',width=15,height=2,command=hit_me)
b.pack()
windows.mainloop()
