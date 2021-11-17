import random

gameoptions=["p", "s", "r"]
computer_choice = random.choice(gameoptions)
user_choice = input("(P)aper, (S)cissors, or (R)ock? Your choice!")

if (user_choice == computer_choice):
    print("It's a tie!")
elif (user_choice=="p" and computer_choice=="r"):
    print("Paper beats rock! You win!")
elif (user_choice=="p" and computer_choice=="s"):
    print("Scissors beats paper! You lose :(")
elif (user_choice=="r" and computer_choice=="s"):
    print("Rock beats scissors! You win!")
elif (user_choice=="r" and computer_choice=="p"):
    print("Paper beats rock! You lose :(")
elif (user_choice=="s" and computer_choice=="p"):
    print("Scissors beats paper! You win!")
elif (user_choice=="s" and computer_choice=="r"):
    print("Rock beats scissors! You lose :(")
else:
    print("I don't understand that input!")
    print("Next time choose from either (p)aper, (s)cissors or (r)ock!")
