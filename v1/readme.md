# Python マルコフ連鎖を利用して文章を生成する。

## 環境
MAC OS X EI Caption

## python version
python 3.5.0

## SQLite version
3.8.10.2

## 形態素解析で文章を単語に分ける
- 形態素解析には Mecab を利用
- python2 系で作成
    - python3 で作成したかったが、Mecab のバインディングがうまくいなかった
- mecab_div/readme.md を参照

## マルコフ連鎖を利用して文章を作成する。
- python3 系で作成

### データベースの作成
SQLite のデータベースを作成する。  
(table と column を作成する)  
一度作成すればいい。  

```
$ python make_db.py
```

### 辞書の作成
Mecab によって分割した文字列を SQLite のデータベースに登録
mecab_div フォルダで作成した text.csv を使う

```
$ python make_dic.py
```

### 辞書をもとに文章を作成

```
$ python markov.py
```
