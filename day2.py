#/////////////////////////////  DAY 2 ///////////////////////////////

#1PRIMITIVE DATA TYPES
#2Getting characters from the string index
#3Type Error
#4Type Checking
#5Type Conversion
#6 exercises on Type conversion
#7Arithmetic Operations
#8BMI Calculator
#9round() function
#10Number manipulation
#11f-String
#12excercise on f-String and Math
#13 Tip calculator to the total bill



print("Welcome to the Day 2 in 100 Days of Python Programming")


# String
# finding the index in string  also said subscript
# string concatination
#print("Rashid"[0])
#print("Rashid"[1])
#print("Rashid"[2])
#print("Rashid"[3])
#print("Rashid"[4])
#print("Rashid"[5])

# getting last index of the string
#print("Rashid"[5])

#print(("12345")) # it is also a string

#print(("Rashid " + "12345")) # string concatination


#Integers

#print(12345)
#print(12 + 34)
#print(123_456_789)  #underscore is used instead of comma to sparate digits
#print(123456789)

#Float

#print(3.14) # decimal point numbers
#print(3.14 + 3.14)

#Boolean
# give result in the form of True or False

#print(2<4) #True
#print(2>4) #False


#Type Error
#len of integer can't be found through len()


#print(len(123456)) #TypeError: object of type 'int' has no len()
#myNameCharacters = len(input("Enter you name: "))

#string and numbers can't concatinate in a string

#print("There are " +myNameCharacters+ "characters in my name")  #TypeError: can only concatenate str (not "int") to str



#Type Checking

myName = "Rashid"
myAge = 24
height = 6.1
#print("The type of myName is" +type(myName))  #TypeError: can only concatenate str (not "type") to str
#print(type(myName))
#print(type(myAge))
#print(type(height))


#Type Conversion
#str() to convert into string
#float() to convert into float
#int() to convert into integer
#bool() to convert into integer

num = 123
myStr = "12345"
newNum = str(num)
#print(type(num))
#print(type(newNum))
#print(type(float(num)))
myNewStr = myStr
int(myNewStr)
#print(type(myNewStr))

myNum = 1
#print(type(bool(myNum)))

# small exercise
num1 = "123"
num2 = 12.3
num3 = 1
#print(int(num1)+int(num2)+int(num3))


#another exercise
#firstDigit = input("Enter a number to gets its first digit: ")  # input() return string value
#secondDigit = input("Enter a number to gets its second digits: ")
#sumOfTwoDigits = int(firstDigit[0]) + int(secondDigit[1])
#print(sumOfTwoDigits)


#one more exercise
#myDigit = input("Enter the  two digits number: ") #remember input return string value
#mySum = int(myDigit[0])+ int(myDigit[1])
#print(mySum)


#ARITHMETIC OPERATION
#print(4**4)      #(4)^2 = 64
#print(4*2)      #8
#print(4/2)      #2.0 result in float
#print(4%2)      # 0 remainder
#print(4-2)      #2
#print(4//2)     #2 result in integer


#BMI Calculator
myHeight = input("Enter your height in meters: ")
myWeight = input("Enter your weight in kg: ")
newHeight = float(myHeight)

newWeight = int(myWeight)
print((newHeight))
print(newWeight)

totHeight = newHeight * newHeight
bmi = newWeight / totHeight
print(bmi)


#round()
#print(round(2.28888))    # =3
#print(8/3)               #2.6666665
#print(round(8/3, 2))    #2.67 plcae 2 digits after decimal point (precision)

#f-String
name = "Rashid Ali"
age = 24
# print(f"My name is {name} and I am {age} years old")

#currentAge = input("Enter you age: ")
#currentAge = int(currentAge)
#endDate = 90       # total years life
#weeksinyear = 52    # 52 weeks in a year
#totWeek = weeksinyear * endDate   #total weeks in 90 years(exptectd end date of a man)
#currentWeek = currentAge * weeksinyear
#leftWeek = totWeek - currentWeek

#print(f"There are {leftWeek} weeks left in your life")



#13 Tip calculator to the total bill
print("Welcome to the Tip Calculator")
bill = input("What was the total bill? ")
myBill = float(bill)
tip = input("How much tip would you like to give? 10%, 12% or 15%? ")
totalTip = (int(tip) / 100) * myBill
totalBill = myBill + totalTip
totPeople = input("How many people to split the bill? ")
bilForEach = totalBill / int(totPeople)
print(f"Each person should pay {round(bilForEach,2)}")


#//////// Day 2 Completed //////////////