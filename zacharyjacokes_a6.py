import random

pokemon_type = ['fire', 'electric', 'grass']
pokemon_char = ['cute', 'cool', 'scary']
pokemon = ['Charmander', 'Rapidash', 'Moltres', 'Pikachu', 'Electabuzz', 'Zapdos', 'Bulbasaur', 'Exeggutor', 'Victreebel']



print("Welcome to the beginning of your new Pokemon adventure! Let\'s find out what Pokemon you get to start out with!")

start = str(input("Are you ready to get assigned a Pokemon? (y/n): "))

while True:

    def func1():
        return random.choice(pokemon_type)

    def func2():
        return random.choice(pokemon_char)

    x = func1()
    y = func2()

    if start == 'y':
        print("Your favorite type has been determined to be: " + x + "...")
        print("Your assigned personality characteristic is: " + y + "...")
    else:
        print("Oh. Okay fine. Bye.")
        break

    while x == 'fire':
        if y == 'cute':
            print("Congratulations! You get a "+ str(pokemon[0]) + "!")
        elif y == 'cool':
            print("Flamin\'! You get a " + str(pokemon[1]) + "!")
        else:
            print("Look out! You get a " + str(pokemon[2]) + "!")
        break

    while x == 'electric':
        if y == 'cute':
            print("Pika pi! You\'ve been given a " + str(pokemon[3]) + "!")
        elif y == 'cool':
            print("Zzzap! You received a " + str(pokemon[4]) + "!")
        else:
            print("Beautiful yet terrifying! You get a " + str(pokemon[5]) + "!")
        break

    while x == 'grass':
        if y == 'cute':
            print("How adorable! You\'ve been given a " + str(pokemon[6]) + "!")
        elif y == 'cool':
            print("What the heck\'s going on here? You just received a " + str(pokemon[7]) + "!")
        else:
            print("Um...gross. You are now the proud owner of a new " + str(pokemon[8]) + "!")
        break

    pleased = str(input("Would you like to try again? (y/n): "))
    if pleased == 'n':
        print("We did it! Enjoy your new Pokemon! Bye bye.")
        break
    else:
        continue
