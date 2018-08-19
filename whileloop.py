print("hello")
g=0
while(g!=3):
    g=input("guess it")
    g=int(g)
    if g>6:
        print("too high")
    else:
        if g<6:
             print("too low")
        else:
            print("you win")
print("game over")
    
