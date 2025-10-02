def bubble_sort(numbers, in_place=True):

    if not in_place:
        numbers = numbers[:]

    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break

    return numbers


#        pruebas 

print("Lista vacía:", bubble_sort([]))
print("Un elemento:", bubble_sort([42]))
print("Ya ordenada:", bubble_sort([1, 2, 3, 4]))
print("Invertida:", bubble_sort([4, 3, 2, 1]))
print("Con repetidos:", bubble_sort([3, 1, 2, 1, 3]))

# Probando in_place y copia

# modifica la original
original = [5, 3, 8, 4, 2]
print("Ordenada (in-place):", bubble_sort(original))  
print("Original después:", original)

# no modifica
orig2 = [5, 3, 8, 4, 2]
print("Ordenada (copia):", bubble_sort(orig2, in_place=False))  
print("Orig2 sigue igual:", orig2)
