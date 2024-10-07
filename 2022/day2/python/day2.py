# mappings for opponent and your moves
opponent_moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
your_moves = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

# the score for the shape you selected
shape_score = {'Rock' : 1, 'Paper': 2, 'Scissors': 3}

def calculate(opponent, you):

    opponent_shape = opponent_moves[opponent]
    your_shape = your_moves[you]

    score = shape_score[your_shape]

    if opponent_shape == your_shape:
        score += 3
    elif (opponent_shape == 'Rock' and your_shape == 'Paper') or \
        (opponent_shape == 'Paper' and your_shape == 'Scissors') or \
        (opponent_shape == 'Scissors' and your_shape == 'Rock'):
        score += 6
    else:
        score += 0

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
