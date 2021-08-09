# choose your Pokemon program

pokemon = {'fire_cute': 'Charmander', 'fire_cool': 'Rapidash', 'fire_scary': 'Moltres', 'electric_cute': 'Pikachu', 'electric_cool': 'Electabuzz', 'electric_scary': 'Zapdos', 'grass_cute': 'Bulbasaur', 'grass_cool': 'Exeggutor', 'grass_scary': 'Victreebel'}

print("\n Hello! It\'s time to pick a favorite Pokemon. The following are \'types\' of Pokemon: ")

while True:
    print("_____________________________________________________________________________________ \n \n-- fire \n-- electric \n-- grass")
    type = str(input("_____________________________________________________________________________________\n \n Which Pokemon type of the three options above resonates with you the most?: "))
    choice = str(input("_____________________________________________________________________________________\n \n ...and in general, would you describe yourself as \'cute\', \'cool\', or \'scary\'?: "))

    if type == 'fire':
        if choice == 'cute':
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['fire_cute'] + "!")
        elif choice == 'cool':
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['fire_cool'] + "!")
        else:
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['fire_scary'] + "!")
    elif type == 'electric':
        if choice == 'cute':
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['electric_cute'] + "!")
        elif choice == 'cool':
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['electric_cool'] + "!")
        else:
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['electric_scary'] + "!")
    else:
        if choice == 'cute':
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['grass_cute'] + "!")
        elif choice == 'cool':
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['grass_cool'] + "!")
        else:
            print("_____________________________________________________________________________________\n \n Your favorite Pokemon is " + pokemon['grass_scary'] + "!")

    pleased = str(input("_____________________________________________________________________________________\n \n Are you happy with this choice? (y/n): "))

    if pleased == 'y':
        print("_____________________________________________________________________________________\n \n Okay great! Thank you, bye bye.")
        break
    else:
        continue
