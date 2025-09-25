#import sys
#print(sys.version)
#print("hello world!")


#a = 789
#b = 123
#print(a,b)
#printing a single value for two varibles in a single line

#a = b = 100
#print(a,b)

#a , b = 10, 30 
#c , d = a, b
#print(c,d,a,b)

#a = 4
#b = 6
#c = 2
#print(a*b , b*c , c*a)

#type of data
# name = "app",
# age = 18
# phone = 2456789092
# student = True

# print(type(name) ,type(age),type(phone),type(student))

#days in a week
# day = 7
# one = 24
# hours = day * one
# print(hours)
# print(one*60) #mins in one day
# print(day*one*60)#mins in a week

# count = input("Enter the number:")
# min = 60
# print("minutes of the given number:",int(count) * min)

# count = int(input("Enter your age:"))
# days = int(count) * 365
# hours = days * 24
# mins = hours * 60
# secs = mins * 60
# print("your days:",days)
# print("your hours:",hours)
# print("your mins:",mins)
# print("your secs:",secs)


# tuple = (1,2,3,4,5)
# print(type(tuple))

# set = {12,3,4,5}
# print(type(set))

# dict = {"name":"th","age":"18"}
# print(type(dict))

# list = [3,4,5,6]
# print(type(list))

#displaying values and indexing list

# a = (1,"th",2.5,True)
# b = {80,90}
# c = {"name":"th" , "age":18 ,}
# d = [3,4,5,6]

# print(a[0])
# print(c["name"])
# print(d[2])
# print(list(b)[0])

#using if else statement
#p = int(input("Enter the number:"))
# if p >= 75:

#  print("ur are eligible for program")
# else:
#  print("ur not eligible for the program")

#print("ur eligible for the program" if p >= 75 else "ur are not eliugible")

#checking login
# username = "rafath"
# password = "thsuperiordam15"

# a = (input("Enter ur username:"))
# b = (input("Enter us password:"))

#print("login successfull" if a == username and b == password else "unsucessfull")

# if a == username and b == password:
#     print("login successfull")
# else:
#     print("unsucessfull")

#range
# a = range(20)
# print(a)
# print(list(a))
# print(tuple(a))
# print(set(a))

#for
# a = [1,2,3,4,5]
# for i in a:
#     print("num:",i)
# a = [14,15,23,40]
# for i in a:
#     if(i % 2 == 0):
#      print("even:",i)
#     else:
#        print("odd:",i)

# a = [1,2,3,4,5,7] 
# print(len(a))   

#duplicate
# a = [1,2,3,4,1,5,6]
# b = len(a)
# for i in range(0,b):
#     for j in range(i+1,b):
#         if(a[i] == a[j]):
#             print("duplicate:",a[i],"at indices",i,"and",j)

#function
# def add(a,b):
#      return a + b
# print(add(1,3))
# print(add(4,2))

# name = input("Enter the name:")
# age = int(input("Enter the age:"))
# height = int(input("Enter the height in cm:"))
# height_in_meters = float(height/100)
# weight = int(input("Enter the weight"))

# bmi = weight/(height_in_meters)**2
# print(bmi)
# if bmi < 18.5:
#     print("under weight")
# elif bmi >= 18.5 and bmi <= 24.9:
#     print("healthy weight")
# elif bmi >= 25.0 and bmi <= 30.0:
#     print("over weight")
# elif bmi >= 30.0 and bmi <= 35.0:
#     print("obesity")
# else:
#     print("severe obesity")
  #square 
# x = y = z = 15
# print(x**2 + y**2 + z**2)

#area of triangle
# b = int(input("Enter the base:"))
# h = int(input("Enter the height"))
# area = 0.5 * b * h
# print("area of triangle:",area)

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("error:division by zero is not allowed")
#modules
def add(a,b):
    return print(a + b)
add(45,50)

import math
print(math.pi)