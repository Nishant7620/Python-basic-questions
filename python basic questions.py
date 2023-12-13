# Print the phrase "Hello, World!" using the print statement.

print("Hello, World!")

#------------------------------------------------------------------------------------------------------------------------------------
# Print three different messages on separate lines.
print("Always Work Hard")
print("Python is interpreted language")
print("Python is high level language")

#-------------------------------------------------------------------------------------------------------------------------------
#: Print three different messages on separate lines using one print statement.

print("Always work hard\n Python is easy to learn language\n Python is high level language")

#-----------------------------------------------------------------------------------------------------------------------------------
#Concatenate and print two variables.

x = "Hello"
y = "World"

print(x+y)

#---------------------------------------------------------------------------------------------------------------------------------
#Print three words separated by a specific character ‘$’

print("Always", "Work", "Hard",sep="$")

#----------------------------------------------------------------------------------------------------------------------------------
#Print two messages on the same line using the end parameter.

msg1="Python is easy to learn language"

msg2 ="Python is highlevel language"

print(msg1,end=" ")
print(msg2)

#---------------------------------------------------------------------------------------------------------------------------------
#Print a message with quotes around it.

msg ="Python is \"highlevel\" language"
print(msg)

#---------------------------------------------------------------------------------------------------------------------------------
#Print the result of a boolean expression.

x = 10
y = 10

print(x==y)

#================================================================================================================================
#2.Type casting:

#Q1: Convert an integer to a float.

x=10
y = float(x)
print(y)

#--------------------------------------------------------------------------------------------------------------------------------
# Q2: Convert a float to an integer.

x = 5.5
y = int(x)

print(y)

#---------------------------------------------------------------------------------------------------------------------------------
# Q3: Convert a string to an integer.

str1 ="20"
x =int(str1)

print(x)
#----------------------------------------------------------------------------------------------------------------------------------
# Q4: Convert a string to a float.

str1 ="25"
y = float(str1)

print(y)
#---------------------------------------------------------------------------------------------------------------------------------
# Q5: Convert an integer to a string.

x = 15
y=str(x)
print(y,type(y))
#----------------------------------------------------------------------------------------------------------------------------------
# Q6: Convert a float to a string.

Float = 8.5
str2 = str(Float)

print(str2,type(str2))
#----------------------------------------------------------------------------------------------------------------------------------
# Q7: Convert a string to a list of characters.

str1 ="PYTHON"
list1 =list(str1)
print(list1)

#---------------------------------------------------------------------------------------------------------------------------------
# Q8: Convert an integer to its binary representation.

a =  10
b =bin(a)

print(b)
#---------------------------------------------------------------------------------------------------------------------------------
# Q9: Convert a binary string to an integer.

p =0b1010
q =str(p)
print(q)

#-----------------------------------------------------------------------------------------------------------------------------------
# Q10: Convert a tuple to a list

tuple1 = (1,2,3,4,5,6)

list2 =list(tuple1)
print(list2)

#----------------------------------------------------------------------------------------------------------------------------------
# Q11: Convert a list to a tuple.

listt = [1,2,3,4,5,6]

tupple =tuple(listt)
print(tupple)

#-----------------------------------------------------------------------------------------------------------------------------------
# Q12: Convert a set to a list.

s = {1,2,3,4,5,6}

t =tuple(s)
print(t)

#----------------------------------------------------------------------------------------------------------------------------------
# Q13: Convert a list to a set.

l =[1,2,3,4,5,6]
s1 =set(l)
print(s1)