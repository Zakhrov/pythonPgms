div=[]

x=int(input("enter a number"))

start=int(input("enter the starting range of divisor"))
stop=int(input("enter the ending range of the divisor"))

for i in range(start,stop):
    if x%i==0:
        div.append(i)
        i+=1

print(div)

