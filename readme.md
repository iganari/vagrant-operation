# Vagrant Operation

+ [BASH版]
+ [Python版]

## BASH版の使い方

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

+ `.bashec` の再読み込み

```
source ~/.bashrc
```

## 現状のイケてないとこ :no_good:

+ BASH版しか無い
    + ---> Python3でも作成中 :snake:
+ Vagrantがそもそもインストールしているかの判定が入っていない
    + ゆくゆく実装予定 ---> issueにしておく

## [リファクタ中] Python Versionについて

### :warning: 注意

+ Python 3.x でのみ想定しています

### 使い方

```
cd virtualbox-operation
python3 -m venv .vb
source .vb/bin/activate
```


## 出来ること・出来ないこと

### 出来ること

+ start
    + ローカル内のVMの起動(ヘッドレス)
+ stop
    + ローカル内のVMの一時停止
+ search
    + ローカル内の指定したVMのVagrantfileの探しだし

### 出来ないこと

+ 上記以外
    + :warning: VirtualBoxやVagrantとうまくやって行きたいので、敢えて権限・出来ることを絞っています
