import urllib.request
import time
def get_price():
    page=urllib.request.urlopen("myfirst.html")
    file=open("myfirst.html")
    decoding=page.read().decode("utf8")
    where=decoding.find('>$')
    startprice=where+2
    endprice=startprice+4
    return float(decoding[startprice:endprice])

option=input("do you want the price immediatelt?y/n")
if option=="y":
    print(get_price())

else:
    price=99
    while price>4.74:
        get_price()
        price=get_price()
    print(price)
    print("buy")
