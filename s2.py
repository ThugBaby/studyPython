# !/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    f=open("test.txt","r",encoding='utf-8')
    str=f.read()
    print(str)
except IOError as e:
    print("except:",e)
finally:
    if f:
        f.close()
#使用with自动调用close()方法
with open("test.txt","r",encoding="utf-8") as f:
    print(f.read())
#read(size)读取指定大小，readline(读取一行)，readlines()读取所有行返回List

with open("test.txt","a",encoding="utf-8") as f:
    f.write("test")




