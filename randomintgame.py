from random import randint
secret=randint(1,10)
print("welcome to the game")
while secret:
    g=input("enter the number")
    g=int(g)
    if g>secret:
        print("too high")
    else:
        if g<secret:
            print("too low")
        else:
            print("you won")
print("the secret number is ",secret)

