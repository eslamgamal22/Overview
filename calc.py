import random
print("Welcome to 'whose wallet?'")
names_str = input("You will give me a list of names , and i will pick a person to pay \n").split(", ")
pick = random.choice(names_str)
print("ask ",pick, "to pay dinnner")
