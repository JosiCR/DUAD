number_list = [5, 3, 8, 4, 2] # O(1)

for i in range(len(number_list)): # O(n)
    swapped = False             # O(1)
    for n in range (len(number_list) - i - 1): # O(n)
        if number_list[n] > number_list[n + 1]:  # O(1)
            number_list[n], number_list[n + 1] = number_list[n + 1], number_list[n]  # O(1)
            swapped = True          # O(1)
    if not swapped:                 # O(1)
        break                       # O(1)

print(f"Lista ordenada: {number_list}") # O(1)