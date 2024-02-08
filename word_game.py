
import os
import random
i=1
j=0

filepath='C:\\Users\\PC\\Documents\\Munene\\Python'
file_path=os.path.join(filepath,"Oxford 5000.txt")
with open(file_path,'r') as file:
    content=file.read()
    words=content.split()

list_length=len(words)

def limits():
    upper_limit=list_length-1
    random_word_number=random.randint(0,upper_limit)
    return random_word_number

word_number=limits()
initial_word=words[word_number]
word=initial_word.lower()
length=len(word)-1

guessed_word=""
first=input("\nEnter the first letter of the word: ")
while True:
    first_length=len(first)
    if first.lower()==word[0]:
        guessed_word+=first

        print("\nWord progress:",guessed_word)
        guess=input("Correct, enter the next letter: ")
        break
    elif not first.isalpha():
        first=input("Invalid option, only letters allowed. Try again: ").lower()
        j+=1
    elif first_length != 1:
        first=input("Invalid option, only one letter allowed. Try again: ").lower()
        j+=1
    else:
        first=input("Wrong, try again: ")
        j+=1
while i <= length:
    guess_length=len(guess)
    if guess.isalpha() and guess_length==1:
        if guess.lower()==word[i]:
            if i==length:
                print("\nYou got it, the word is",initial_word,"with a total of",j,"guessses.")
                break
            if i < length:
                i += 1
                guessed_word+=guess

                print("\nWord progress:",guessed_word)
                if i == length:
                    guess=input("Enter the last letter: ")
                else:
                    guess=input("Correct, enter the next letter: ")

        else:
            guess=input("You are wrong try again: ")
            j+=1
    elif not guess.isalpha():
        guess=input("Invalid option, only letters allowed. Try again: ")
        j+=1
    else:
        guess=input("Invalid option, only one letter allowed. Try again: ")
        j+=1
