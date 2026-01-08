# #Subscripting strings
# print("Hello"[0])
# print("Hello"[-1])

# #Strings
# print("123"+"456")
# #Integes
# print(123+456)
# #float 
# print(123.0+456.0)

# #Boolean
# print(True)
# print(False)
# print(True+False)


# print(type("Hello"))
# print(type(123))
# print(type(3.14))
# print(type(True))

# #Typeconversion/Typecasting
# print(int("123")+int("456"))

# name_of_city=input("Enter the name of the city:")
# length_of_city=len(name_of_city)
# print(type(name_of_city))
# print(type(length_of_city))
# print("name_of_city:"+str(length_of_city))

# #priority of Operator=PEMDAS
# print(6/3) # implicit Typecasting
# print(5//3)
# print(2**3)
# print(3*3/3-3)

# #BMI Calculator
# height = 1.65 
# weight = 84
# bmi=84/(1.65**2)
# print(bmi)
# print(int(bmi))
# print(round(bmi)) #rounding into integer
# print(round(bmi,2)) #rounding into 2 decimal places

# #f-strings
# score=0
# height=28.8
# Winner=True

# score+=1
# print(score)

# print("your score is" +str(score))
# print(f"your score is= {score}")
# print(f"Your is:{score}, Your height is {height}, You are the winner is:{Winner}")


#Building a tip Calculator
print("Welcome to the tip calculator!")
bill=float(input("Enter the total bill that you have spendt in the restaurant:"))
tip_percentage=int(input("Enter the percentage like(15%,20%)or enter a custom one"))
number_of_people=int(input("Enter the number of people to split the bill:"))
total_bill=(bill+(bill*tip_percentage/100))/number_of_people
final_amount="{:.2f}".format(total_bill)
print(f"Each person should pay: ${final_amount}")

