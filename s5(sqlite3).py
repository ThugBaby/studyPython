# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import sqlite3
conn=sqlite3.connect("test.db")
cusor=conn.cursor()
#cusor.execute("create table user (id varchar(20) primary key,name varchar(20))")
cusor.execute("insert into user(id,name) values(\'1\',\'Michael\')")
print(cusor.rowcount)
cusor.close()
conn.commit()
conn.close()

conn=sqlite3.connect()