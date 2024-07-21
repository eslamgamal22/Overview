import random
import string
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print ("welcome to our samble game \n")
words = ["hello","cat","football","milk"]
random_word = random.choice(words)
# اعرض ممسافات بنفس عدد حروف الكلمه 
display = ["_"] * len(random_word) # المسافات بتتحفظ فى قائمه بنفس عدد حروف الكلمه
print(" ".join(display)) # بين كل شرطه مسافه

print(hangman_stages[0])
lives = 6
guessed_letter = []
#اطلب تخمين حرف 
while "_" in display and lives > 0 : #طالما فى شرطه ف اللعبه يبقى لسه مخلصتش  
    guessed = input ("\nplease enter a letter : ").lower() 
    # بنشوف اختار الحرف قبل كده
    if guessed in guessed_letter :
         print("you alresdy guessed that letter ")
         print(f"you have {lives} more tries ")
         continue
    guessed_letter.append(guessed)

    if guessed not in random_word :
         lives -= 1
         print(hangman_stages[6 - lives])

    for position in range(len(random_word) ):
        if random_word[position] == guessed :
            display[position] = guessed
    
    print(" ".join(display))
    print(f"\nyou have {lives} more tries")


if lives == 0 :
    print("""
           ***** 
          YOU LOSS
           *****
         """)   
    print(hangman_stages[-1])
else:
    print("""
         ********
          YOU WIN
         ******** 
   
         """)     