# Python マルコフ連鎖を利用して文章を生成する
version 2

- 連鎖数を 3 に変更
- 文章生成時にたまに発生するエラーを修正
- シェルスクリプトで mecab 利用する部分を python 3 に書き換えた

## 環境

- Mac OS X EI Caption
- python 3
- sqlite3

## 使い方

### 1. データベースの作成
SQLite3 でデータベースを作成する
```
$ python make_db.py
```

### 2. 形態素解析で文章を単語に分ける

- 形態素解析には Mecab を利用
- Mecab の利用する部分はシェルスクリプトを使用

```
$ chmod u+x do_mecab.sh
$ python make_markov_chain.py
```

### 3. 登録したデータを利用して文章を作成する。

```
$ python make_sentence.py
```
