# #For Loop
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)


# student_scores = [150,142, 133, 124, 115, 106, 97, 88, 79, 70]
# total_exam_score=sum(student_scores)
# sum=0
# for score in student_scores:
#     sum+=score
#     print(sum)


# student_scores = [150,142, 133, 124, 115, 106, 97, 88, 79, 70]
# max_score=0
# for score in student_scores:
#     if score>max_score:
#         max_score=score
# print(f"The highest score in the class is: {max_score}")



# # Range Function
# sum=0
# for number in range(1,101):
#     sum+=number
#     print(sum)
 
# # You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# # Your program should print each number from 1 to 100 in turn and include number 100.
# # But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# # When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# # And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)


# Password Generator
print("Welcome to the PyPassword Generator!")
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
lr_input=int(input("How many letters would you like in your password?\n"))
nr_input=int(input("How many numbers would you like in your password?\n"))
sr_input=int(input("How many symbols would you like in your password?\n"))

# #Easy level password
# password=""
# for char in range(1, lr_input + 1):
#     random_char=random.choice(letters)
#     print(random_char)
#     password+=random_char
#     print(password)  
     

# #In single line
# password=""
# for char in range(0, nr_input):
#     password+=random.choice(numbers)
# for char in range(0, sr_input):
#     password+=random.choice(symbols)
# for char in range(0, lr_input):
#     password+=random.choice(letters)
# print(password)
    

# #Hard Level Password

password_list=[]
for char in range(0, nr_input):
    password_list.append(random.choice(numbers))
for char in range(0, sr_input):
    password_list.append(random.choice(symbols))
for char in range(0, lr_input):
    password_list.append(random.choice(letters))
print(password_list)
random.shuffle(password_list)
print(password_list)
    
password =""
for char in password_list:
    password+=char
print(f"Your password is: {password}")