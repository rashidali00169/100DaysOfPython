#/////////////////////////////  DAY 3 ///////////////////////////////

#1 Conditional Statement (if else)
#2 Nested if elif and do some exercises on this
#3 Exercise to check weight using bmi
#4 Exercise to check the year is leap year or not
#5 Exercise to add items in pizza food delivery
#6 Logical Operator
#7 Code Block
#8 Scope
#9 Mini project of treasure land


print("Welcome to the Day 3 in 100 Days of Python Programming")
# conditional Statement (if else)

# prompt a number from the user to check the number is even or odd?

# number = int(input("Enter a number: "))
# if(number % 2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")



# write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them interpretation of their BMI based on the BMI value

# height = float(input("Enter your height in meters: "))
# weight = int(input("Enter your weight in kg: "))
# bmi = weight / (height * height)
# if (bmi <= 18):
#     print(f"The weight is {round(bmi, 2)}, They are under weight")
# elif (bmi >= 18.5 and bmi< 25):
#     print(f"The weight is {round(bmi, 2)}, They have a normal weight")
# elif (bmi >= 25 and bmi < 30):
#     print(f"The weight is {round(bmi, 2)}, They are slightly overweight")
# elif (bmi >= 30 and bmi < 35):
#     print(f"The weight is {round(bmi, 2)}, They are obese")
# else:
#     print(f"The weight is {round(bmi, 2)}, They are clinically obese")



#Checking the year is leap or not

# year = int(input("Enter the year you want to check: "))
# if (year % 4 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


#Pizza order exercise


# print("Thank you for choosing python pizza delivery")
# small = 15
# normal = 20
# large = 25
# print(f"Small size Pizza = {small}")
# print(f"Normal size Pizza = {normal}")
# print(f"Large size Pizza = {large}")
# size = input("What size pizza do you want S[small], N[normal], L[large]?  ")
# addPeppironi = input("Do want to add Peppironi Y[yes],N[no]?  ")
# extraCheese = input("Do you want extra cheese? Y[yes], N[no]?  ")
#
#
# if(size == 's' or size == 'S'):
#     if(addPeppironi == 'Y' or addPeppironi == 'y'):
#         small = small + 2
#     if(extraCheese == 'Y' or extraCheese == 'y'):
#          small = small + 1
#     print(f"Total bill for small pizza is {small}")
#
# elif(size == 'n' or size == 'N'):
#     if (addPeppironi == 'Y' or addPeppironi == 'y'):
#         normal = normal + 3
#     if (extraCheese == 'Y' or extraCheese == 'y'):
#         normal = normal + 1
#     print(f"Total bill for small pizza is {normal}")
#
#
# elif(size == 'l' or size == 'L'):
#     if (addPeppironi == 'Y' or addPeppironi == 'y'):
#         large = large + 3
#     if (extraCheese == 'Y' or extraCheese == 'y'):
#         large = large + 1
#     print(f"Total bill for small pizza is {large}")
#
# else:
#     print("Please enter the correct choice from S, N and L")



#love checker exercise

# name1 = input("Enter first person name: ")
# name2 = input("Enter second person name: ")
# couple = name1 + name2
# coupleName = couple.lower()
# t = coupleName.count('t')
# r = coupleName.count('r')
# u = coupleName.count('u')
# e = coupleName.count('e')
#
# score1 = t + r + u + e
#
#
# l = coupleName.count('l')
# o = coupleName.count('o')
# v = coupleName.count('v')
# e = coupleName.count('e')
#
# score2 = l + o + v + e
#
# totalScore = int(str(score1) + str(score2))
#
# if((totalScore < 10) or (totalScore > 90)):
#     print(f"Your score is {totalScore}, you go together coke and mentos")
# elif((totalScore >= 40) or (totalScore <= 50)):
#     print(f"Your score is {totalScore}, you are alright together")
# else:
#     print(f"your score is {totalScore}")



#Project Tresure Land
print("Welcome to the treasure land")
print("Your mission is to find the treasure.")
turn = input('you are at a cross road. Where do you want to go? Type "left" or "right": ')
if (turn == "left" or turn == "Left"):
    nextTurn = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if(nextTurn == "Wait" or nextTurn == "wait"):
        door = input("You arrived at the island unharm. There is a house 3 doors. Red, Yellow and Blue. Which color do you choose? ")
        if (door == "Yellow" or door == "yellow"):
            print("Your found the treasure. You Win")
        elif(door == "Blue" or door == "blue"):
            print("You enter a room of beasts. Game Over.")
        else:
            print("It's full of fire. Game Over.")
    else:
        print("You get attack by angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")



#//////// Day 3 Completed //////////////