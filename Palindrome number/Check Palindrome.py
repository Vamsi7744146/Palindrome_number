#write a program to check the given number is palindroma or not
n=int(input())
rev=0
dummy=n
while dummy>0:
    rem=dummy%10
    rev=rev*10+rem
    dummy//=10
if n==rev:
    print('n is palindrome')
else:
    print('not palindrome')