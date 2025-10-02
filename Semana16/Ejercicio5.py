def vuelta():
    my_string = 'hola mundo'
    reversed_str = ''
    for char in range(len(my_string)-1, -1, -1):
        reversed_str += my_string[char]
    return reversed_str


vuelta()