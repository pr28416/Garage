from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

maxTries = 6
words = []

print(bcolors.OKGREEN + 'hello' + bcolors.ENDC)

with open('five_letter_words.txt') as f:
    for line in f:
        words.append(line.strip("\n"))

word = words[randint(0, len(words)-1)]
while len(set(word)) != 5: word = words[randint(0, len(words)-1)]
print('debug:', word)

t = 0
while t < maxTries:
    guess = input("Enter 5-letter word, all lowercase: ")
    if len(guess) != 5 or any([not ('a' <= c <= 'z') for c in guess]):
        print("Invalid input.")
        continue
    output = ""
    for c in range(len(guess)):
        if guess[c] == word[c]:
            output += bcolors.OKGREEN
        elif guess[c] in word:
            output += bcolors.WARNING
        else:
            output += bcolors.ENDC
        output += guess[c]
    output += bcolors.ENDC
    print(output)
    if word == guess:
        print("You guessed the word correctly!")
        break
    t += 1
else:
    print("You didn't guess the word correctly! It was", word)