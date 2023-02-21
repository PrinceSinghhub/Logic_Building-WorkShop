n = int(input("Enter the range:- "))
print('All Even number')
for i in range(1,n+1):
    if i%2==0:
        print(i, end = ' ')
print("\nAll Odd number")
for i in range(n+1):
    if i%2!=0:
        print(i, end =' ')
