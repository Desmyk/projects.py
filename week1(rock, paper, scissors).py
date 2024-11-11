import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_round():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    result = compare_choices(user_choice, computer_choice)
    if result == 'draw':
        print("It's a draw!")
    elif result == 'user':
        print("You win!")
    else:
        print("You lose.")

def play_game():
    while True:
        print("\nNew round!")
        play_round()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
    
    
