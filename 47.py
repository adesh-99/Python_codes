#47. Write user defined function in Python to Find the sum of elements in a list
def listsum():
    x=[]
    p=int(input("enter no of elements to enter in list:"))
    for i in range(0,p):
       y=int(input("Enter elements of list:"))
       x.append(y)
    sum=0
    for i in range(0,p):
        sum+=x[i]
        i=i+1
    print("Sum of all elements of list is:",sum)
listsum()