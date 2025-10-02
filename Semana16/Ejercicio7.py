def alphabetics_words (j):
    words = j.split("-")
    ordered_words  = sorted(words, key=str.lower)
    result = "-".join(ordered_words)
    return result


result = alphabetics_words("python-variable-funcion-computadora-monitor")
print(result)