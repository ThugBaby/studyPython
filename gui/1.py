import tkinter as tk

windows=tk.Tk()
windows.title('my window')
windows.geometry('400x400')
e=tk.Entry(windows,show=None)
e.pack()

def generate_dir():
   b1.config(text='正在生成...',state='disable')

b1=tk.Button(windows,text="开始",width=15,
             height=2,command=generate_dir)
b1.pack()

windows.mainloop()

