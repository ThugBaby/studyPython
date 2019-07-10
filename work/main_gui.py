# /usr/bin/ env python3
# -*-coding:utf-8-*-
from sub_thread import *
import tkinter as tk
import tkinter.messagebox
windows=tk.Tk()
tk_string=tk.StringVar()
windowWidth = windows.winfo_reqwidth()
windowHeight = windows.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(windows.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(windows.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
windows.geometry("+{}+{}".format(positionRight, positionDown))

windows.title('生成工具')
windows.geometry('450x150')
l = tk.Label(windows, width=100, text="请在下方输入定制ftp地址",font="MicrosoftYahei")
e=tk.Entry(windows,show=None,width=300,bd=3.5,textvariable=tk_string)
e.place(x=0,y=35)
l.pack()
len_address=0
def run():
    #tk.messagebox.showinfo(message=ftp_address.get())
    e.config(state='disable')
    b1.config(text='正在生成...', state='disable')
def success():
    windows.destroy()
def generate_dir():
    t1 = MyThread(q,tk_string.get())
    t1.start()
    t1.join()
    while True:
        if not q.empty():
            if q.get()=='end':
                break
    print("耗时%d秒" % (datetime.now() - start_time).seconds)
    b1.config(text='完成', state='disable')

    r = tk.messagebox.showinfo(title='success', message='生成成功')
    if r:
        success()
ui_thread = threading.Thread(target=run)
main_thread = threading.Thread(target=generate_dir)
def change_state():
    len_address = len(tk_string.get())
    if len_address == 0:
        tk.messagebox.showinfo(message='请输入地址！')
    else:
        ui_thread.start()
        main_thread.start()
b1=tk.Button(windows,text="开始",width=10,height=2,command=change_state)
b1.place(x=170,y=85)

windows.mainloop()



