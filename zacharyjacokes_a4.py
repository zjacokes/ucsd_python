# the pattern in the provided .txt file subtracts 101-n from the starting number 10000 where 'n' is defined as the number of iterations plus 1 (the first iteration = 0)
# UNTIL 101-n = 10, at which point the pattern starts over from n = 100 again.

n,x,y = 10101,101,100

while n > 4995:
    n = n - x
    x = x - 1
    print(n)
while n < 4996 and n > 0:
    n = n - y
    y = y - 1
    print(n)




#first attempt:

#n,x,y = 10000,100,100
#while x > 9:
#    if n == 10000:
#        print(n)
#        n = n - x
#    elif n < 10000:
#        print(n)
#        x = x - 1
#        n = n - x
#    while n < 5000 and y > 11:
#        if n == 4995:
#            print(n)
#            n = n - y
#        elif n < 4995:
#            print(n)
#            y = y - 1
#            n = n - y



#second attempt:

#n,x,y = 10101,101,100
#while n > 0:
#    if n > 4995:
#        n = n - x
#        x = x - 1
#        print(n)
#    else:
#        n = n - y
#        y = y - 1
#        print(n)
