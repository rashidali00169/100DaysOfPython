#////////////////// Day 8 ////////////////////

#functions with parameters and arguments
#Task Exercise to check how many cane needed for painting a wall
#Task Exercise to check a number is prime or not
#Project Ceaser Cipher


import math


def greet(name,location):
    print(f"Hello {name}, are you from {location}?")
greet( "Rashid", "Sadiqabad")


#we can also take positional keyword as an argument

def greetWith (name, location):
    print(f"Hello {name}, are you from {location}?")
greetWith(name="Ali", location="RYK")

#we can pass our input also as argument

# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
#
# def myFunction(first, last):
#     print(f"My first name is {first} and my last name is {last}")
#
# myFunction(firstName, lastName)

#
# def paint(height, width, coverage):
#     noOfCane = (height * width) / 5
#     print(f"You will need {math.ceil(noOfCane)} of cane")
#
#
# testHeight = int(input("Enter height of the wall: "))
# testWidth = int(input("Enter width of the wall: "))
#
# coverage = 5
# paint(testHeight,testWidth,coverage)



#Check the number is prime or not

number = int(input("Enter a number: "))

def primeNumber(number):
    isPrime = True
    for i in range (2,number):
        print(f"The value of i is {i}")
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("Prime number")
    else:
        print("Not a prime number")

primeNumber(number)