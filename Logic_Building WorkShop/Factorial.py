n = int(input("Enter number:- "))
count = 1
for i in range(n, -1, -1):
    if i==1:
        break
    count*=i
print("The factorial of", n, 'is',count)