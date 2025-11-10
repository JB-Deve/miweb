# practicando mas

import os
os.system("cls")

###
# Fizz Buzz
###

"""
Escribe un programa que muestre por consola (con un print) los
numeros de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión),
sustituyendolo los siguientes:
- multiplos de 3 por la palabras "fizz"
- multiplos de 5 por la palabra "buzz"
- multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz
"""

# def fizzbuzz():
#     for index in range(1, 101):
#         if index % 3 == 0 and index % 5 == 0:
#             print("fizzbuzz")
#         elif index % 3 == 0:
#             print("fizz")
#         elif index % 5 == 0:
#             print("buzz")
#         else:
#             print(index)

# fizzbuzz()

# ###
# # Es un Anagrama
# ###

# def es_anagrama(word1, word2):
#     if word1.lower() == word2.lower():
#         return False
#     return sorted(word1.lower()) == sorted(word2.lower())

# print(es_anagrama("amor", "roma"))

###
# Fibonacci
###

# def fibonacci():
#     prev = 0
#     next = 1

#     for index in range(0, 15):     
#         print(prev)
#         fib = prev + next
#         prev = next
#         next = fib

# fibonacci()

###
# Primo
###


def is_prime():

    for number in range(1, 101):
            
        if number >= 2:
            #return False
            is_divisible = False
        
            for index in range(2, int(number**0.5) + 1):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)    

is_prime()
