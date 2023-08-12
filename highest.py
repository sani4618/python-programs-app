def findLarge(x,y):
    if x>y:
        return x
    else:
        return y
    
num1=int(input("enter the first number to be checked "))
num2=int(input("enter the second number to be checked "))
result=findLarge(num1,num2)
print("Largest Number is ",result)    


