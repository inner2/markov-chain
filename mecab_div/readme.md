# MeCab を利用して形態素解析を行う

## 環境
MAC OS X EI Caption

## python version
python 2.7.10

## MeCab version
mecab of 0.996

## Mecab install
Homebrew を利用してインストール

```
$ brew install mecab
$ brew install mecab-ipadic
```

## 準備
辞書を作るために文章を入れた text.txt ファイルを準備する。

## 内容
text.txt ファイルの文章を mecab により分割し、
text.csv ファイルに保存する。

### 実行
```
$ python mecab_div.py
```
