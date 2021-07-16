import random
import time
print ("Welcome to the random number generator program!")
time.sleep(0.7)
print ("This program will generate as many random numbers as you want with a range of your own choice.")
time.sleep(0.7)
Use=str(input("Do you want to use the random number generator (Yes/No) "))
if Use=="No":
    quit()
if Use=="Yes":
    time.sleep(0.7)
    U_r=int(input("Enter the upper range - "))
    U_l=int(input("Enter the lower range - "))
    Number=random.randint(U_l,U_r)
    time.sleep(0.7)
    print ("The randomly generated number is ", Number)
while True:
    time.sleep(0.9)
    Again=str(input("Do you want to use the program again? (Yes/No) "))
    if Again=="No":
        print ("Thanks for using this program!")
        quit()
    if Again=="Yes":
        New_range=str(input("Do you want to enter a new range? (Yes/No) "))
        if New_range=="No":
            Number=random.randint(U_l,U_r)
            time.sleep(0.7)
            print ("The randomly generated number is ",Number)
        if New_range=="Yes":
            U_r=int(input("Enter the upper range - "))
            U_l=int(input("Enter the lower range - "))
            Number=random.randint(U_l,U_r)
            time.sleep(0.7)
            print ("The randomly generated number is ",Number)
