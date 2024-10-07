def highest_sum(file_name):
    highest = 0 #to store the highest sum of calories
    current = 0 #to store the current sum of calories for current elf

    with open(file_name, 'r') as file:
        for line in file:
            stripped_line = line.strip() 

            if stripped_line == "": #check if line is empty, indicating new elf
                if current > highest:
                    highest = current
                current = 0

            else:
                current += int(stripped_line)

        if current > highest:
            highest = current

    print(f"The highest sum is: {highest}")

def three_highest_sum(file_name):
    elves_list = [] #to store the sum of calories for each elf
    current = 0 #to the current sum of calories for current elf

    with open(file_name, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            
            if stripped_line == "": #check if line is empty, indicating new elf
                elves_list.append(current) 
                current = 0;
            else:
                current += int(stripped_line)

        elves_list.append(current)

    elves_list.sort(reverse=True) #sort list in descending order

    sum_of_top_three = sum(elves_list[:3]) #sum of the top three elves in the list

    print(f"The sum of the top 3 elves is: {sum_of_top_three}")
                

highest_sum('input.txt')
three_highest_sum('input.txt')
        
        
