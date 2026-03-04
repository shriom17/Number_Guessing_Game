import random

def genrate_random_number():
    return random.randint(1, 100)
def check_guess(guess, number):
    if guess < number:
        return "Chhoto Vai"
    elif guess > number:
        return "Areh Beshi Boro Hoye Gelo Toh"
    else:
        return "Sabas Vai, Buke Ay"