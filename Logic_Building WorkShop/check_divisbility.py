n = int(input("Enter number:- "))
print("The given number is divisible by")
for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')
