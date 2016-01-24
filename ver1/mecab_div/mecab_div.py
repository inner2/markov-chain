#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2
import MeCab


# MeCab
def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result


# Main
if __name__ == "__main__":
    filename = "text.txt"
    src = open(filename, "r").read()
    # print src
    word_list = wakati(src)

    f = open("text.csv", "w")
    word2 = ""
    for word in word_list:
        word2 = word2 + word + ","

    # print word2
    f.write(word2)
    f.close()
