#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")
username = input("Username:")
print("Username is: " + username)


Move = input("Your choise:")
print("You chose: " + Move)
import random
result=str(random.randint(1, 3))
print("computer chose" + result)

if Move == result:
    print("draw")
elif Move == ROCK and result == SCISSOR:
    print("you won")
elif Move == SCISSOR and result == PAPER:
    print("you won")   
elif Move == PAPER and result == ROCK:
    print("you won")
elif Move == ROCK and result == PAPER:
    print("you lost") 
elif Move == PAPER and result == SCISSOR:
    print("you lost")   
elif Move == SCISSOR and result == ROCK:
    print("you lost")                          
