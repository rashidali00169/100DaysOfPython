#/////////////////////////////  DAY 4 ///////////////////////////////

#1 Randomisation
#2 Exercise on randomisation(random numbers)
#3 Lists + list methods
#(i) append()
#(ii) extend()
#(iii) insert()
#(iv) remove()
#(v) pop()
#(vi) clear()
#(vii) index()
#(viii) count()
#(ix) sort()
#(x) reverse()
#(xi) copy()
#(xii) del keyword
#4 Exercise on list
#5 Nested Lists
#6 Exercise on nested list
#7 Made a Project on "Rock, Paper and Scissors"

#Random numbers

 #import random
# randomInteger = random.randint(1,10) # random numbers from 1-10
# print(randomInteger)
#
# randFloat = random.random()     # floating random number from 0-1
# print(randFloat)
#
# randFloatNumber = random.random() * 5    # floating numbers form 1.0-5
# print(randFloatNumber)
#
#
# loveScore = random.randint(1,100)
# print(loveScore)

#exercise on random numbers using head tail example
# toss = random.randint(1,2)
# if(toss == 1):
#     print(f"{toss} Head")
# else:
#     print(f"{toss} Tail")



#list, a value having multiple values index bases of same or different type of data types
# list = ["Rashid", "Sain", "Musab", "Zeeshan", "Usama", 1,2,3,4,5,6, True, False]
# print(list)

#// Methods or data structure of List

# append()  add an item to the end of the list.
myList = []
myList.append('Rashid')
myList.append('Ali')
myList.append('"Musab"')
myList.append('"Ahmad"')
myList.append('"Arham"')


print(myList)

#extend(iterable)  Extend the list by appending all the items from the iterable.
myList.extend("Usama") # iterable as U s a m a
print(myList)

#insert() Insert an item at a given position

myList.insert(0, "Zeeshan")
myList.insert(1,"Ahmad")
print(myList)

#remove() Remove the first item from the list
myList.remove("Zeeshan")
print(myList)

#pop() Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
myList.pop()  #remove last item
print(myList)

myList.pop(0)  # remove from the specific position which is 0
print(myList)


#clear() Remove all items from the list.
# myList.clear()
# print(myList)

#index()   Return zero-based index in the list of the first item whose value is equal to x.
# Raises a ValueError if there is no such item.
#The optional arguments start and end are interpreted as in the slice notation and are used
# to limit the search to a particular subsequence of the list.
# The returned index is computed relative to the beginning of the full sequence
# rather than the start argument.

index = myList.index("Rashid")  #give index of the argument
print(f"The index of 'Rashid' is {index} in the list")


#count() Return the number of times x appears in the list.
count = myList.count("Rashid")
print(f"Rashid is occure {count} times in the list")

#sort() sorting in ascending order
myList.sort()
print(myList)

anotherlist = [5,9,4,7,2,8,1,6]
anotherlist.sort()
print(anotherlist)


#reverse() Reverse the item in list in descending order
myList.reverse()
print(myList)

anotherlist.reverse()
print(anotherlist)


#copy() Return a shallow copy of the list
#if assign one list to other then it copy the list reference change in one will be in both
myOtherlist = myList
print(myOtherlist)
myOtherlist.append("Faiz")
print(myOtherlist)
print(myList)
#usign copy() will never change in both list if one is changed
myLastList = myList.copy()
print(myLastList)
myLastList.append("irfan")
print(myLastList)
print(myList)

#del keyword to delete an item
del myList[0]
print(myList)

#Exercise to choose who will pay the bill

import random

# name = ["Rashid", "Bilal", "Ahmad", "Hassan", "Faiz"]
# nameLength = len(name)
# guess = random.randint(0,nameLength-1)
#
# print(f"{name[guess]} is going to get meal")


#Nested Lists
# fruit = ["Apple", "Banana", "Melon"]
# vegetable = ["Potato", "Tomato", "Onion"]
# mixList = [fruit,vegetable]
# print(mixList)

# print(mixList[1][0])  #Potato
# print(mixList[0][1])  #Banana



#Nested List Exercise
# line1 = [" a ", " b ", " c "]
# line2 = [" a ", " b ", " c "]
# line3 = [" a ", " b ", " c "]
# map = [line1, line2, line3]
#
# position = input()
# letter = position[0].lower()  #first letter of position converted into lower case
# abc = ['a', 'b', 'c']
# letterIndex = abc.index(letter)
# numberIndex = int(position[1]) - 1   # convert second letter of position and do -1 (-1 from the actual length which will be 2)
# map[numberIndex][letterIndex] = 'x'
#
# print(f"{line1}\n{line2}\n{line3}")

#Project
#Rock, Paper, Scisso Game



rock = '''
    _________
___|     _____)
        (_____)
        (______)
---      (____)
  |_____(___)

'''


paper = '''
    ____________
___|     __________)
        (____________)
        (______________)
---     (__________)
  |_____(________)

'''


scissor = '''
    _______
___|  _____ )______
         __________ )
           __________
        _____________ )
        (_____)
---|___(___)

'''

print(rock)
print(paper)
print(scissor)

# 0 for Rock
# 1 for paper
# 2 for scissor


computerChoice = random.randint(0,2)


myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))

print(f"Computer Choose {computerChoice}")
print(f"You choose {myChoice}")

if (myChoice >= 3 or myChoice <0):
    print("Give a valid number from [0, 1, 2]")
elif(myChoice == computerChoice):
    print("Draw")
#checking all conditions for my winning
elif((myChoice == 0) and (computerChoice == 2 )) or ((myChoice == 2) and (computerChoice == 1)) or ((myChoice == 1) and (computerChoice == 0)):  #Rock wins against scissor
    print("You Win")

else:
    print("Computer Win")




# //////// Day 4 Completed //////////////