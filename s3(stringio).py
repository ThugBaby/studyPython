# /usr/bin/ env python3
# -*-coding:utf-8-*_
from io import StringIO
f=StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print(f.getvalue())

f=StringIO("hello world")
while True:
    s=f.readline()
    if s=="":
        break
    print(s.strip())
     #strip()默认去除首尾\n或空格

from io import BytesIO
f=BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())

f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode("utf-8"))


