rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Starting room
current_room = 'Great Hall'

while True:
    print(f"\nYou are currently in the {current_room}")

    # List available directions
    available_directions = rooms.get(current_room, {})
    print(f"Available directions: {', '.join(available_directions.keys())}")

    # Get user input for direction or exit
    user_input = input("Select where you would like to go or type 'exit' to quit: ").capitalize()

    # If user chooses to exit
    if user_input == 'Exit':
        current_room = 'Exit'
        print("You have exited the game.")
        break

    # Move to the next room if the direction is valid
    elif user_input in available_directions:
        current_room = available_directions[user_input]
    else:
        print("Invalid direction! Please choose a valid direction or type 'exit'.")
