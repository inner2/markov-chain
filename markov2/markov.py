# python3
# import module
import sqlite3

# Connect database
conn = sqlite3.connect('markov.db')
c = conn.cursor()


# create sentence
def create_sentence():
    sentence = ""
    c.execute("select * from stocks order by random() limit 1")
    list1 = c.fetchall()
    # print(list1)
    w1 = list1[0][1]

    for i in range(20):
        c.execute("select * from stocks where word1 = '%s' order by random() limit 1" % w1)
        list1 = c.fetchall()
        w1 = list1[0][1]
        sentence += w1
        # print(i, list1)
    print(sentence)


# Main
if __name__ == "__main__":
    # read_csv()
    create_sentence()
    conn.close()
