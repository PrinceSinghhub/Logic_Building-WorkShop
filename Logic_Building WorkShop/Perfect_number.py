n = int(input("Enter your number:- "))
count =0
ans = 1
for i in range(1, n+1):
    if i*i==n:
        ans=i
        count+=1
if count==1:
    print('The given number is perfect number which square of', ans)
else:
    print("The given number is not perfect number")