import tkinter as tk

windows=tk.Tk()
windows.title('my window')
windows.geometry('200x200')
e=tk.Entry(windows,show=None)
e.pack()

def insert_point():
    var=e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
    t.insert('end',var)

b1=tk.Button(windows,text="insert point",width=15,
             height=2,command=insert_end)
b1.pack()
b2=tk.Button(windows,text='insert end',command=insert_end)
b2.pack()
t=tk.Text(windows,height=2)
t.pack()


windows.mainloop()

