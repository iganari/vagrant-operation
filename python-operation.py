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
    
    chk_vb_script = os.path.isfile('/usr/bin/VBoxManage')
    vb_script_ubuntu = '/usr/bin/VBoxManage'
    vb_script_macos  = '/usr/local/bin/VboxManage'
    paths = [ "/usr/bin/", "/usr/local/bin/" ]

    for path in paths: 
        print(path, 'VBoxManage')

        # if chk_vb_script == True:
        #     pass
        # else:
        #     print('Maybe, You do not install Virtualbox (Not lock up VBoxManage !)')
        #     sys.exit(0)

if __name__ == '__main__':

    # /tmpに書き込み権限があるか確認する
    chk_tmp_permission()

    # VirtualBoxがインストールしてあるか確認する
    # 具体的には '/usr/bin/VBoxManage' が存在することを確認する
    chk_vbscript()




    # test
    print('END')
