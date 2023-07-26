#AIM: WAP to display the grade of a statment based on the percentage enterd by the user criteria as follow.

per=int(input("Enter the percentage:-"))
if(per>90):
    print("Grade is A+")
elif(per>80 and per<=89):
    print("Grade is A")
elif(per>70 and per<=79):
    print("Grade is B")
elif(per>60 and per<=69):
    print("Grade is C")
elif(per>50 and per<=59):
    print("Grade is D")
else:
    print("Fail")
