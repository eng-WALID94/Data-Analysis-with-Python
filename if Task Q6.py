#Question 6: Ask the user to enter their age and whether they have a driver’s license (yes or no).
# If the user is 18 or older and has a driver’s license, print "You are allowed to drive.
# " Otherwise, print "You are not allowed to drive."



# My name is: WALID MUKHLIS ALI
# Question 6:

userAge = int(input("Enter your age: "))
driverLicense = input("Do you have a driver's license? (yes or no): ").lower()

if userAge >= 18 and driverLicense == "yes":
    print("You allowed to drive.")
else:
    print("You are not allowed to drive.")