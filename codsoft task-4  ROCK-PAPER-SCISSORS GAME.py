import random

def get_human_choice():
    while True:
        human_input = input("Choose rock, paper, or scissors: ").lower()
        if human_input in ("rock", "paper", "scissors"):
            return human_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(human_choice, computer_choice):
    if human_choice == computer_choice:
        return "It's a tie!"
    elif (human_choice == "rock" and computer_choice == "scissors") or\
         (human_choice == "paper" and computer_choice == "rock") or \
         (human_choice == "scissors" and computer_choice == "paper"):
        return "You win the game!"
    else:
        return "Computer wins the game!"

while True:
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {human_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(human_choice, computer_choice)
    print(result)

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        break
