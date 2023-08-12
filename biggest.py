def findLarge(x,y,z):
    if x>y:
        return x
    elif y>z:
        return y
    else:
        return z
num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
num3=int(input("enter the 3rd number"))
result=findLarge(num1,num2,num3)
print("Largest Number is ",result)


