import random


word_list = ["Punjab", "Sindh", "Blochistan", "KPK"]
target_word = random.choice(word_list).lower()
print(target_word)

display_word = []
for letters in target_word:
    display_word += '_'
print(display_word)

lives = 6
game_over = False
while game_over == False:
    guess_letter = input("Guess a letter : ")
    # print(guess_letter)
    #clear_output()

    if guess_letter in display_word:
        print("This letter already guessed, try different letter")

    if guess_letter in target_word:
        for position in range(len(target_word)):
            if guess_letter == target_word[position]:
                display_word[position] = guess_letter

    else:
        lives -= 1
       # print(hangman[lives])
        print(lives, "lives left.")
        if lives == 0:
            game_over = True
            print("You lost !!")
            print("Correct word is : ", target_word)

    if '_' not in display_word:
        print("You win !!")
        game_over = True

    print(display_word)