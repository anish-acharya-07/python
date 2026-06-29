import random

# scraping words form words.txt file

file = open("word_guessing_game/words.txt","r")

data = file.read()

file.close()

words = data.split("\n")

clean_word = []

for word in words :
    word = word.strip()

    if word != (""):
        clean_word.append(word)


print()