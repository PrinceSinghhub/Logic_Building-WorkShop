n = int(input("Enter number:- "))
a = 0
b = 1
sum = a+b
print(0)
print(1)
for i in range(n-2):
    print(sum)
    a = b
    b = sum
    sum=a+b
