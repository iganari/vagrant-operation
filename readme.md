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
python3 -m venv .vb
source .vb/bin/activate
```


## 出来ること・出来ないこと

### 出来ること

+ ローカル内のVMの起動(ヘッドレス)
+ ローカル内のVMの一時停止
+ ローカル内の指定したVMのVagrantfileの探しだし

### 出来ないこと

+ 上記以外

VirtualBoxやVagrantとうまくやって行きたいので、敢えて権限・出来ることを絞っています
