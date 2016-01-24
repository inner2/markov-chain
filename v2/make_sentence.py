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
    w1 = list1[0][0]
    w2 = list1[0][1]
    sentence += w1 + w2

    for i in range(20):
        try:
            c.execute("select * from stocks where word1 = '" + w1 + "' and word2 = '" + w2 + "' order by random() limit 1")
            list2 = c.fetchall()
            w1, w2 = w2, list2[0][2]
            sentence += list2[0][2]
            # print(i, list2)

        except:
            # print("error")
            break
    return sentence


# Main
if __name__ == "__main__":
    # read_csv()
    result = create_sentence()
    print(result)
    conn.close()
