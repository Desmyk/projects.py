import random

# Function to roll a dice with values between 1 and 6
def roll_dice():
    return random.randint(1, 6)

# Function to move the player to a new position based on the rolled value
def move_player(player, value, squares, player_positions):
    # Calculate the new position by taking the modulus of the length of the squares list to loop back to the start of the board
    new_position = (player_positions[player] + value) % len(squares)
    
    # Print the rolled value and the new position
    print(f"{player} rolled a {value} and moved to square {new_position}.")
    
    # Return the new position
    return new_position

# Function to check for snakes or ladders and move the player accordingly
def check_for_snake_or_ladder(square, snakes_and_ladders, player):
    # Check if the current square is a key in the snakes_and_ladders dictionary
    if square in snakes_and_ladders:
        # If it is, move the player to the value associated with the square key
        print(f"{player} landed on a snake or ladder!")
        return snakes_and_ladders[square]
    
    # If not, return the current square
    return square

# Function to play the Snakes and Ladders game with the given number of players
def play_game(squares, snakes_and_ladders, num_players):
    # Initialize a list of positions for all players, starting at square 0
    player_positions = [0] * num_players
    player = 0
    
    # Game loop
    while True:
        # Roll the dice for the current player
        rolled_value = roll_dice()
        
        # move player to new position
        player_positions[player] = move_player(player, rolled_value, squares, player_positions)
        
        # Check for snakes or ladders at the new position
        player_positions[player] = check_for_snake_or_ladder(player_positions[player], snakes_and_ladders, player)
        
        # Check if the current player has won the game
        if player_positions[player] >= len(squares) - 1:
            # Print a message indicating that the player has won
            print(f"{player + 1} has won the game!")
            # Break the game loop
            break
        
        # Move to the next player
        player = (player + 1) % num_players

# Define the squares on the board
squares = [i for i in range(100)]

# Define the snakes and ladders on the board
snakes_and_ladders = {
    1: 10,
    4: 14,
    9: 21,
    25: 5,
    36: 44,
    51: 67,
    71: 91,
    80: 11,
    98: 78
}

# Get the number of players from the user
num_players = int(input("Enter the number of players: "))

# Call the play_game function to start the game
play_game(squares, snakes_and_ladders, num_players)