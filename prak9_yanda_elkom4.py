# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:47:26 2021

@author: Yanda Puspita Sari
"""
print("----- ELKOM 4 -----")

a = ["abc","fgh","cac","21090"]
print("List string: ", a)

count = 0
for x in a:
	if x[:1] == x[-1:]:
		print("- ", x)
		count += 1
        
print(f"Terdapat {count} string yang memenuhi kriteria")