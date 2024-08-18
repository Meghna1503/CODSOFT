import random
Symbols=["R","P","S"]
User_choice = str(input("R for Rock,P for Paper,S for Scissor\n"
                        "Enter your choice: "))
Computer_choice=random.choice(Symbols)
print("Computer chose:",Computer_choice)
if Computer_choice==User_choice:
    print("The match is draw ")
elif Computer_choice=="P" and User_choice=="S":
    print("You Win || System Lose")
elif User_choice=="P" and Computer_choice=="S":
    print("System Win || You lose")
elif Computer_choice=="R" and User_choice=="S":
    print("System Win || You lose")
elif User_choice=="R" and Computer_choice=="S":
    print("You Win || System Lose")
elif Computer_choice == "R" and User_choice == "P":
    print("You Win || System Lose")
elif User_choice == "R" and Computer_choice == "P":
    print("System Win || You Lose")
else:
    print("Invalid Choice")
play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
if play_again != 'yes':
    print("Thanks for playing!")





