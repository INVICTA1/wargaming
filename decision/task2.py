from random import randint
def search_big_number():
    mass = [randint(1,10**5) for i in range(9)]
    print(mass)
    mass_sorted = sorted(mass)
    print(mass_sorted)
