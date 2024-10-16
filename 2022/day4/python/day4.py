#checking assignments for each pair of elf
def check_assignments(assignments1, assignments2):
    
    start1, end1 = assignments1
    start2, end2 = assignments2

    if start1 <= start2 and end1 >= end2:
        return True
    if start2 <= start1 and end2 >= end1:
        return True
    
    return False

# Check if the two assignment ranges overlap
def assignments_overlap(assignments1, assignments2):

    start1, end1 = assignments1
    start2, end2 = assignments2 

    if start1 <= end2 and end1 >= start2:
        return True

    return False


def assignment_pairs(file_name):

    count = 0
    count2 = 0

    with open(file_name, 'r') as file:
        
        for line in file:
            pair = line.strip().split(',')
            
            # Convert each Elf's assignment range to a tuple of integers (start, end)
            assignments1 = tuple(map(int, pair[0].split('-')))
            assignments2 = tuple(map(int, pair[1].split('-')))

            # Check if one Elf's assignment fully contains the other
            if check_assignments(assignments1, assignments2):
                count += 1

            # Check if the two Elves' assignments overlap
            if assignments_overlap(assignments1, assignments2):
                count2 += 1

    print(f"Number of assignment pairs where one fully contains the other: {count}")

    print(f"Number of assignment pairs that overlap: {count2}")



assignment_pairs('input.txt')
