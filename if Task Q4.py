#Question 4: Create a program that asks the user to enter two numbers.
# The program should compare the numbers and print which one is greater or if they are equal.

# My name is: WALID MUKHLIS ALI
#Question 4:


no1 = int(input("Please enter the first number: "))
no2 = int(input("Please enter the second number: "))

if no1 > no2:
    print(f"Number {no1} is greater than {no2}")
elif no2 > no1:
    print(f"Number {no2} is greater than {no1}")
else:
    print(f"The first number {no1} are equal to the second number {no2}")