# VirtualBox Operation

[![CircleCI](https://circleci.com/gh/iganari/circleci-test.svg?style=svg)](https://circleci.com/gh/iganari/circleci-test)


+ [Bash版](https://github.com/iganari/virtualbox-operation/blob/master/readme.md#bash版について)
+ [Python版](https://github.com/iganari/virtualbox-operation/blob/master/readme.md#python版について)

## 出来ること・出来ないこと

### 出来ること :blush:

+ start
    + ローカル内のVMの起動(ヘッドレス)
+ stop
    + ローカル内のVMの一時停止
+ search
    + ローカル内の指定したVMのVagrantfileの探しだし

### 出来ないこと :cry:

+ 上記以外
    + VirtualBoxやVagrantとうまくやって行きたいので、敢えて出来ることを絞っています


## Bash版について

### 使い方

+ clone

```
git clone https://github.com/iganari/vagrant-operation.git
cd vagrant-operation
```

+ 実行テスト

```
bash bash-operation.sh
```

+ 端末の `~/.bashrc` に記載する

```diff
+ alias vb='bash ${vagrant-operaionのPATH}/bash-operaion.sh'
```

+ `~/.bashec` の再読み込み

```
source ~/.bashrc
```

## Python版について

+ 使用出来ますがリファクタリング中です :building_construction:
+ Python 3.x でのみ想定しています

### 使い方

+ clone

```
git clone https://github.com/iganari/vagrant-operation.git
cd vagrant-operation
```

+ 実行テスト

```
python3 python-operation.py
```

+ 端末の `~/.bashrc` に記載する

```diff
+ alias vb='python3 ${vagrant-operaionのPATH}/python-operaion.py'
```

+ `~/.bashec` の再読み込み

```
source ~/.bashrc
```

### オプション

+ help

```
python3 python-operation.py -h
```
```
### 例

$ python3 python-operation.py -h

Description: Manage commands for VirtualBox.

    Usage: $ vb [ options ]

  Options:

      -h : show this help message and exit
```


### Python版の開発方法

+ 仮想環境の有効化

```
python3 -m venv .vb
source .vb/bin/activate
pip install -r package.txt
```

+ flake8によるコードレビュー

```
flake8 python-operation.py --show-source
```

+ 仮想環境の無効化

```
deactivate
```

# 現状のイケてないとこ :no_good:

+ Golang版が無い
    + issue化 [:memo:](https://github.com/iganari/virtualbox-operation/issues/7)
+ Virtualbox/Vagrantがそもそもインストールしているかの判定が入っていない
    + ゆくゆく実装予定
        + issue化 [:memo:](https://github.com/iganari/virtualbox-operation/issues/3)
