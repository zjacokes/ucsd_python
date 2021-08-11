import random

pokemon_type = ['fire', 'electric', 'grass']
pokemon_char = ['cute', 'cool', 'scary']
pokemon = ['Charmander', 'Rapidash', 'Moltres', 'Pikachu', 'Electabuzz', 'Zapdos', 'Bulbasaur', 'Exeggutor', 'Victreebel']



print("\n -- Welcome to the beginning of your new Pokemon adventure! Let\'s find out what Pokemon you get to start out with!")

start = str(input("\n - Are you ready to get assigned a Pokemon? (y/n): "))

while True:

    def func1():
        return random.choice(pokemon_type)
    def func2():
        return random.choice(pokemon_char)

    x = func1()
    z = func2()

    def func3(a):
        return a
    def func4(b):
        return b

    a = func3(x)
    b = func4(z)

    if start == 'y':
        print("\n -- Looks like your favorite type is " + x + "...")
        print("\n -- Okay, your predetermined characteristic is " + z + "...")
    else:
        print("\n -- Oh. Okay fine. Bye.")
        break

    while a == 'fire':
        if b == 'cute':
            print("\n -- Congratulations! You get a "+ str(pokemon[0]) + "!")
        elif b == 'cool':
            print("\n -- Flamin\'! You get a " + str(pokemon[1]) + "!")
        else:
            print("\n -- Look out! You get a " + str(pokemon[2]) + "!")
        break

    while a == 'electric':
        if b == 'cute':
            print("\n -- Pika pi! You\'ve been given a " + str(pokemon[3]) + "!")
        elif b == 'cool':
            print("\n -- Zzzap! You received a " + str(pokemon[4]) + "!")
        else:
            print("\n -- Shocking! Terrifying! You get a " + str(pokemon[5]) + "!")
        break

    while x == 'grass':
        if z == 'cute':
            print("\n -- How adorable! You\'ve been given a " + str(pokemon[6]) + "!")
        elif z == 'cool':
            print("\n -- What the heck\'s going on here? You just received a " + str(pokemon[7]) + "!")
        else:
            print("\n -- Um...gross. You are now the proud owner of a new " + str(pokemon[8]) + "!")
        break

    pleased = str(input("\n - Would you like to try again? (y/n): "))
    if pleased == 'n':
        print("\n -- We did it! Enjoy your new Pokemon! Bye bye.")
        break
    else:
        continue
