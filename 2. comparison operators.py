#Q1.Write a program to compare two numbers and print whether they are equal or not.

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if num1 == num2:
    print("numbers are equal")

else:
    print("numbers are not equal")

#-----------------------------------------------------------------------------------
#Q2.Create a program that checks whether a given number is positive, negative, or zero.

num = int(input("enter the first number: "))

if num >=1:
    print("number is positive")

elif num<0:
    print("number is negative")

else:
    print("number is zero")    

#----------------------------------------------------------------------------------------
# Q3.Write a program to compare three numbers and find the maximum among them.    

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is maximum")

elif num2>num1 and num2>num3:
    print(f"{num2} is maximum")

else :
    print(f"{num3} is maximum")

#--------------------------------------------------------------------------------------
# Q4.Create a program to determine if a given year is a leap year or not.
year = int(input("enter a year: "))

if year %4==0 and year %100!=0 or year%400==0:
    print("leap year")
else:
    print("not leap year")    

#--------------------------------------------------------------------------------------
#Q5.Write a program to compare two strings and check if they are equal or not.

str1 = input("enter a string")
str2 = input("enter a string")

if str1 == str2:
    print("strings are equal")
else:
    print("strings are not equal")    

#-----------------------------------------------------------------------------------------
#Q6.Create a program to determine whether a given number is even or odd.

n = int(input("enter a number: "))

if n%2==0:
    print("even number")
else:
    print("odd number")    


#-----------------------------------------------------------------------------------------
# Q7.Write a program to check if a number is positive and even.    

n = int(input("enter a number: "))

if n>0 and n%2==0:
    print("positive even number")

else:
    print(" negative odd number")

#----------------------------------------------------------------------------------------
# Q8.Create a program to check if a number is divisible by another number.

n1 = int(input("enter a number: "))
n2 = int(input("enter number number you want to divide by: "))

if n1%n2==0:
    print(f"{n1} is divisible by {n2} ")
else:
    print(f"{n1} is not divisible by {n2} ")

#----------------------------------------------------------------------------------------
# Q9.Write a program to check if a given character is a vowel or consonant.
vowel = input("enter a vowel")

list = ["a","e","i","o","u"]

if vowel in list:
    print("it is a vowel")
else:
    print("not a vowel")    

#---------------------------------------------------------------------------------------
#Q10.Create a program to check if a number is greater than, less than, or equal to zero.

num1 = int(input("enter a number: "))
 
if num1>0:
    print(f"{num1} is greater than zero")

elif num1<0:
    print(f"{num1} is less than zero") 

else:
    print(f"{num1} is equal to zero")


#--------------------------------------------------------------------------------------------
#Q11.Create a program to check if a number is positive and greater than 10


num1 = int(input("enter a number: "))

if num1>0 and num1>10:
    print(f"{num1} is positive and greater than 10")

else:
      print(f"{num1} is less than 10")

      
#---------------------------------------------------------------------------------------------
#Q12.Write a program to check if a number is odd and less than 100.

num = int(input("enter a number: "))

if num<100 and num%2!=0:
    print("number is odd and less than 100")

else:
    print("number is even or odd and less than or greater than 100")