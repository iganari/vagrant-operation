#!/usr/bin/env python
# conding: utf-8

# print('Hello World')

### /tmpに書き込み権限があるか確認する

def chk_tmp_permission():
    import os
    
    chk_write = os.access('/opt', os.W_OK)

    if chk_write == True:
        print('OK. You have Write Permisson')
    else:
        print('NO, You do not have Write Permisson')


if __name__ == '__main__':
    chk_tmp_permission()
