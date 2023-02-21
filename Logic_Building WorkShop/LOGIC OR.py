n = input("Enter 1st number in binary:- ")
m = input("Enter 2nd number in binary:- ")
ans  = ''
for i in range(len(n)):
    if n[i]=='0' and m[i]=='0':
        ans+='0'
    else:
        ans+='1'
print("The answer of 1st and 2ns number is",ans)

