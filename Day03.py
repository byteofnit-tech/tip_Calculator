# #rollercoaster height check
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height >=120:
#     print("you can ride the rollercoaster!")
# else:
#     print("You cannnot ride the rollercoaster!")


# number_to_check=int(input("What is the number you want to check?"))
# if number_to_check %2==0:
#     print("The number is even number")
# else:
#     print("The number is odd number")



# #Neseted if-else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height >=120:
#     print("you can ride the rollercoaster!")
#     age=int(input("What is your age?"))
#     if age<12:
#         print("Your ticket price is $5")
#     elif 12<=age<=16:
#         print("Your ticket price is $7")
#     elif age>16 and age<=18:
#         print("your ticket price is $8")
#     else:
#         print("Your ticket price is $12")
# else:
#     print("You cannnot ride the rollercoaster!")




# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# if height >=120:
#     print("you can ride the rollercoaster!")
#     age=int(input("What is your age?"))
#     if age<12:
#         bill=5
#         print("Child ticket price is $5")
#     elif 12<=age<=18:
#         bill=7
#         print("Youth ticket price is $7")
#     elif age>=45 and age<=55:
#         bill=0
#         print("Middle age people tickets is free")
#     else:
#         bill=12
#         print("adult ticket price is $12")
#     wants_photo=input("DO you want a photo taken? Y or N.")
#     if wants_photo=="Y":
#         bill+=3
#     print(f"tour == final bill is ${bill}")
# else:
#     print("You cannnot ride the rollercoaster!")




# #Python Pizza Deliveries
# print("Welcome to Python pizza delivery service!")
# bill=0
# size=input("What size of pizza do you want? S, M, or L:")
# if size=="S":
#     price=15
#     print(price)
# elif size=="M":
#     price=20
#     print(price)
# else:
#     price=25
#     print(price)
# pepperoni=input("Do you want pepporoni? Y or N:")
# if pepperoni=="Y":
#     if size=="S":
#         price+=2
#     elif size=="M":
#         price+=3
#     else:
#         price+=4
# extra_cheese=input("Do you want extra cheese? Y or N:")
# if extra_cheese=="Y":
#     price+=1
# print(f"Your final bill is: ${price}")




#Today's Project:Treasure Island
print("Welcomme to the Treasure Island.You mission is to find the treasure.")
choice1=input('You\'re at a cross road. Where do you want to go? Type "left" or "right": ')
if choice1=="left":
    print("Game Over")
elif choice1=="right":
    choice2=input('You\'ve come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat.Type "swim" to swim across:')
    if choice2=="swim":
        print("Game Over")
    elif choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.Which coloue do you wanna to choose?")
        if choice3=="blue":
            print("Game Over,You enter a room of beasts.Khel khatama Tata Bye Bye")
        elif choice3=="red":
            print("Game Over,You enter a room of fire. Khel khatama Tata Bye Bye")
        elif choice3=="yellow":
            print("Congratualations! You found the treasure! You Win!")

