# Question 5: Write a program that asks the user to input their exam score. If the score is 90 or above, print "Excellent."
# If it is between 75 and 89, print "Good job."
# If it's between 50 and 74, print "You passed."
# If it's below 50, print "You failed."



# My name is: WALID MUKHLIS ALI
# Question 5:


ScoreNo = float(input("Enter the exam score: "))
if ScoreNo >= 90:
    print("Excellent!")
elif  75 <= ScoreNo <= 89:
    print("Good job!")
elif 50 <= ScoreNo <= 74:
    print("You passed!")
else:
    print("You failed!")