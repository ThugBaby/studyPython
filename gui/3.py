import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected ' + var.get())

r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()

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


window.mainloop()