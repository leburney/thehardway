def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# calls the function with argument value of 20 and 30
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# call the function with arguments set to the variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# calls the function with the arguments "10+20" and "5+6"
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# calls the function  with the arguments math and variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
