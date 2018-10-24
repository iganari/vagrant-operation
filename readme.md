# Virtualbox Operation

+ [Bash版](https://github.com/iganari/virtualbox-operation/blob/master/readme.md#bash版について)
+ [Python版]

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
    + :warning: VirtualBoxやVagrantとうまくやって行きたいので、敢えて出来ることを絞っています


## Bash版について

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

### :warning: 注意

+ 作成中です :bow:
+ Python 3.x でのみ想定しています

### 使い方

```
cd virtualbox-operation
python3 -m venv .vb
source .vb/bin/activate
```

# 現状のイケてないとこ :no_good:

+ Bash版しか無い
    + Python3
        + 作成中 :snake:
    + Golang
        + issue化 :memo:
+ Virtualbox/Vagrantがそもそもインストールしているかの判定が入っていない
    + ゆくゆく実装予定
        + issue化 :memo:
