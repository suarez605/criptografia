import sys

"""Test de Kullback (fi-test)
    Autor: Alvaro Esteban Suarez Lozano (@suarez605)
    Test usado para estudiar la distribucion de frecuencias de un texto para 
    contrastar en funcion de ellas si se trata de un posible criptograma en 
    lenguaje natural o si es una secuencia aleatoria de simbolos.

"""

dicc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

texto = sys.argv[1]

a = {}
for elem in dicc:
    conteo = texto.count(elem)
    a[elem] = (conteo, conteo-1)


print(f"Longitud texto: {len(texto)}")
print("Elementos")
N=0
sum_f_i=0
for elem in a.keys():
    print(f"{elem}: {a[elem]}")
    N += a[elem][0]
    sum_f_i += (a[elem][0]*a[elem][1])

print(f"N: {N}")
print(f"N(N-1)={N*(N-1)}")
fi_r = N*(N-1)*0.0385
print(f"fi_r = {fi_r}")
fi_p = N*(N-1)*0.0667
print(f"fi_p = {fi_r}")
print(f"fi-exp = {sum_f_i}")
print("-------------------------RESULTADOS------------------------------------")
print(f"La distancia entre fi_p y sum_f_i es {abs(fi_p - sum_f_i)}")
print(f"La distancia entre fi_r y sum_f_i es {abs(fi_r - sum_f_i)}")
if abs(fi_p - sum_f_i) < abs(fi_r - sum_f_i):
    print("Los resultados nos indican que hay mas opciones de estar ante un texto escrito en lenguaje natural.")
elif abs(fi_p - sum_f_i) > abs(fi_r - sum_f_i):
    print("Los resultados nos indican que hay mas opciones de estar frente a una secuencia aleatoria o una sustitucion simple.")
else:
    print("Los resultados no apoyan ni una hipotesis de estar frente a una secuencia aleatoria o una sustitucion simple ni ante un lenguaje natural")
    

