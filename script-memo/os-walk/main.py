#!/usr/bin/env python
# coding: utf-8

import os

# 配列の作成
found = []

# 探したいワード
srh_word = hogehoge

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

# 配列の確認
print(found)


