# fin a prime number

import os
os.system("cls")

# inversor -----------------------------
def inversor(num):
    return int(str(num)[::-1])

# palindromo ---------------------------
def palin(n):
    if n == inversor(n):
        print("TRUE pal")
    else:
        print("False pal")

# prime ---------------------------------
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# pasando valores
n = inversor(2001)
palin(n)
# agregando print a los Trues and Falses ---
if prime(n):
    print(f"{n} Es primo")
else:
    print(f"{n} nope")

#invirtiendo again
n = int(str(n)[::-1])
print(n)
# --------------------------------------



