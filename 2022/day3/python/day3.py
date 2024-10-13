
def priority(item):
    
    ''' 
    checks if item is lowercase from 'a' to 'z'
    ord(item) gives ASCII value of character.
    For example: 
        ord('a') - ord('a') + 1 = 
        61 - 61 + 1 = 1 (since in the ASCII table character 61 represents a)
            
    For 'b' it becomes:
        ord('b') - ord('a') + 1 =
        62 - 61 + 1 = 2.
    
    This continues for all lowercase letters, with 'z' having priority of 26
    '''

    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27
    return 0

def sum_priorities(file_name):

    total = 0

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            #split the line into two 
            mid = len(line)//2
            first_compartment = line[:mid]
            second_compartment = line[mid:]

            #to check the common item between each compartment 
            common_items = set(first_compartment).intersection(set(second_compartment))

            if common_items:
                common_item = common_items.pop()
                total += priority(common_item)

    print(f"Total sum of priorities of common item is: {total}")


def badge_priority(file_name):

    total = 0

    with open(file_name, 'r') as file:
        lines = file.readlines()

        
        #iterate through the file in chunks of 3 (rucksack carried by and elf, 3 elves is one group)
        for i in range(0, len(lines), 3):
            # get rucksacks for the current group
            rucksack1 = lines[i].strip()
            rucksack2 = lines[i + 1].strip()
            rucksack3 = lines[i + 2].strip()

            #to check the common items across the 3 rucksacks
            common_items = set(rucksack1).intersection(set(rucksack2), set(rucksack3))

            if common_items:
                common_item = common_items.pop()
                total += priority(common_item)

    print(f"Total sum of badge priorities is: {total}")


badge_priority('input.txt')
sum_priorities('input.txt')
