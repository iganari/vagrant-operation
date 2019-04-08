#!/bin/env python
# conding: utf-8

#
# vb command
#

import os
import sys
# import pdb
# import argparse
import subprocess


def parse_opts():
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument(
        '-c',
        '--check',
        type=str,
        help='WIP: check VM List.',
    )

    return parser.parse_args()


# VBoxManage コマンドの有無を確認する関数
def chk_vb_command():

    """
    ローカルにVirtualBoxのCLIがインストールしてあるか確認する
    """

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
def exe_vm_all(vc_path):

    """
    ローカルマシンに存在するVMのリストを作成
    """

    vms_name_all_list = []

    try:
        res = subprocess.run([vc_path, "list", "vms"],
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
        print('外部プログラムの実行に失敗しました [' + vc_path + ']', file=sys.stderr)

    # 配列をソートする
    vms_name_all_list = sorted(vms_name_all_list)

    # 配列の確認
    # print(vms_name_all_list)

    return vms_name_all_list


# 現在起動しているVMの表示名を取得する(vms_name_running_list)
def exe_vm_running(vc_path):

    """
    現在、ローカルマシン上で起動状態のVMのリストを作成
    """

    vms_name_running_list = []

    try:
        res = subprocess.run([vc_path, "list", "runningvms"],
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
        print('外部プログラムの実行に失敗しました [' + vc_path + ']', file=sys.stderr)

    # 配列をソートする
    vms_name_running_list = sorted(vms_name_running_list)

    # 配列の確認
    # print(vms_name_running_list)

    return vms_name_running_list


# 配列の比較
def chk_list_diff(vname_all, vname_rng):

    """
    (存在するVM) - (起動中VM) をすることで、これか起動出来るVMのリストを作成
    """

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
def print_list(vc_path, vname_all, vname_rng, vname_dif):

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
        fnc_start(vname_all, vname_rng, vname_dif, vc_path)
    elif ans == 2:
        fnc_stop(vname_all, vname_rng, vname_dif, vc_path)
    elif ans == 3:
        fnc_search(vname_all, vname_rng, vname_dif)
    elif ans == 9:
        print('OK! See You!!')
        sys.exit(0)
    else:
        print('Error. Invalid input vale: {}'.format(ans))
        sys.exit(1)


# inputによる入力と数値チェック
def input_num():

    """
    数字チェック
    """

    i = input('>> ')

    chk_num = i.isdecimal()

    if chk_num is True:
        # print('OK')
        input_number = int(i)
        pass
    else:
        print('入力された値が数値でありません')
        sys.exit(1)

    return input_number


# startの関数
def fnc_start(vname_all, vname_rng, vname_dif, vc_path):

    """
    VMの起動関数
    """

    print('\n---------------------------')
    print('    [ DIFFERENCE  VM ]    |')
    print('---------------------------')

    if vname_dif == []:
        print('*** ' + 'not Diff VMs' + ' ***')
    else:
        for index in range(len(vname_dif)):
            print(' ' + str(index + 1) + ' : ' + vname_dif[index])

    # ユーザの入力
    start_ans = input_num()
    print('your input : ', start_ans)
    # 修正
    start_ans = start_ans - 1

    if start_ans > len(vname_dif) - 1:
        print('入力した数値が大きすぎます')
    else:
        # 入力された数値に対応するvnameを代入
        start_vname = vname_dif[start_ans]

        # print('len(hairetu): ', len(vame_dif))
        # print('start_vname', start_vname)

        # vnameを元にVirtualBoxをヘッドレスモードで起動する

        print('Start Virtualbox is ' + str(start_vname))
        try:
            res = subprocess.run([vc_path, "startvm", start_vname, "-type", "vrdp"],
                                 check=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)

            # 標準出力としてターミナルに出力する
            # sys.stdout.buffer.write(res.stdout)

        except subprocess.CalledProcessError:
            print('外部プログラムの実行に失敗しました [' + vc_path + ']', file=sys.stderr)


# stopの関数
def fnc_stop(vname_all, vname_rng, vname_dif, vc_path):

    """
    VMの停止関数
    """

    print('\n---------------------------')
    print('    [   Running VM   ]    |')
    print('---------------------------')

    if vname_rng == []:
        print('*** ' + 'not Running VMs' + ' ***')
    else:
        for index in range(len(vname_rng)):
            print(' ' + str(index + 1) + ' : ' + vname_rng[index])

    # ユーザの入力
    stop_ans = input_num()
    print('your input : ', stop_ans)
    # 修正
    stop_ans = stop_ans - 1

    if stop_ans > len(vname_rng) - 1:
        print('入力した数値が大きすぎます')
    else:
        # 入力された数値に対応するvnameを代入
        stop_vname = vname_rng[stop_ans]

        # vnameを元にVirtualBoxを停止させる
        print('Stop Virtualbox is ' + str(stop_vname))
        try:
            res = subprocess.run([vc_path, "controlvm", stop_vname, "poweroff"],
                                 check=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)

        except subprocess.CalledProcessError:
            print('外部プログラムの実行に失敗しました [' + vc_path + ']', file=sys.stderr)


# searchの関数
def fnc_search(vname_all, vname_rng, vname_dif):

    """
    VMの探索関数
    """

    print('\n---------------------------')
    print('      [   ALL VM   ]      |')
    print('---------------------------')

    if vname_all == []:
        print('*** ' + 'not VMs' + ' ***')
    else:
        for index in range(len(vname_all)):
            print(' ' + str(index + 1) + ' : ' + vname_all[index])

    # ユーザの入力
    search_ans = input_num()
    print('your input : ', search_ans)
    # 修正
    search_ans = search_ans - 1

    if search_ans > len(vname_all) - 1:
        print('入力した数値が大きすぎます')
    else:
        # 入力された数値に対応するvnameを代入
        search_vname = vname_all[search_ans]

        print(search_vname)

        vag_files = []
        # 環境変数から$HOMEを入れる
        HOME_PATH = os.environ["HOME"]

        print(HOME_PATH)

        # os.walkによる 'Vagrantfile' の検索
        for root, dirs, files in os.walk(HOME_PATH):
            for filename in files:
                if filename == 'Vagrantfile' and root.find('.vagrant.d') is -1:
                    vag_files.append(os.path.join(root, filename))
                else:
                    pass

        if vag_files == []:
            print('あなたが探しているVagrantfileは存在しません.')
            sys.exit(0)

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

    vc_path = chk_vb_command()

    vname_all = exe_vm_all(vc_path)
    vname_rng = exe_vm_running(vc_path)
    vname_dif = chk_list_diff(vname_all, vname_rng)

    # メイン処理
    print_list(vc_path, vname_all, vname_rng, vname_dif)


if __name__ == '__main__':
    main()
