#importing libraries
import random
from HangmanWords import word_list
from HangmanArt import logo, stages

print()
print()
#randomly chossing a word from the list and assigning it to the var chosen word

chosen_word = random.choice(word_list)
lives = 6
word_length = len(chosen_word)
end_of_game = False
print('Welcome to George\'s Hanman Game')

print(logo)
print()
print()
#creating a list of dashes that signify the missing alphabets

blank = []
for a in range(word_length):
    blank+='_'
print(blank)
print()
print(f'chosen word = {chosen_word}\n')

#Implementing repeatability to 2 previous loops-- makng the user guess again till the word is exhausted: implemented using while loop in line 28 
while not end_of_game:
    ## user taking a guess
    user_guess = input('Guess a letter')
    print()
    #checking that the position of each dash matches with that of a chosen word and replacing the corresponding dash

    if user_guess in blank:
        print('you have already guessed letter {user_guess}')
    #crossing against the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            blank[position] = letter
       #Handling guess not in word
    if letter != user_guess:
        lives-=1
        print('Wwrong guess, you have lost a life buddy')
        if lives == 0:
            end_of_game = True
            print('game over, you lose')

       #Joining all the elements in the list and turning it into strings    
    print(f'{' '.join(blank)}')
    if '_' not in blank:
        end_of_game = True
        print('You win')
    print(stages[lives])