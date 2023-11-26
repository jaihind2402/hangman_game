from hangman_words import word_list
from hangman_arts import stages, logo
#TODO-11: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
index = random.randrange(len(word_list))
chosen_word = word_list[index]
# print(f'random word chosen by the computer is {chosen_word}')

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word_length = len(chosen_word)
#TODO-8: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
condition = False
display = []
for i in range(word_length):
    display.append('_')
index_i = 0
print(logo)
temp = ''
while not condition:    
    guess = str(input('Guess a letter: ')).lower()
    if temp == guess:
        print(f'You have already guessed the letter, {temp}\n')
    # print("You have ")
    for position in range(word_length):
        letter = chosen_word[position]
        #TODO-9: - If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."
         #Join all the elements in the list and turn it into a String.
        # 
        if letter == guess:
            # print("you entered letter is in the word! ")
            display[position] = letter
        # else:
        #     print("")

            # for i in range(len(stages)):
        #     print("Wrong")
    print(f"{' '.join(display)}\n")
    # print(f"the display word is {display}")
    if guess not in chosen_word:
        lives = lives -1
        print(f"{guess} letter is not in the word \n")
        print(stages[lives])

    if '_'  not in display:
        condition = True
        print('You Won\n')
    if lives == 0:
        print('You Lose \n')
        condition = True
    temp +=guess
    #TODO-10: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        
        # break
    # else:
    #     guess
    # index_i+=1
# print(f"condition:  {condition}")

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-12: - If the user has entered a letter they've already guessed, print the letter and let them know.
