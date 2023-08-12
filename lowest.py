def findSmall(x,y):
    if x<y:
        return x
    else:
        return y

num1=int(input("enter the First number"))
num2=int(input("Enter the 2nd number"))
result=findSmall(num1,num2)
print("smallest is ",result)
   