
num1= int(input("enter 1st number: "))
op=input("enter the operator: ")
num2=int(input("enter 2nd number: "))

if(op=="+"):
    print(num1+num2)
elif(op=="*"):
    print(num1*num2)
elif(op=="-"):
    print(num1-num2)
elif(op=="/"):
    print(num1/num2)
else:
    print("invalid inputs")

