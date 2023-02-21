n = input("Enter 1st number:- ")
m = input("Enter 2ns number:- ")
ans = ''
for i in range(len(n)):
    if n[i]=='0' and m[i]=='0':
        ans+='1'
    else:
        ans+='0'
print("The NOR of 1st and 2nd number is", ans)