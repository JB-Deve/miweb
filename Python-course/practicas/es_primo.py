# fin a prime number

import os
os.system("cls")

# generar numeros -------------------------
#nesecito crear un alamcen
def generador_numeros(n, n_max):
    return list(range(n, n_max))

# verificar: is prime? --------------------
def es_prime(n):
    """ Prime Checker"""
    # there is no '1 or -n primes'
    if n <= 1:
        return False

    #for i in range(2, n): # 'n' verifica todos lo valores
    for i in range(2, int(n**0.5) + 1): # ** filtra los numbers a comprobar
        if n % i == 0:
            return False
    return True

# verificar: es palindrome ----------------
def is_palindrome(num):
    """ Palindrome Comparator """
    return num == int(str(num)[::-1])

# skip line 10 by 10 ----------------------
def salto_linea(lista):
    """ Line Skipper"""
    for i, num in enumerate(lista):

        print(f"{num:>4}", end=" ")
        if (i + 1) % 10 == 0:
            print()

# callers ---------------------------------
# generamos los numeros
rango_numeros = generador_numeros(0, 1000)

# filtramos los numeros primos
primos = [num for num in rango_numeros if es_prime(num)]

# filtramos: 'primo & palindrome'
primos_palindromos = [num for num in primos if is_palindrome(num)]

# imprimimos 'primo & palindrome' con el salto de linea cada 10 elem
salto_linea(primos_palindromos)
