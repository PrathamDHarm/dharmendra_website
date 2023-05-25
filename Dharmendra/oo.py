# # year=int(input())

# # if (year%4==0):
# #     #print("leap")
# #     if (year%100==0):
# #         #print("not")
# #         if (year % 400 ==0):
# #             print("leap")
# #         else:
# #             print("not")
# #     else:
# #         print("leap")
# # else:
# #     print("not")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill=0
# if size== "S":
#     bill=bill+15
#     if add_pepperoni=="Y":
#         bill+=2
# elif size=="M":
#     bill=bill+20
#     if add_pepperoni=="Y":
#         bill+=3
# elif size =="L":
#     bill=bill+25
#     if add_pepperoni=="Y":
#         bill=bill+3

# print(bill)

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# n1=name1.upper()
# n2=name2.upper()

# x=n1.count("L") + n2.count("L")
# y=n1.count("O") + n2.count("O")
# a=n1.count("V") + n2.count("V")
# z=n1.count("E") + n2.count("E")
# # print(f"L occurs {x} times")
# # print(f"O occurs {y} times")
# # print(f"V occurs {a} times")
# # print(f"E occurs {z} times")
# total =x + y+a+z
# # print("Total =",total)

# x=n1.count("T") + n2.count("T")
# y=n1.count("R") + n2.count("R")
# a=n1.count("U") + n2.count("U")
# z=n1.count("E") + n2.count("E")
# # print(f"L occurs {x} times")
# # print(f"O occurs {y} times")
# # print(f"V occurs {a} times")
# # print(f"E occurs {z} times")
# total1 =x + y+a+z
# # print("Total: ",total1)
# q=str(total1)+str(total)
# d=int(q)

# if d<10 or d>90:
#     print(f"Your score is {q}, you are like coke and mentos.")
# elif d>40 and d<50:
#     print(f"Your score is {q}, you are alright together.") 
# else:
#     print(f"Your score is {q}")

# import random

# x= random.randint(0,1)
# print(x)
# if x==0:
#     print("tails")
# else:
#     print("heads")

# from random import sample

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# x=sample(names, 1)
# print()

# import random

# def game(c,d):
#     if c=="R" and d=="S":
#         print("pLAYER1 WON ")
#     elif c=="S" and d=="P":
#         print("player1 won")
#     elif c=="P" and d=="R":
#         print("player1 won")
#     elif c==d:
#         print("draw")
#     if d=="R" and c=="S":
#         print("pLAYER2 WON ")
#     elif d=="S" and c=="P":
#         print("player2 won")
#     elif d=="P" and c=="R":
#         print("player2 won")

# print("ROCK=r/R, SCISSOR=s/S, PAPER=p/P  ")
# while True:

#     a=input("Player1 Input: ")
#     c=a.upper()
#     b=["R","S","P"]
#     d= random.choice(b)
#     if c=="R":
#         print("player1: ",c)
#         print("player2: ",d)
        
#     elif c=="P":
#         print("player1: ",c)
#         print("player2: ",d)
        
#     elif c=="S":
#         print("player1: ",c)
#         print("player2: ",d)
        
#     else:
#         print("Error input")
#     game(c,d)
#     print("---")

# import numpy as np
# s=0
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   s=int(s)+student_heights[n]
# a=s/np.size(student_heights)
# print(round(a))

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# student_scores.sort()
# print("The highest score in the class is: "+str(student_scores[n]))

# s=0
# for i in range (1,100):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#        print("fizz")
#     elif i%5==0:
#         print("Buzz")
    
#     else:
#         print(i)

# def prime_checker(number):
#     if number>1:
#         for i in range  (2, int(number/2)+1):
            
#             if number%i==0:
#                 print("It's not a prime number")
#                 break
#         else:
#                 print("It's a prime number")
# n = int(input("Check this number: "))
# prime_checker(number=n)


# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country, visits, cities):
#     new_country = {
#       "country": country,
#       "visits": visits,
#       "cities": cities
#     }
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

a=input("choose any of these direction RIGHT or LEFT: ")
a.lower()
if a=="left":
    b=input("choose any of these motion swim or wait: ")
    b.lower()
    if b=="wait":
        print("which color door would like u 2 choose ")
        c=input("choose any of these color Red or Blue or Yellow or anyother color: ")
        c.lower()
        if c=="red":
            print("burned by fire")
        elif c=="blue":
            print("eaten by beasts")
        elif c=="yellow":
            print("You win!")
        else:
            print("GAME OVER! ")
    elif b=="swim":
        print("Eaten by trout GAME OVER! ")
    else:
        print("Eaten by trout GAME OVER! ")
elif a=="RIGHT":
    print("Fall into a hole GAME OVER! ")
else:
    print("Fall into a hole GAME OVER! ")