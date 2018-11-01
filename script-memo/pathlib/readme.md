# os.walk

## ディレクトリ配下のファイルの内容を調査したい

## 参考資料

https://qiita.com/amowwee/items/e63b3610ea750f7dba1b

+ 手軽にやるならglob.glob
+ サブディレクトリまで走査するなら、python 3.4以前ならos.walk、python 3.5以降ならglob.glob
+ python 3.4以降で、その後のファイル操作まで考えるなら、pathlibがお勧め


## pathlib

https://docs.python.jp/3/library/pathlib.html

+ python 3.4以降ではpathlibモジュールが標準ライブラリに追加されました


出来なさそう…
素直に、os.pathを使う
