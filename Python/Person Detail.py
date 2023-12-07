import datetime

name=input("Enter your name :")

age=int(input("Enter your age : "))

year =int(input('Enter your birth year :'))

month =int(input('Enter your birth month :'))

day =int(input('Enter your birth day :'))

dob = datetime.date(year, month, day)

bl=input("Degree : ")

aim_in_life=input("Enter your aim of life :")

print('Name :',name)

print('Age :',age)

print('DOB :',dob)

print('Class :',bl)

print('Aim in life :',aim_in_life)