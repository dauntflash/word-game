
import os
import random
from termcolor import colored
i=1
j=0


rules='''
Before we begin, here are the rules;
1. The computer generates a random word and you have to guess it letter by letter to the last one.
2. Only letters are allowed as inputs. (No numeric or special characters.)
3. Only one letter input is allowed.

Enjoy, 
'''


def clear_screen(): #THIS CAN ONLY BE USED ON WINDOWS MACHINES, FOR OTHER OS CHECK ALTERNATIVES
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

#HERE WE DECLARE A FUNCTION THAT'S STORING WHAT TO BE STORED WHEN THE PROGRAM BEGINS RUNNING
def welcome_page():
    print(colored("*" * 50, 'blue'))
    print(colored("    HELLO, WELCOME TO DAUNTCITY WORD GAME.",'green'))
    print(colored("*" * 50, 'blue'))

welcome_page()


print(colored(rules,'green'))
filepath='C:\\Users\\PC\\Documents\\Munene\\Python' #THE PATH TO THE FILE CONTAINIG THE WORD LIST
file_path=(os.path.join(filepath,"Oxford 5000.txt")) #COMBINING THE PATH WITH THE FILE NAME, YOU CAN CHANGE THE FILE ANME TO THE NAME OF YOUR FILE

try:
    with open(file_path,'r') as file:
        content=file.read()
        words=content.split()
except FileNotFoundError:
    print("Sorry the file Oxford 5000.txt not foud")

list_length=len(words)

#WE DECLARE A FUNCTION THAT GIVES US A RANDOM NUMBER BETWEEN 0 AND THE LIST LENGTH(THE NUMBER OF WORDS IN THE FILE)
def limits():
    upper_limit=list_length-1
    random_word_number=random.randint(0,upper_limit)
    return random_word_number


word_number=limits() #THE RANDOM NUMBER GENERATED ABOVE IS STORED IN THIS VARIABLE
initial_word=words[word_number] #WE NOW STORE THE WORD IN THE INDEX ABOVE IN THIS VARIABLE
word=initial_word.lower() #THE SAME WORD IS STORED HERE BUT NOW IN LOWERCASE
length=len(word)-1
guessed_word=""
word_progress="Word progress:"+" _"*len(word)
print(colored(word_progress,'yellow'))
first=input("\nEnter the first letter of the word: ")
remaining_blank=length

while True:
    first_length=len(first)
    if first.lower()==word[0]:
        guessed_word+=first


        word_progress="\n"+"Word progress: "+guessed_word+" _"*remaining_blank
        print(colored(word_progress, 'yellow'))


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
                print("\n\n","*"*5,"GAME OVER","*"*5,"\n\n")
                break
            if i < length:
                remaining_blank-=1
                i += 1
                guessed_word+=guess

                word_progress="\n"+"Word progress: "+guessed_word+" _"*remaining_blank
                print(colored(word_progress, 'yellow'))

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


