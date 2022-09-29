import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear #clear the screen after every letter guess

print(logo)
game_is_finished = False
lives = len(stages) - 1 #variable to keep track of how many lives left

chosen_word = random.choice(word_list)  #chose random word from word_list
word_length = len(chosen_word) #get the lenght of the chosen word

#create blank list
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished: #while game is false
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"The word was {chosen_word}")
            print("You lost.")
      
    #check if user has got all letters
    if not "_" in display:
        game_is_finished = True
        print("You won.")
  
    print(stages[lives])