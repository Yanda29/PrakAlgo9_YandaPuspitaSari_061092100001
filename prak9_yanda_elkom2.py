# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:28:38 2021

@author: Yanda Puspita Sari
"""
print('tuple 1: ')
a=('102','322', '345', '240', '300','450')
b = ", ".join(a[0:3])
c = ", ".join(a[4:7])
d= ", ".join(a[8:11])
print((b,c,d))
print('rata rata dari tuple adalah: ')
print ([sum(map(float, filter(None, a[0:3])))/(len(a)-1),(sum(map(float, filter(None, a[4:7])))/(len(a)-1)),(sum(map(float, filter(None, a[8:11])))/(len(a)-1))])  
