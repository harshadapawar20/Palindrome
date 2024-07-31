n = int(input("Enter the number: "))
rev = 0
original = n
while(n!=0):
    rem = n%10
    rev=rev*10 +rem
    n=n//10
print("reverse is: ", rev)

if(original==rev):
    print("It is a Palindrom")

else:
    print("Not palindrom")
    