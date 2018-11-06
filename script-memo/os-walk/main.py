#!/usr/bin/env python
# coding: utf-8

import os

# 配列の作成
found = []
found2 = []


   # for root, dirs, files in os.walk("/test_dir/"):
   # for root, dirs, files in os.walk("/tmp/"):
# for root, dirs, files in os.walk("./"):
#     for filename in files:
#         found.append(os.path.join(root, filename))   # ファイルのみ再帰でいい場合はここまででOK
#     for dirname in dirs:
#         found.append(os.path.join(root, dirname))    # サブディレクトリまでリストに含めたい場合はこれも書く
# print(found)

for root, dirs, files in os.walk("./"):
    for filename in files:
        # print(filename)
        if filename == 'Vagrantfile':
            found.append(os.path.join(root, filename))   # ファイルのみ再帰でいい場合はここまででOK

    # for dirname in dirs:
    #     found.append(os.path.join(root, dirname))    # サブディレクトリまでリストに含めたい場合はこれも書く

# # 配列の確認
# print(found)



# 環境変数の確認
print(os.environ["HOME"])
MY_PATH = os.environ["HOME"]

# os.walkによるファイル検索
for root, dirs, files in os.walk(MY_PATH):
    for filename in files:
        if filename == 'Vagrantfile' and root.find('.vagrant.d') is -1:
            found2.append(os.path.join(root, filename))
print(found2)


# 探したいワード
srh_word = 'hogehoge'

for files in found2:
    # print(files) # 一個ずつ
    with open(files, encoding='utf-8') as f:
        for row in f:
            # print(row)
            if not row.find(srh_word) is -1:
                print(row)
                print('This file is ', files)
