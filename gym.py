from transaction import *
items=["workout","weights","bikes"]
prices=[35.0,10.30,1.20]
running=True
while running:
    option=1
    for choice in items:
        print(str(option)+"." + choice)
        option=option+1
    print(str(option)+ ". Quit")
    choice=int(input("choose an option"))
    if choice==option:
        running=False
    else:
        credit_card=input("credit card number")
        save_transaction(prices[choice-1],credit_card,items[choice-1])
