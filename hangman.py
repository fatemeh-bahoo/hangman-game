import random 
import hangman_ascii

from hangman_words import word_list
chosen_word = random.choice(word_list)

end_of_the_game = False
lives = 6

from hangman_logo import logo
print(logo)

display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print(f"You've already guessed {guess} letter")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. Now you have {lives} lives" + hangman_ascii.stages[lives])
        if lives == 0:
            end_of_the_game = True
            print(f"You lose!, the answer was: '{chosen_word}'")            

    print(f"Your answer: {' '.join(display)}")

    if "_" not in display:
        end_of_the_game = True
        print("You win.")