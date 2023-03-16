import random

vowels = ["a", "e", "u", "i", "y", "o"]
consonants = ["z", "r", "t", "p", "q" ,"s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
nameLength = int(input("Please enter a number"))
name = []

for i in range(nameLength // 2):
    name.append(consonants[random.randint(0, len(consonants) - 1)] + vowels[random.randint(0, len(vowels) - 1)])
    finalName = "".join(name)
print(finalName)

