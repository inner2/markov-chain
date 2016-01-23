# Markov 連鎖

## 環境
MAC OS X EI Caption

## python version
python 3.5.0

## SQLite version
3.8.10.2

## データベースの作成
SQLite のデータベースを作成する。  
(table と column を作成する)  
一度作成すればいい。  

```
$ python make_db.py
```

## 辞書の作成
Mecab によって分割した文字列を SQLite のデータベースに登録
mecab_div フォルダで作成した text.csv を使う

```
$ python make_dic.py
```

## 辞書をもとに文章を作成

```
$ python markov.py
```
