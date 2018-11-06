#!/usr/bin/env python
# coding: utf-8

print('Plz tell me Number that You Want to Check ')

i = input('>> ')

print('Your Input is ', i)

# print('isdeimal:', i.isdecimal()) 

chk_num = i.isdecimal()

if chk_num == True:
  print('This is OK')
else:
  print('This is NG')  
