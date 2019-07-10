# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#查看当前目录的绝对路径
curpath=os.path.abspath(".")
print(curpath)
#首先把新目录的完整路径表示出来
#os.path.join(path,'1')
#创建一个新目录
#f=curpath.join('1')
#b=os.path.exists(f)
# print(b,f)
# if not b:
#     os.mkdir(f)
#os.mkdir(path.join('2'))
#os.rmdir(path.join("1"))

dir1=["01-项目资料","02-开发提交","03-用例设计","04-测试过程","05-版本发布","06-版本总结"]
dir2=["01-对比结果","02-杀毒报告","03-审计报告","04-执行数据","05-自动化报告","06-质量分析","07-其他资料"]
dir3=["01-发布文档","02-升级包及安装文件"]
#s=(''.join('%s' % '01-项目资料')).encode('gbk')
i=0
while i<len(dir1):
    if not os.path.exists(curpath+'\\'+dir1[i]):
        os.mkdir(curpath+'\\'+dir1[i])
    i=i+1
i=0
subdir=''
while i<len(dir2):
    subdir=curpath+'\\'+dir1[3]+'\\'+dir2[i]
    print(subdir)
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    i=i+1
i=0
while i<len(dir3):
    subdir=curpath+'\\'+dir1[4]+'\\'+dir3[i]
    print(subdir)
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    i=i+1


