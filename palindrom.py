def Reverse(n):
    
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=int(n/10)
    return rev


num=int(input("Enter a number to check: "))
result=Reverse(num)
if(result==num):
    print("The number is palindrome!")
else:
    print("The number is not palindrome!")    
       

