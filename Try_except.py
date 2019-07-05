number=0
try:
    
    number1=int(input("enter a number"))
    number2=number1/number
    print(number2)
    
except ZeroDivisionError as err:
    print(err)
    # run and see????????????????? invalid literal with int as base 10
except ValueError as inv:
    print(inv)
