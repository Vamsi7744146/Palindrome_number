#write a program to print palindrome numbers given by the range    
LL=int(input())
UP=int(input())
for num in range(LL,UP+1):
    rev=0
    dummy=num
    len(str(num))
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    if num==rev:
        print(num)