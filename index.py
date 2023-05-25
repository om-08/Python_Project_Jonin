
import random
 #can call it using stages[0] where o is lives

import hangman
import hangman_word

chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)


lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []       #created list of [_]
for _ in range(word_length):
    display += "_"

#todo-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:      #this is important
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already gussed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    
    if guess  not in chosen_word :
        lives = lives - 1 
        print (f"You Gussed {guess}, that's not in the word. You Loose a Life, Total = {lives}")         # here it is not a idea place because its getiing printed 5 times so the lives calculation sucks
    else:
        print(f"You Gussed {guess}, that's  in the word. You do not loose a Life, Total = {lives}")
    print(f"{''.join(display)}")
     

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True    #overidden vlue for while loop to stop think like using boolean always data structures mei km aayega 
        print("You win.")
    elif (lives == 0):
        end_of_game = True
        print("You Lose U killed him ")
    print(hangman.stages[lives])

     