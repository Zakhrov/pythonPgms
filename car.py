
# what is while comparing here below?????????????????
# it's an endless loop

def game():
    cmd=""
    stopped=False
    started=False
    
    while True:
        cmd=input("> ").lower()
        if cmd=="start" and started==True and stopped==False:
            print("car already started")
                
        elif cmd=="start" and started==False:
            print("car started... Ready to go!!")
            started=True
            stopped=False

        elif cmd=="stop" and stopped==True:
            cont=input("car already stopped, Do you want to continue? y/n :").lower()
            if cont=="y":
                continue
            elif cont=="n":
                 break
        elif cmd=="stop" and started==False:
            print("start the car before you choose stop")
            


        
                

        elif cmd=="stop" and started==True and stopped==False:
            print("car stopped")
            stopped=True
            started=False
        
        elif cmd=="help":
            print("""
            start -to start the car
            stop  -to stop the car
            quit  -to quit the game
            """)
        elif cmd=="quit":
            break
        else:
            print("invalid command")
            ### why is not bre aking here?????????
            # because loop is still true
    print("end of game")    

game()
