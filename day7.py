#////////////////// Day 7 ////////////////////

# Project of Hangman Game
import random

namesList = ["punjab", "sindh", "blochistan", "khaberpakhtunkhawa"]
chooseName = random.choice(namesList)
print(chooseName)
print(f"The length of name is {len(chooseName)}")

display = []
for x in range(0,len(chooseName)):
    display += "-"

print(display)




#print("\n")

lifes = 6
myGuessName = []
guessCharacter = input("Enter the character to guess it is in your name: ").lower()
for letter in chooseName:
    if letter == guessCharacter:
        print('yes')
    else:
        print("no")



# while(lifes > 0):
#
#     for position in range(len(chooseName)):
#         if (position == chooseName):
#             print("yes")




#         if (guessCharacter == x):
#             print("I Got it")
#             myGuessName = myGuessName + x
#         # if (len(listName) == len(listName)):
#         #     print("You Won")
#     if (guessCharacter != chooseName):
#             lifes = lifes -1
#
# print(myGuessName)





    # if (guessCharacter == myName):
    #     myGuessName = myGuessName + guessCharacter
    # elif (guessCharacter != myName):
    #     lifes = lifes -1
    #
    #
    # if (len(guessCharacter) == len(myName)):
    #     print("You Won")

# print("You loose")