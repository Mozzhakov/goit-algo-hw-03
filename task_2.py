# Second task

import random

def get_numbers_ticket(min, max, quantity):
    if not min >= 1 or not max < 1000:
        return []
    
    num_list = []

    for i in range(min, max):
        num_list.append(i)
    
    if quantity <= len(num_list):
        random_nums = random.sample(num_list, quantity)
        random_nums.sort()
        return random_nums 
    else:
        return [] 

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

