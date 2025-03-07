vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"


# Varianta 1
def elimina_vocala(ch):
    return ch not in vocale
print("".join((filter(elimina_vocala, input_string))))

# Varianta 2 
print("".join((filter(lambda x: x not in vocale , input_string))))

# Varianta 3 - list comprehention
print("".join([ch for ch in input_string if ch not in vocale]))