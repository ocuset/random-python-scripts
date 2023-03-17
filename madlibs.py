from random import choice

list_of_words = []
for i in range(int(input("Please enter the number of words you want to play with: "))):
    list_of_words.append(input("Please enter some words for the 'madlibs': "))

text = input("Please enter a text with some blanks (identified by ___) in it: ")

while "___" in text:
    text = text.replace("___", choice(list_of_words), 1)

print(text)