fin = open("C:\\Users\PC2\Documents\PRG105\words.txt")
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word

