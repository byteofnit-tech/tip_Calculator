# import random
# import my_module
# random_intger=random.randint(1,10)
# print(random_intger)
# print(my_module.my_favourite_number)

# import random
# random_number_0_to_1=random.random() * 10
# print(random_number_0_to_1)

# random_float=random.uniform(1,10)
# print(random_float)


# #Print Heads or Tails
# import random
# random_heads_or_tails=random.randint(0,1)
# if random_heads_or_tails==1:
#     print("Heads")
# else:
#     print("Tails")


# #Lists in Python
# states_of_america=["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# print(states_of_america[0])
# states_of_america[1]="Pencilvania"
# states_of_america.append("Virgina")
# print(states_of_america)

# #Project: Who will pay the bill?
# import random
# friends=["Angela", "Bob", "Caroline", "Dave", "Eleanor", "Frank"]

# print(random.choice(friends))
# #or
# random_index=random.randint(0,4)
# print(friends[random_index])


# states_of_america=["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# print(len(states_of_america))

# num_of_states=len(states_of_america)
# print(num_of_states)




# # dirty_dozen=["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits=["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables=["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen=[fruits,vegetables]
# print(dirty_dozen[1][1])
# print(dirty_dozen)
# print(dirty_dozen[0][0])


#Project: Rock, Paper, Scissors
import random
print("Welcome to Rock, Paper, Scissors")
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice=random.randint(0,2)
print(f"computer choice: {computer_choice}")
# if user_choice==0 and computer_choice==2:
#     print("You win!")
# elif user_choice==0 and computer_choice==1:
#     print("You lose!")
# elif user_choice==1 and computer_choice==0:
#     print("You win!")
# elif user_choice==1 and computer_choice==2:
#     print("You lose!")
# elif user_choice==2 and computer_choice==0:
#     print("You lose!")
# elif user_choice==2 and computer_choice==1:
#     print("You win!")
if user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice>user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")   
elif user_choice > computer_choice:
    print("You win!")           
else:
    print("You typed an invalid number, you lose!")     