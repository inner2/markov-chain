# 参考ページなど

## mecab を実行
[コマンドでmecabを実行](http://logic.moo.jp/data/archives/322.html)

```
$ chmod u+x hello.sh
```

## コマンドの実行
[python3 - subprocess](http://docs.python.jp/3.5/library/subprocess.html)
[Pythonでコマンドの実行結果の標準出力を取得する](http://te2u.hatenablog.jp/entry/2015/07/15/235240)
[pythonでコマンド実行するには](http://takuya-1st.hatenablog.jp/entry/2014/08/23/022031)

```
cmd = 'ls -l'
result = subprocess.getoutput(cmd)
print(result)
```


## コマンドラインの読み取り
input_read.py
```
# input
import sys
aaa = sys.stdin.readline()
print(aaa)
```
