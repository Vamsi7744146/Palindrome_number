#write a program to print 10th palindrome number
num=1
count=0
target=10
while count<target:
    rev=0
    dummy=num
    a=len(str())
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    if num==rev:
        count+=1
        if count==target:
            print(num)
    num+=1