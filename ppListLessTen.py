x=[]
y=[]
i=int(input("Enter number of elements to be entered :\n"))

for a in range(i):
    n=int(input("enter number"))
    x.append(n)
    if n<5:
        y.append(n)
print("the list contains :")
print(x)
print(" elements less than 5")
print(y)
