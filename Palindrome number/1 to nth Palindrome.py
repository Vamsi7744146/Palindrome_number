#write a program to print 6th to 10 palindrome number
num=1
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
        count+=1
        if count>6:
            print(num)
    num+=1