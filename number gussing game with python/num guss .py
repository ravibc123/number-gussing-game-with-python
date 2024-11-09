import random
number=random.randint(1,90)
gusses=0
while gusses!=number:
    gusses=int(input("enter your gusses number"))

    if (gusses<number):

        print("gusses too low number:")
        gusses=int(input("enter your number again"))

    elif(gusses>number):
        print("gusses high  number:")
        gusses=int(input("enter your number again"))
    else:
        break
    print("you gussed the right number")
