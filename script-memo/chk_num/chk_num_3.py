#!/usr/bin/env python
# coding='utf-8'


# x = '123456'
x = 123456

# print(x)
# print('int:', isinstance(x, int))
# print('float:', isinstance(x, float))

chk_num = isinstance(x, int)

if chk_num == True:
  print('OK')
else:
  print('NG')  
