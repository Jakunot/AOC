# mappings for opponent and your moves
opponent_moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}

#scoring outcome depending on opponent moves
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}

# the score for the shape you selected
shape_score = {'Rock' : 1, 'Paper': 2, 'Scissors': 3}

def determine_move(opponent_shape, outcome):

    #lose
    if outcome == 'X':
        if opponent_shape == 'Rock':
            return 'Scissors'
        elif opponent_shape == 'Paper':
            return 'Rock'
        elif opponent_shape == 'Scissors':
            return 'Paper'
    
    #draw
    if outcome == 'Y':
        return opponent_shape

    #win
    if outcome == 'Z':
        if opponent_shape == 'Rock':
            return 'Paper'
        elif opponent_shape == 'Paper':
            return 'Scissors'
        elif opponent_shape == 'Scissors':
            return 'Rock'

def calculate(opponent, outcome):

    #determine opponents move
    opponent_shape = opponent_moves[opponent]

    #determine your move based on opponent move and desired outcome
    your_shape = determine_move(opponent_shape, outcome)

    #base score for the shape you chose
    score = shape_score[your_shape]

    score += outcome_score[outcome]

    return score

def total(file_name):
    total = 0

    with open(file_name, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            # Ensure the line is not empty and has two values
            if stripped_line:
                try:
                    opponent, you = stripped_line.split()
                    total += calculate(opponent, you)
                except ValueError:
                    # This will handle lines that don't split into exactly two values
                    print(f"Ignoring invalid line: {stripped_line}")


    print(f"Your total score is: {total}")

total('input.txt')

