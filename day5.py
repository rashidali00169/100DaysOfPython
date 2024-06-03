#////////////////// Day 5 /////////////////////////


#1 for loop
#2 Range Function
#3 Exercise to find the highest height above the school students from the list
#4 Exercise to find the maximum number from the list
#5 FizzBuzz Game
#6 Project Python Password Generator


import random

# fruit = ["Apple", "Banana", "Mango"]
# for x in fruit:
#     print(x)
#     print(x + " pie")
#     print(fruit)
#
# print(fruit)

#Exercise to count the avg height from the given students

# heights = [ 156, 178, 165, 171, 187]
#
# heightCounter = 0
# for h in heights:
#     heightCounter +=h
#
# print(f"Total Heights {heightCounter}")
# print(f"The total students {len(heights)}")
# avg = heightCounter/5
# print(f"The average height is {round(avg)}")




#take multiple input from user
# studentScor = input().split()
# for n in range(0, len(studentScor)):
#     studentScor[n]= int(studentScor[n])
# print(studentScor)
# max = 0
# for x in studentScor:
#     if (x > max):
#         max = x
#
#
# print(f"The highest score in the class is {max} ")



#Exercise to count the total of the numbers

# start = int(input("Enter starting range: "))
# end = int(input("Enter ending range: "))
# total = 0
# for x in range(start,end+1):
#     if(x % 2 ==0):
#         total += x
# print(total)




#FizzBuzz puzzle

# for x in range(1,101):
#
#      if((x % 3 == 0) and (x % 5 ==0)):
#         print("FizzBuzz")
#      elif (x % 3 == 0):
#          print("Fizz")
#      elif(x % 5 == 0):
#         print("Buzz")
#      else:
#          print(x)


# Project Python Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+']

print("Welcome to the PyPython Password Generator!")
totLetters = int(input("How many letters would you like in your password? "))
totSymbols = int(input("How many symbols  would you like in your password? "))
totNumbers = int(input("How many numbers would you like in your password? "))



myPassword = []
for password in range(0, totLetters):
    myPassword  +=random.choice(letters)

for password in range(0,totSymbols):
    myPassword += random.choice(symbols)


for password in range(0,totNumbers):
    myPassword += random.choice(numbers)

random.shuffle(myPassword)
print(f"Here is your password: {myPassword}")



#/////////////////// End of Day 5 /////////////////////
