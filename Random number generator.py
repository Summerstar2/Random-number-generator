import random
def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
print ("Welcome to the random number generator program!")
print ("This program will generate as many random numbers as you want with a range of your own choice.")
Use=str(input("Do you want to use the random number generator (Yes/No) "))
if Use=="No":
    quit()
if Use=="Yes":
    while True:
        U_r=int(input("Enter the upper range - "))
        U_l=int(input("Enter the lower range - "))
        while U_r<U_l:
            print ("Upper range cannot be lower than lower range. Enter again.")
            U_r=int(input("Enter the upper range - "))
            U_l=int(input("Enter the lower range - "))
        Number=random.randint(U_l,U_r)
        print ("The randomly generated number is ", Number)
        if not Continue():
            break
