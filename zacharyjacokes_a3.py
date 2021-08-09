print("Hey! You look bored.")

movie_number = int(input("Let\'s figure out a movie or show or something for you to watch tonight. Please type in a number from 1-10: "))

if(movie_number>10):
    print("What the heck! I can only go up to 10. For this infraction you must watch... \'The Notebook.\'")
elif(movie_number==10):
    print("May the odds be ever in your favor. You will be watching \'The Hunger Games\' tonight.")
elif(movie_number==9):
    print("Bad luck chum! You will be watching \'Pirates of the Carribean\' tonight.")
elif(movie_number==8):
    print("Buyer beware! You\'re watching \'Confessions of a Shopaholic\' tonight.")
elif(movie_number==7):
    print("Good luck breaking out of this one! You\'re watching \'The Shawshank Redemption\' tonight!")
elif(movie_number==6):
    print("MY PRECIOUSSSSSSSS! You\'re watching \'The Lord of the Rings\' trilogy! In its entirety.")
elif(movie_number==5):
    print("I\'ll make you an offer you can\'t refuse. Put on \'The Godfather\' tonight.")
elif(movie_number==4):
    print("Ohhh you think darkness is your ally? You\'re watching \'The Dark Knight Rises\' tonight.")
elif(movie_number==3):
    print("It\'s no dream. You\'re watching \'Inception\' tonight.")
elif(movie_number==2):
    print("If yer not first, yer last! You\'re watching \'Talladega Nights\' tonight.")
elif(movie_number==1):
    print("The snozzberries taste like snozzberries! You\'re watching \'Charlie and the Chocolate Factory\' tonight.")
else:
    print("You did not follow the instructions. You must now listen to the \'Numa Numa\' song on repeat.")
