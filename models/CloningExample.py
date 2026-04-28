
a = [1,3,5,7]

# b = a # b es una referencia a a

# Clonamos la lista a
b = a[:] # Clonamos la lista a

b[0] = 15

print( "resultado de a: ", a)
print( "resultado de b: ", b)
  

  

# EJEMPLO DE REMOVER ELEMENTO DE UNA LISTA Y CALCULAR EL PRODUCTO DE LOS ELEMENTOS 

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
def remove_elem(data, target):
    new_data = data.copy()
    for item in data:
        if item == target:
            new_data.remove(target)
            return new_data


def get_product(data):
    new_data = data.copy()
    total = 1
    for i in range(len(new_data)):
        total *= new_data.pop()
        return total


c = remove_elem(c, 3)
print(get_product(b))
print(a)