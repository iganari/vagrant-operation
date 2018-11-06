#!/bin/env python
# conding: utf-8

# 
# vb command
#

import os
import sys
# import pdb

# Usage
usage = """
Description: Manage commands for VirtualBox.

    Usage: $ vb [ options ]

  Options:

      -h : show this help message and exit

"""

# 引数の取得
def get_args():

    # 返り値の定義
    options = "" # 個々の引数
    subject = ""

    try:
        for arg in sys.argv:
            if arg.rstrip().startswith("-"):
                options = options + arg.replace("-", "")
        subject = " ".join(sys.argv).split("]")[1]

    except IndexError:
        pass

    return options, subject


# /tmp の書き込み権限をチェックする
def chk_tmp_permission():

    chk_write = os.access('/tmp', os.W_OK)

    if chk_write is True:
        print('OK. You have Write Permisson')
        # pass
    else:
        print('NO, You do not have Write Permisson')
        sys.exit(0)


# VBoxManage コマンドの有無を確認する関数
def chk_vb_command():
    import subprocess

    paths = ["/usr/bin/", "/usr/local/bin/"]

    for path in paths: 
        vb_cmd = path + 'VBoxManage'
        if os.path.isfile(vb_cmd) is True:
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

# 実在するVMの表示名を取得する(vms_name_all_list)
def exe_vm_all():

    cmd = chk_vb_command()
    # print('Check all VMs')

    import subprocess

    vms_name_all_list = []

    try:
        res = subprocess.run([cmd, "list", "vms"],
                             check=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)

        # 標準出力としてターミナルに出力する
        # sys.stdout.buffer.write(res.stdout)

        # 一行ずつ取り出して、処理したい
        for line in res.stdout.splitlines():
            # すべての表示
            # print(line)

            # " で区切って配列形式
            # print(line.split('"'))

            # " で区切って配列形式の2個目 = VM name
            vms_name_all = line.split('"')[1]
            # print(vms_name_all)

            # 配列に追加する
            vms_name_all_list.append(vms_name_all)

    except subprocess.CalledProcessError:
        print('外部プログラムの実行に失敗しました [' + cmd + ']', file=sys.stderr)

    # 配列をソートする
    vms_name_all_list = sorted(vms_name_all_list)

    # 配列の確認
    # print(vms_name_all_list)

    return vms_name_all_list


# 現在起動しているVMの表示名を取得する(vms_name_running_list)
def exe_vm_running():

    cmd = chk_vb_command()
    # print('Check runnint VMs')

    import subprocess

    vms_name_running_list = []

    try:
        res = subprocess.run([cmd, "list", "runningvms"],
                             check=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)

        # 標準出力としてターミナルに出力する
        # sys.stdout.buffer.write(res.stdout)

        # 一行ずつ取り出して、処理したい
        for line in res.stdout.splitlines():
            # すべての表示
            # print(line)

            # " で区切って配列形式
            # print(line.split('"'))

            # " で区切って配列形式の2個目 = VM name
            vms_name_running = line.split('"')[1]
            # print(vms_name_all)

            # 配列に追加する
            vms_name_running_list.append(vms_name_running)

    except subprocess.CalledProcessError:
        print('外部プログラムの実行に失敗しました [' + cmd + ']', file=sys.stderr)

    # 配列をソートする
    vms_name_running_list = sorted(vms_name_running_list)

    # 配列の確認
    # print(vms_name_running_list)

    return vms_name_running_list

# 配列の比較
def chk_list_diff():

    # 関数の呼び出し
    vname_all = exe_vm_all()
    vname_rng = exe_vm_running()

    # 集合(set)にして差分を確認
    vname_dif = set(vname_all) - set(vname_rng)

    # 差分のsetをsetのまま表示する
    # print(vname_dif)

    # setを配列(list)に直す
    vname_dif = list(vname_dif)
    # print(vname_dif)

    # 出来た配列をソートする
    vname_dif = sorted(vname_dif)
    # print(vname_dif)

    return vname_dif

# VirtualBoxのリスト表示
def print_list():

    vname_all = exe_vm_all()
    vname_rng = exe_vm_running()
    vname_dif = chk_list_diff()

    print('\n\n### Virtual Box List ###')
    print('\n---------------------------')
    print('      [   ALL VM   ]      |')     
    print('---------------------------')


    if vname_all == []:
        print('*** ' + 'not Making VMs' + ' ***')
    else:
        for index in range(len(vname_all)):
            print('    ' + vname_all[index])

    # print('\n\n## Virtual Box List ##\n')
    print('\n---------------------------')
    print('    [   Running VM   ]    |')     
    print('---------------------------')

    if vname_rng == []:
        print('*** ' + 'not Running VMs' + ' ***')
    else:
        for index in range(len(vname_rng)):
            print('    ' + vname_rng[index])

    # print('\n\n## Virtual Box List ##\n')
    print('\n---------------------------')
    print('    [ DIFFERENCE  VM ]    |')     
    print('---------------------------')

    if vname_dif == []:
        print('*** ' + 'not Diff VMs' + ' ***')
    else:
        for index in range(len(vname_dif)):
            print('    ' + vname_dif[index])


    print('\n\n### choose NUMBER of operation VM behave ###\n')
    print(' 1 : start')
    print(' 2 : stop')
    print(' 3 : search')
    print(' 9 : exit')


    # ユーザの入力
    ans = input_num()
    # print(ans)
    print('input: ', ans)

    if ans == 1:
        fnc_start()    
    elif ans ==2: 
        fnc_stop()    
    elif ans ==3: 
        fnc_search()
    elif ans ==9: 
        print('OK! See You!!')
        sys.exit(0)
    else:
        print('Error')
        sys.exit(1)


