# HANGMAN GAME #
import random
word_list= ["mia", "ava", "jonny", "riley", "angelina", "ryan"]

choosen_word= random.choice(word_list)



display=[]

for letter in range(len(choosen_word)):
    display.append("_")
print("No of words: ")
print(display)
end= False
n=6 #number of lives
while not end:
    guess_input=input("Enter your guess alphabet").lower()
    for letter in range(len(choosen_word)):
        if choosen_word[letter]==guess_input:
            display[letter]= choosen_word[letter]
    
    print(display)   

    
   
    if guess_input not in choosen_word:
        n=n-1
        print("Lives" + str(n))  
        
    if "_" not in display:
        end= True
        print("Good work Chaamppppp")
    elif n==0:
        end= True
        print("Game Over")

print(f"The word is:  {choosen_word}")
       
 