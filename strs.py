#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# split分隔符  encoding='utf-8' 解决中文乱码问题
f = open('name.txt', encoding='utf-8')
data = f.read()
print(data.split('|'))
f.close()

# strip分隔符
f2 = open('name1.txt', encoding='utf-8')
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1
f2.close()
