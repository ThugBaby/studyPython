import threading
from datetime import datetime
from queue import Queue
import time
q = Queue()
start_time=datetime.now()
class MyThread(threading.Thread):
    def __init__(self,q,ftp_address):
        threading.Thread.__init__(self)
        self.q = q
        self.ftp_address=ftp_address
    def run(self):
        start_time=datetime.now()
        #此处开始处理,
        print(self.ftp_address)
        a = "\sdafsd\dfasdf防守打法\fsdf\12312\sdasf\为"
        print(repr(a))
        #time.sleep(2)
        self.q.put("end")

