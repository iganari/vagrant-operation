#!/usr/bin/env python
# coding: utf-8

from pathlib import Path


# pathオブジェクトを生成
p = Path('.')

print(p.iterdir())

list(p.glab('**/*.*'))


# 
# # test_01直下のファイルとディレクトリを取得
# # Path.glob(patteern)はジェネレータを返す
# # 結果を明示するためlist化しているが、普段は不要
# list(p.glab("*"))
# 
# # ファイル名の条件検索
# list(p.glab("*.txt"))
# 
# # 再帰的な検索
# list(p.glab("**/*"))
