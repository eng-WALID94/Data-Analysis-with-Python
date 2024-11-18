#Question 3: Write a program that takes the temperature in Celsius as input from the user.
#If the temperature is below 0, print "It's freezing!" If it's between 0 and 20, print "It's cold.
# " Otherwise, print "It's warm."



# My name is: WALID MUKHLIS ALI
#Question 3:
T = float(input("Please enter the temperature in Celsius: "))
if T < 0:
    print("It's freezing!")
elif T < 20 and T > 0:
    print("It's cold.")
else:
    print("It's warm.")