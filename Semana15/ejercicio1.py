number_list = [5, 3, 8, 4, 2]

for i in range(len(number_list)):
    swapped = False
    for n in range (len(number_list) - i - 1):
        if number_list[n] > number_list[n + 1]:
            number_list[n], number_list[n + 1] = number_list[n + 1], number_list[n]
            swapped = True
    if not swapped:
        break

print(f"Lista ordenada: {number_list}")