import random
choice=["rock", "Paper","scissors"]

def winner(player_choice, computer_choice):
    if player_choice== computer_choice:
        return ("It's a tie")
    elif (player_choice == "rock" and computer_choice =="scissors") or \
         (player_choice == "paper" and computer_choice=="scissors") or \
         (player_choice == "scissors" and computer_choice =="paper"):
        return ("You Win")
    else:
        return("You loose")
    
while True:
    player_choice=input("\n choose rock, paper or scissors (or type 'exit' to exit):\n")
    player_choice=player_choice.lower()
    if player_choice== 'exit':
        print("BYE!")
        break

    if player_choice not in choice:
        print("Invalid choice")
        continue


    computer_choice= random.choice(choice)
    print(f"Computer's choice is {computer_choice}")

    result= winner(player_choice, computer_choice)
    print(result)
