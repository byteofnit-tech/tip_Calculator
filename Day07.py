word_list = ["apple", "banana", "cherry", "date", "elderberry"]
import random
random_word = random.choice(word_list)
print("Randomly selected word:", random_word)

placeholder = ""
for position in range(len(random_word)):
    placeholder+="_"
    print(placeholder)
guess = input("Guess a letter:").lower()
print("You guessed:", guess)
for letter in random_word:
   if letter == guess:
    print("Correct")
   else:
    print("Incorrect")

