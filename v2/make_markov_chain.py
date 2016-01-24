# python3
# input module
import subprocess
import sqlite3

# split word
word_split = '''
'''

# Connect database
conn = sqlite3.connect('markov.db')
c = conn.cursor()


# make markov chain
def make_markov():
    # read sourcefile text.txt
    filename = 'text.txt'
    src = open(filename, 'r').read()

    src_list = src.split(word_split)

    # mecab による形態素解析
    for sentence in src_list:

        # run command
        result = subprocess.getoutput('./do_mecab.sh ' + sentence)
        # print(result)

        word_list = result.split(' ')
        word_list.remove('')  # 不要なデータの削除

        w1 = ''
        w2 = ''
        for word in word_list:
            if w1 and w2:
                c.execute("insert into stocks values(?, ?, ?)", (w1, w2, word))
                # print("insert data", w1, w2, word)
            w1, w2 = w2, word

    # save database
    conn.commit()


# create database table
def create_table():
    c.execute("create table stocks(word1, word2, word3")


# Main
if __name__ == "__main__":
    make_markov()
    conn.close()
