# This was developed by the Nerd Inc.
# Distributing this code as ones own will not be tolerated

import time
import random
import os
import sys

wallet = 500
bank = 0
fish = 0
cow = 0
dog = 0
cat = 0

answer = input("Welcome! Enter command(do help if you want a list of commands): ")

if answer.lower() == "buy":
    print("-Fish(10 points)")
    print("-Cow(20 points)")
    print("-Dog(30 points)")
    print("-Cat(35 points)")
    answer2 = (input("What would you like to buy? "))

    if answer2.lower() == "Cow":
        count1 = input("How many cows do you want to buy? ")
        price = int(count1) * 20

        if price < wallet:
            cow += int(count1)
            wallet -= int(price)
            print("You bought this many cows: " + str(count1))
            os.execl(sys.executable, sys.executable, *sys.argv)

        elif price > wallet:
            print("Not enough money!!")
            os.execl(sys.executable, sys.executable, *sys.argv)

    if answer2.lower() == ("dog"):
        count2 = input("How many dogs do you want to buy? ")
        price2 = int(count2) * 30

        if price2 < wallet:
            dog += int(count2)
            wallet -= int(price2)
            print("You bought this many dogs: " + str(count2))
            os.execl(sys.executable, sys.executable, *sys.argv)

        elif price2 > wallet:
            print("Not enough money!!")
            os.execl(sys.executable, sys.executable, *sys.argv)
    
    if answer2.lower() == ("fish"):
        count3 = input("How many fish do you want to buy? ")
        price3 = int(count3) * 10

        if price3 < wallet:
            fish += int(count3)
            wallet -= int(price3)
            print("You bought this many fish: " + str(count3))
            os.execl(sys.executable, sys.executable, *sys.argv)

        elif price3 > wallet:
            print("Not enough money!!")
            os.execl(sys.executable, sys.executable, *sys.argv)

    if answer2.lower() == ("cat"):
        count4 = input("How many cats do you want to buy? ")
        price4 = int(count4) * 35
        if price4 < wallet:
            cat += int(count4)
            wallet -= int(price4)
            print("You bought this many cats: " + str(count4))
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif price4 > wallet:
            print("Not enough money!!")
            os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("We dont have that item, please try again!")
        os.execl(sys.executable, sys.executable, *sys.argv)



if answer.lower() == "dep points":
    answer4 = int(input("How many points would you like to deposit?: "))
    if wallet > answer4:
        bank += answer4
        wallet -= answer4    
        print("Your bank balance: " + bank)
        print("Your wallet balance: " + wallet)
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif wallet < answer4:
        print("You dont have enough point for this action")
        os.execl(sys.executable, sys.executable, *sys.argv)



if answer.lower() == "roll dice":
    answer5 = input("Are You sure you want to roll a dice for 30 points, Yes/No: ")
    if answer5.lower() == "yes":
        wallet -= 30
        print("You rolled the number")
        time.sleep(0.4)
        print(".")
        time.sleep(0.4)
        print(".")
        time.sleep(0.4)
        print(".")
        luck = random.randint(1, 6)
        fortune = luck * 10
        wallet += fortune
        print("You won this many points: " + str(fortune))
        time.sleep(0.6)
        print("Your current wallet balance: " + str(wallet))
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    elif answer5.lower() == "no":
        os.execl(sys.executable, sys.executable, *sys.argv)



if answer.lower() == "help":
    print("-buy")
    print("-dep points")
    print("-roll dice")
    print("-bank status")
    os.execl(sys.executable, sys.executable, *sys.argv)



if answer.lower() == "bank status":
    print("Your wallet: " + str(wallet))
    print("Your bank account: " + str(bank))
    os.execl(sys.executable, sys.executable, *sys.argv)
