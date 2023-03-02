1)Why Python is general-purpose dynamic high-level and interpreted language?
 Ans:- Because they are not written in machine-readable language,
 Python programs need to be processed before machines can run them. 
Python is an interpreted language. 
This means that every time a program is run, its interpreter runs through the code and translates it into machine-readable byte code.

2)Why is Python called a dynamically typed language?
Dynamic typing means that the type of the variable is determined only during runtime.

3)List some pros and cons of Python programming language?
ANS:- pros:
1)python is a Simple to learn.
2)python is Easy to Use.
3)python Highly Compatible.
4)It is Object-Oriented.
5)python has Lots of Libraries.
6)python has Built-in Data Structures.

cons:
1) poor Memory Efficiency.
2) slow Speed.
3) weak in Mobile Computing.
4) runtime Errors.

4) In what all domains can we use Python?
Ans:- data science, web development, scientific programming.

5)What are variable and how can we declare them?
Ans:- any thing which declare the information of data
Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

6)How can we take an input from the user in Python?
ans:- we can use input() function

7)What is the default datatype of the value that has been taken as an input using input() function?
Ans:- By default, python returns a string object.

8)What is type casting?
ans:-Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

9)Can we take more than one input from the user using single input() function? If yes, how? If no, why?
Ans:- yes we can take multiple inputs in single input()
a, b, c = input("Enter three values: ").split()
print("Total number of students: ", a)
print("Number of boys is : ", b)
print("Number of girls is : ", c)

10) what are keywords 
Ans:- basicaly we use keywords are break, continue, true, false, and, or, not, for, while, def, class, if, else, elif, import, from, except, exec, print, return, yield, lambda, global

11)Can we use keywords as a variable? Support your answer with reason.
Ans:- We cannot use a keyword as a variable name, function name, or any other identifier. 
They are used to define the syntax and structure of the Python language.    

12)What is indentation? What's the use of indentaion in Python?
Ans:-Indentation simply means the space from the margin to the beginning of the characters in a line
 Python uses indentation to indicate a block of code.

13)How can we throw some output in Python?
Ans:- The basic way to do output is the print statement
print()

14)What are operators in Python?
Ans:- In Python, operators are special symbols that designate that some sort of computation should be performed.
operators are + for addition
 - for substractions
 * for multiplication
 / for float division
 // for integer division
 ** for power calculation
 % for Modulus

x = 5
y = 3

print("Addition of x + y = ", x+y)
print("Substraction of x - y = ", x-y)
print("Multiplication of x * y = ", x*y)
print("Float Division of x / y = ", x/y)
print("Integer Divison of x // y = ", x//y)
print("Modulus of x % y = ", x%y)
print("Power of y on x i.e; x ** y = ", x**y)

15)What is difference between / and // operators?
ans:- 
Normal Division : Divides the value on the left by the one on the right. Notice that division results in a floating-point value.

divide=10/3 #Normal Division  

print(divide)  

OUTPUT :  3.333333333333333  

Floor Division : Divides and returns the integer value of the quotient. It neglects the digits after the decimal.

divide=10//3 #Floor Division  

print(divide)  

OUTPUT :  3
16)Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron

ans:- numeric_str = "ineuron"*4
print("Multiply numeric str = ", numeric_str)

17)Write a code to take a number as an input from the user and check if the number is odd or even.
ans:- 
num = int (input("enter the number even or odd"))
if(num%2) ==0 :
    print("number is even", num)
else:
   print("number is odd",num)

18) What are boolean operator?
it is operator like true or false 

19)  What will the output of the following?

1 or 0

0 and 0

True and False and True

1 or 0 or 0

answer:-- 1 or 0 --->
if we treat 1 if true , 0 is false 
then the statement becomes true.

0 and 0 --->> true only

true and false and true ---> true only

1 or 0 or 0 --->> true only


20)What are conditional statements in Python?
answer:-- 
A conditional statement tells a program to execute an action depending on whether a condition is true or false.
conditional statement are 
if, if..else, nested  if if-elif statment.

21) what is the use of if , elif and else keyword ?
answer:--The if...else statement is used to execute a block of code among two alternatives. However, if we need to make a choice between more than two alternatives, then we use the if...elif...else statement. 
Here, If condition1 evaluates to true , code block 1 is executed.

22) Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
answer:-- 
age = 22
if age >= 18:
    print("i can vote")
else:
    print("i cant vote")   
 
output :-- 
=======
i can vote

  age = 15
if age >= 18:
    print("i can vote")
elif age < 18:
    print("i cant vote")
else:
    print("byy!!") 
 
output:--
=======
i cant vote

23) Write a code that displays the sum of all the even numbers from the given list.
numbers = [12, 75, 150, 180, 145, 525, 50]

answer:--
nums = [12, 75, 150, 180, 145, 525, 50]
def solve(nums):
   return sum([i for i in nums if i % 2 == 1])
print(solve(nums))

output is :--
745

24) Write a code to take 3 numbers as an input from the user and display the greatest no as output.
answer:-- 
a = 10
b = 15
c = 20

if a > b and a>c:
    print("largest number is a", a)
elif b>c:
    print("largest number is b", b)
else :
    print("largest number is c", c) 

output is :---
==============
largest number is c 20

25) Write a program to display only those numbers from a list that satisfy the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]

answer:--
a = [12, 75, 150, 180, 145, 525, 50]
b = []
for i in a:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        b.append(i)
        
print(b)

output is:---
=============
[75, 150, 145]

