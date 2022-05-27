# Version 1.0

"""
 This was developed by the NeighbourhoodCoders.
 Distributing this code as ones own will not be tolerated.
 This project was made by the effort of Dvir and Maksim.
"""

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
unicorn = 0
dinosaur = 0

while True:
    answer = input("Enter command(do help if you want a list of commands): ")
    try:
        if answer.lower() == "sell":
            answer6 = input("What do you want to sell? (dog, fish, cat, cow, unicorn, dinosaur) ")

            if answer6.lower() == "dog":
                amount = int(input("How many would you like to sell? "))
                if amount <= dog:
                    dog -= amount
                    wallet += amount * 20
                    print(wallet)
                if amount >= dog:
                    print("Not enough animals, try selling less!")

            if answer6.lower() == "fish":
                amount = int(input("How many would you like to sell? "))
                if amount <= fish:
                    fish -= amount
                    wallet += amount * 5
                    print(wallet)
                if amount >= fish:
                    print("Not enough animals, try selling less!")
            
            if answer6.lower() == "cat":
                amount = int(input("How many would you like to sell? "))
                if amount <= cat:
                    cat -= amount
                    wallet += amount * 25
                    print(wallet)
                if amount >= cat:
                    print("Not enough animals, try selling less!")

            if answer6.lower() == "cow":
                amount = int(input("How many would you like to sell? "))
                if amount <= cow:
                    cow -= amount
                    wallet += amount * 10
                    print(wallet)
                if amount >= cow:
                    print("Not enough animals, try selling less!")

            if answer6.lower() == "unicorn":
                amount = int(input("How many would you like to sell? "))
                if amount <= unicorn:
                    unicorn -= amount
                    wallet += amount * 90
                    print(wallet)
                if amount >= unicorn:
                    print("Not enough animals, try selling less!")

            if answer6.lower() == "dinosaur":
                amount = int(input("How many would you like to sell? "))
                if amount <= dinosaur:
                    dinosaur -= amount
                    wallet += amount * 190
                    print(wallet)
                if amount >= dinosaur:
                    print("Not enough animals, try selling less!")

        if answer.lower() == "buy":
            print("-Fish (10 points)")
            print("-Cow (20 points)")
            print("-Dog (30 points)")
            print("-Cat (35 points)")
            print("-Unicorn (100 points)")
            print("-Dinosaur (200 points)")
            answer2 = (input("What would you like to buy? "))

            if answer2.lower() == ("cow"):
                count1 = input("Sure you can even store a cow(s)?? Well, how many would you like? ")
                price1 = int(count1) * 20

                if price1 < wallet:
                    cow += int(count1)
                    wallet -= int(price1)
                    print("You bought this many cows: " + str(count1))


                elif price1 > wallet:
                    print("Not enough money! Go roll the dice and hope for luck. ")


            if answer2.lower() == ("dog"):
                count2 = input("It's always nice to have a dog, or dogs. How many you want? ")
                price2 = int(count2) * 30

                if price2 < wallet:
                    dog += int(count2)
                    wallet -= int(price2)
                    print("You bought this many dogs: " + str(count2))

                elif price2 > wallet:
                    print("Not enough money! Go roll the dice and hope for luck. ")

            if answer2.lower() == ("fish"):
                count3 = input("You gon' put them in the aquarium or are they for food? Anyways, how many? ")
                price3 = int(count3) * 10

                if price3 < wallet:
                    fish += int(count3)
                    wallet -= int(price3)
                    print("You bought this many fish: " + str(count3))

                elif price3 > wallet:
                    print("Not enough money! Go roll the dice and hope for luck. ")

            if answer2.lower() == ("cat"):
                count4 = input("I'd suggeest not to buy many, but it's your decision. How much? ")
                price4 = int(count4) * 35
                if price4 < wallet:
                    cat += int(count4)
                    wallet -= int(price4)
                    print("You bought this many cats: " + str(count4))
                elif price4 > wallet:
                    print("Not enough money! Go roll the dice and hope for luck. ")

            if answer2.lower() == ("unicorn"):
                count5 = input("Are you a girl? Who buys unicorns? Anyways, how much would you like? ")
                price5 = int(count5) * 100
                if price5 < wallet:
                   unicorn += int(count5)
                   wallet -= int(price5)
                   print("You bought this many unicorns: " + str(count5))
                elif price5 > wallet:
                    print("Not enough money! Go roll the dice and hope for luck. ")
                    

            if answer2.lower() == ("dinosaur"):
                count6 = input("You want to buy the almighty dinosaur? This one won't be cheap! So, how many? In case you can even afford 'many'. ")
                price6 = int(count6) * 200
                if price6 < wallet:
                   unicorn += int(count6)
                   wallet -= int(price6)
                   print("You bought this many dinosaurs: " + str(count6))
                   
                elif price6 > wallet:
                    print("Not enough money! Go roll the dice and hope for luck. ")
                    
                else:
                 print("Invalid command.")
        else:
            print("Unvalid command.")
    except:
        print("There was an error, please try again")

    try:
        if answer.lower() == "dep points":
            answer4 = int(
           input("How many points would you like to deposit (You can do all to deposit all of your points)?: "))
            if wallet >= answer4 and answer4 == "all":
                bank += wallet
                wallet -= wallet
                print("Your bank balance: " + str(bank))
                print("Your wallet balance: " + str(wallet))

            if wallet > answer4:
                bank += answer4
                wallet -= answer4
                print("Your bank balance: " + str(bank))
                print("Your wallet balance: " + str(wallet))
            elif wallet < answer4:
                print("You dont have enough point for this action")
    except:
        print("There was an error, please try again")

    try:
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

            elif answer5.lower() == "no":
                sys.exit("Goodbye friend!")
    except:
        print("There was an error, please try again")

    try:
        if answer.lower() == "help":
            print("-buy")
            print("-dep points")
            print("-roll dice")
            print("-bank status")
            print("-check real life")
            print("-reset")
            print("help { command } if you need help with a command")
    except:
        print("There was an error, please try again")

    try:
        if answer.lower() == "bank status":
            print("Your wallet: " + str(wallet))
            print("Your bank account: " + str(bank))
    except:
        print("There was an error, please try again")

    try:
        if answer.lower() == "check real life":
            print("Hey dude its: ")
            print("This date: " + time.strftime("%Y-%m-%d"))
            print("And this time: " + time.strftime("%H %M"))
            print("Go take a walk man. ")

    except:
        print("There was an error, please try again")

    if wallet == 0 and bank == 0:
        print("!! Game Over !!")
        game_over = input("Do you want to start over? Yes/No: ")
        if game_over.lower() == "yes":
            wallet += 500
            bank -= bank
            fish -= fish
            cow -= cow
            dog -= dog
            cat -= cat
            
        if game_over.lower() == "no":
            sys.exit("Sure, hope you come again!")

    try:
        if answer.lower() == "reset":
            reset = input("Reseting will make you loose all your procces, do you want to continue? Yes/No: ")
            if reset.lower() == "yes":
                print("Your progress will now be deleted, please be patient!")
                time.sleep(8)
                wallet += 500
                bank -= bank
                fish -= fish
                cow -= cow
                dog -= dog
                cat -= cat
                
            if reset.lower() == "no":
                print("Reset progress has been stopped")
                
    except:
        print("There was an error, please try again")
        

    try:
        if answer.lower() == "help buy":
            print("This command is used for buying items")
            
        if answer.lower() == "help dep points":
            print("This command is used for depositing points from your wallet to your bank")
            
        if answer.lower() == "help roll dice":
            print("This command is used for rolling a dice to test your luck and win some points")
            
        if answer.lower() == "help bank status":
            print("This command is used to show you how much money you have in your wallet and bank")
            
        if answer.lower() == "help check real life":
            print("This command is used to see what year, month, day and time it is")
            
        if answer.lower() == "help reset":
            print("This command is used for reseting your current game")
            
    except:
        print("There was an error, please try again")
        
