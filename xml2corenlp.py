from bs4 import BeautifulSoup, Tag
import os, sys
import fileinput

f1 = open("output_training.txt", "a")
sentence = []
train_sentence = []

doc = []
with open ("corpus.xml", "r") as f:
    for line in f:
        #sentence.append(line)
        soup = BeautifulSoup(line)
        for word in soup.find_all('w'):
                if word['pos'] == "PM":
                    train_sentence.append(word.getText().encode('utf-8') + "\t"+ "LABEL")
                else:
                    train_sentence.append(word.getText().encode('utf-8')+"\t"+"0")

        if "</sentence>" in line:
            doc.append("\n".join(train_sentence) + "\n")
            train_sentence = []

        print "length of doc"
        print len(doc)
        if len(doc) == 500:
            f1.write("".join(doc))
            doc = []

f1.write("".join(doc))
f1.close()
