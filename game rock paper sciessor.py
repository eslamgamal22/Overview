import random

rock = "🪨"
paper = "📄"
sciessor = "✂️"
print("Welcom to the '🪨📄✂️' Game ")
confirm = input(
  "press enter to continue or type 'help' to go to help rule: ").lower()
if confirm == "help":
  print("""
         ******** RULES ********
         1) Your choose and the computer choose
         2) rock smashes sciessor => rock Win
         3) sciessor cut paper => sciessor Win
         4) paper cover rock => paper Win    

         """)

#user_choise
user_chooise = input("chooise 'rock or paper or sciessor ' ").lower()

if user_chooise not in ["rock","paper","sciessor"] :
  print("try agin ")
else:  
  if user_chooise == "rock":
     print(f"you chooise {rock}")
  elif user_chooise == "paper":
     print(f"you chooise {paper}")
  else:
     print(f"you chooise {sciessor}")

#computer_choise

computer_chooise = random.choice(["rock","paper","sciessor"]).lower()

if computer_chooise == "rock":
     print(f"computer chooise {rock}")
elif computer_chooise == "paper":
     print(f"computer chooise {paper}")
else:
     print(f"computer chooise {sciessor}")


#Game condition

if computer_chooise == user_chooise:
  print("the same chooise 0 0")

elif ((user_chooise == "rock" and computer_chooise == "sciessor")
       or
      (user_chooise == "paper" and computer_chooise == "rock")
       or
      (user_chooise == "sciessor" and computer_chooise == "paper")):
  print("user Win")
else:
  print("computer Win")     