# Vagrant Operation

:warning: WIP :warning:

## 使い方

+ clone

```
git clone https://github.com/iganari/vagrant-operation.git
cd vagrant-operation
```

+ 実行テスト

```
sh operation.sh
```

## 現状のイケてないとこ :no_good:

+ shellでしか意図する挙動をしない
    + ---> Python3で書き直す :snake:
+ Vagrantがそもそもインストールしているかの判定が入っていない
    + ゆくゆく実装予定 ---> issueにしておく

## [リファクタ中] Python Versionについて

### :warning: 注意

+ Python 3.x でのみ動作確認しています

### 使い方

```
cd virtualbox-operation
source .vb/bin/activate
```
