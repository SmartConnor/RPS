# checks for an integer more than 0 (allow <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 1. "

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts here

# Intialse game variables
mode = "regular"
rounds_played = 0

print(" Rock / Paper / Scissors")
print()

# instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n☻☻☻ Round {rounds_played + 1} (Infinite Mode) ☻☻☻"
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

        print(rounds_heading)
        print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area