# inputによる入力と数値チェック
def input_num():

    i = input('>> ')

    chk_num = i.isdecimal()

    if chk_num == True:
        # print('OK')
        input_number = int(i)
        pass
    else:
        print('入力された値が数値でありません')
        sys.exit(1)

    return input_number


# startの関数
def fnc_start():

    import subprocess

    vname_all = exe_vm_all()
    vname_rng = exe_vm_running()
    vname_dif = chk_list_diff()

    print('\n---------------------------')
    print('    [ DIFFERENCE  VM ]    |')     
    print('---------------------------')

    if vname_dif == []:
        print('*** ' + 'not Diff VMs' + ' ***')
    else:
        for index in range(len(vname_dif)):
            print('    ' + str(index) + '    ' + vname_dif[index])


    # ユーザの入力
    start_ans = input_num()
    print('input: ', start_ans)

    if start_ans > len(vname_dif) - 1:
        print('入力した数値が大きすぎます')
    else:
        # print('input: ', start_ans)
        cmd = chk_vb_command()

        # print(vname_dif)

        # 入力された数値に対応するvnameを代入
        start_vname = vname_dif[start_ans]

        # print('len(hairetu): ', len(vame_dif))
        # print('start_vname', start_vname)

        # vnameを元にVirtualBoxをヘッドレスモードで起動する

        print('Start Virtualbox is ' + str(start_vname))
        try:
            res = subprocess.run([cmd, "startvm", start_vname, "-type", "vrdp"],
                                 check=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)

            # 標準出力としてターミナルに出力する
            # sys.stdout.buffer.write(res.stdout)

        except subprocess.CalledProcessError:
            print('外部プログラムの実行に失敗しました [' + cmd + ']', file=sys.stderr)


# stopの関数
def fnc_stop():

    import subprocess

    vname_all = exe_vm_all()
    vname_rng = exe_vm_running()
    vname_dif = chk_list_diff()

    print('\n---------------------------')
    print('    [   Running VM   ]    |')     
    print('---------------------------')

    if vname_rng == []:
        print('*** ' + 'not Running VMs' + ' ***')
    else:
        for index in range(len(vname_rng)):
            print('    ' + str(index) + '    ' + vname_rng[index])


    # ユーザの入力
    stop_ans = input_num()
    print('input: ', stop_ans)

    if stop_ans > len(vname_rng) - 1:
        print('入力した数値が大きすぎます')
    else:
        cmd = chk_vb_command()

        # 入力された数値に対応するvnameを代入
        stop_vname = vname_rng[stop_ans]

        # vnameを元にVirtualBoxを停止させる
        print('Stop Virtualbox is ' + str(stop_vname))
        try:
            res = subprocess.run([cmd, "controlvm", stop_vname, "poweroff"],
                                 check=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)

        except subprocess.CalledProcessError:
            print('外部プログラムの実行に失敗しました [' + cmd + ']', file=sys.stderr)



# searchの関数
def fnc_search():

    import subprocess

    vname_all = exe_vm_all()
    vname_rng = exe_vm_running()
    vname_dif = chk_list_diff()

    print('\n---------------------------')
    print('      [   ALL VM   ]      |')     
    print('---------------------------')

    if vname_rng == []:
        print('*** ' + 'not VMs' + ' ***')
    else:
        for index in range(len(vname_all)):
            print('    ' + str(index) + '    ' + vname_all[index])


    # ユーザの入力G
    search_ans = input_num()
    print('input: ', search_ans)

    if search_ans > len(vname_all) - 1:
        print('入力した数値が大きすぎます')
    else:
        cmd = chk_vb_command()

        # 入力された数値に対応するvnameを代入
        search_vname = vname_all[search_ans]


        print(search_vname)


        vag_files = []
        # 環境変数から$HOMEを入れる
        HOME_PATH = os.environ["HOME"]

        # os.walkによる 'Vagrantfile' の検索
        for root, dirs, files in os.walk(HOME_PATH):
            for filename in files:
                if filename == 'Vagrantfile' and root.find('.vagrant.d') is -1:
                    vag_files.append(os.path.join(root, filename))
                else:
                    print('Vagrantfileが存在しません.')


        # print(vag_files)
                
        srh_word = search_vname

        for files in vag_files:
            with open(files, encoding='utf-8') as f:
                # print(files)
                for row in f:
                    # print(row)
                    if not row.find(srh_word) is -1:
                        print('This file name is ', files)
                        


# main
def main():

    # 出力値
    output = ""

    # get_args関数の引出し
    options, subject = get_args()

    print('options is ', options)
    print('subject is ', subject)


    # 引数が `-h` だった場合
    if "h" in options:
        print(usage)
        # print('OK')
        sys.exit(0)

    # Confirm whether you have write permission for /tmp
    chk_tmp_permission()

    # メイン処理
    print_list()

    print(output)


if __name__ == '__main__':
    main()
