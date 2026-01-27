# programming_dictionary = {
#     "Bug": "An error in a program that programs from runnig as expected",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again"
# }
# print(programming_dictionary["Bug"])
# programming_dictionary["ashish"] = "He is a very good boy according to the girls"
# print(programming_dictionary)
# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)

# # Loop through a dictionary
# for thing in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])







# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"

# }

# # Nested Lis in Dictionary
# # travel_log = {
# #     "France": ["Paris","Lille","Dijon"],
# #     "Germany": ["Delhi","Mumbai","Patna"]
# # }
#  # print Lille
# # print(travel_log["France"][1])

# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])


# travel_log = {
#     "France": {
#         "cities_visited": ["Paris","lille","Dijon"],
#         "total_visits":12
#     },
#     "Germany": {
#     "cities_visited": ["Delhi","Mumbai","Patna"],
#     "total_visits":5
#     },
# }

# print(travel_log["Germany"]["cities_visited"])





# Secret Auction Program
# TODO-1: Ask the user for input.
# TODO-2: Save data into dictionary {name:price}
# TODO-3: Wheather if new  bids need to be added
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?:")
    price = int(input("What is your bid?:$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or No. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n " *20)


# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"THe winner is {winner} with a bid of $ {highest_bid}")