# python3
# import module
import sqlite3

# Connect database
conn = sqlite3.connect('markov.db')
c = conn.cursor()


# read csv file
def make_dic():
    # read csv file
    f = open("text.csv", "r")
    src = f.read()
    word_list = src.split(",")

    # insert data
    w1 = ""
    w2 = ""
    for word in word_list:
        if w1 and w2:
            c.execute("insert into stocks values(?, ?)" , (w1, w2))
            # print("insert data", w1, w2)
        w1, w2 = w2, word
    conn.commit()


# Main
if __name__ == "__main__":
    make_dic()
    conn.close()
