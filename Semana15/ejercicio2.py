def bubble_sort_reverse(numbers, in_place=True):
    
    if not in_place:
        numbers = numbers[:]

    n = len(numbers)
    limit = n - 1
    swapped = True


    while swapped and limit >= 1:
        swapped = False
        for i in range(limit, 0, -1):
            if numbers[i] < numbers[i - 1]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                swapped = True
        limit -= 1

    return numbers


#       pruebas

print("Lista vacía:", bubble_sort_reverse([]))
print("Un elemento:", bubble_sort_reverse([42]))
print("Ya ordenada:", bubble_sort_reverse([1, 2, 3, 4]))
print("Invertida:", bubble_sort_reverse([4, 3, 2, 1]))
print("Con repetidos:", bubble_sort_reverse([3, 1, 2, 1, 3]))

# Probar in-place y copia

original = [5, 3, 8, 4, 2]
print("Ordenada in-place:", bubble_sort_reverse(original))
print("Original después:", original)

orig2 = [5, 3, 8, 4, 2]
print("Ordenada copia:", bubble_sort_reverse(orig2, in_place=False))
print("Orig2 sigue igual:", orig2)

