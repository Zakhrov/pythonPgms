import promotions 
import starbuzzpromotion
from transaction import *
items=["Latte","Donut","Espresso","Filter"]
prices=[1.50,2.30,1.20,4.0]
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
        discount_price=promotions.discount(prices[choice-1])
        if input("starbuzz card ? type Y or N")=="Y":
            discount_price=starbuzzpromotion.discount(discount_price)
        save_transaction(discount_price,credit_card,items[choice-1])
