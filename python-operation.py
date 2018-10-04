#!/usr/bin/env python
# conding: utf-8

# print('Hello World')

import os
import sys
import pdb

def chk_tmp_permission():
    
    chk_write = os.access('/tmp', os.W_OK)

    if chk_write == True:
        print('OK. You have Write Permisson')
        # pass
    else:
        print('NO, You do not have Write Permisson')
        sys.exit(0)

def chk_vb_command():
    import subprocess
    
    paths = [ "/usr/bin/", "/usr/local/bin/" ]

    for path in paths: 
        vb_cmd = path + 'VBoxManage'
        if os.path.isfile(vb_cmd) == True:
            # print('OK')
            # print(vb_cmd)
            break    # After this, vb_cmd exists in reality.
        else:
            print('Maybe, You do not install Virtualbox ( We could not find ' + vb_cmd + ' )')
    else:
        print('You do not install Virtualbox. Bye!')
        sys.exit(0)
    # print(vb_cmd)
    return vb_cmd

def exe_vm():
    cmd = chk_vb_command()
    print(cmd)    

    import subprocess
   
    # try:
    #   # res = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE)
    #   res = subprocess.run(["vb_cmd", "list", "vms"], stdout=subprocess.PIPE)
    #   sys.stdout.buffer.write(res.stdout)
    # except:
    #   print('Error')

if __name__ == '__main__':

    # Confirm whether you have write permission for /tmp
    chk_tmp_permission()

    # Check if VBoxManage is installed
    # chk_vb_command()

    # 
    # pdb.set_trace()
    exe_vm()


    # test
    print('END')
