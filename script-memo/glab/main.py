#!/usr/bin/env python
# coding: utf-8

import glob


# カレントディレクトリのディレクトリ、ファイルを表示する
print(glob.glob("./*"))


# テキストファイルのみを取得する(カレントディレクトリのみ)
print(glob.glob('./*.txt'))
print(glob.glob("./*.txt"))


# 再帰的にサブディレクトリを検索する

print(glob.glob("./**", recursive=True))
print(glob.glob('./**', recursive=True))
print(glob.glob('./**.txt', recursive=True))
print(glob.glob("./**.txt", recursive=True))


# HOME配下の `Vagrantfile` を検索してみる
print(glob.glob('/home/igarashi/**Vagrantfile'))
