number_list = [5, 3, 8, 4, 2]
n = len(number_list)
limit = n - 1
swapped = True

while swapped and limit >= 1:
    swapped = False

    for i in range(limit, 0, -1):
        if number_list[i] < number_list[i - 1]:
            number_list[i], number_list[i - 1] = number_list[i - 1], number_list[i]
            swapped = True
    limit -=1

print(f"Lista ordenada:{number_list}")