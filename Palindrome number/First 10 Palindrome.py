#write a program to print  first 10th palindrome number
num=1
target=10
count=0
while count<10:
    rev=0
    a=len(str(num))
    dummy=num
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    if num==rev:
        print(num) 
        count+=1
    num+=1