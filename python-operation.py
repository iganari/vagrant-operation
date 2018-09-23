#!/usr/bin/env python
# conding: utf-8

# print('Hello World')

import os


def chk_tmp_permission():
    
    chk_write = os.access('/opt', os.W_OK)

    if chk_write == True:
        print('OK. You have Write Permisson')
        # pass
    else:
        print('NO, You do not have Write Permisson')
        sys.exit(0)

def chk_vbscript():
    import sys
    
    paths = [ "/usr/bin/", "/usr/local/bin/" ]

    for path in paths: 
        vm_path = path + 'VBoxManage'
        # print(vm_path)
        if vm_path == True:
            break
        else:
            print('Maybe, You do not install Virtualbox ( We could not find ' + vm_path + ' )')
    else:
        print('You do not install Virtualbox. Bye!')
        sys.exit(0)

if __name__ == '__main__':

    # Confirm whether you have write permission for /tmp
    chk_tmp_permission()

    # Check if VBoxManage is installed
    chk_vbscript()




    # test
    print('END')
