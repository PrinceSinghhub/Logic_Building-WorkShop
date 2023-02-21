n = int(input("Enter range:- "))
count = 0
sum = 0
for i in range(1,n):
    if i%2==0:
        sum+=i
        count+=1
print("The average of even number is", sum/count)