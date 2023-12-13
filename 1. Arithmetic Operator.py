#Q1. Create a program that takes two numbers as input and prints their sum.
num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

sum = num1 + num2

print(f"sum of numbers: {sum}")

#-----------------------------------------------------------------------------------------------------------------------------------------
#Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

sub = num2 - num1

print(f"subtraction of numbers is: {sub}")

#-----------------------------------------------------------------------------------------------------------------------------------
#Q3.Create a program that multiplies two numbers taken as input.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

mul = num1 * num2 

print(f"multiplication of numbers: {mul}")

#-----------------------------------------------------------------------------------------------------------------------------
#Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

if num2 <=0:
    print("enter non zero number or positive number")
else:
    div = num1 / num2
    print(f"division of numbers is: {div}")

#------------------------------------------------------------------------------------------------------------------------------
# Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

if num2 <=0:
    print("enter non zero number or positive number")
else:
    div = num1 // num2
    print(f"division of numbers is: {div}")

#------------------------------------------------------------------------------------------------------------------------------
# Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

if num2 <=0:
    print("enter non zero number or positive number")
else:
    div = num1 % num2
    print(f"division of numbers is: {div}")

#------------------------------------------------------------------------------------------------------------------------------------
#Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))

power = num2**num1

print(power)

#-------------------------------------------------------------------------------------------------------------------------------------
#Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
principal_amount =int(input("enter a principal amount: "))
rate_of_interest = float(input("enter a rate of interest: "))
time = int(input("enter a time"))

final_amount = principal_amount*(1+rate_of_interest /100)**time

print(final_amount)    

#----------------------------------------------------------------------------------------------------------------------------------
#Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental and decremental values.
num = int(input("enter a number"))

increment = num=+1
decrement = num=-1

print(f"incremental of number: {increment} and dremental of number: {decrement}")

#----------------------------------------------------------------------------------------------------------------------------------
#Q10.Write a program that takes three numbers as input and calculates their average.

num1 = int(input("enter a number"))
num2 = int(input('enter a number'))
num3 = int(input("enter a number"))

avg = (num1 + num2 + num3)/3

print(f"Average of three numbers is: {avg}")
 
 #----------------------------------------------------------------------------------------------------------------------------------
 #