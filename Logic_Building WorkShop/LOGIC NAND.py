n = input("Enter 1st number in binary:- ")
m = input("Enter 2nd number in binary:- ")
ans  = ''
result = ''
for i in range(len(n)):
    if n[i]=='1' and m[i]=='1':
        ans+='1'
    else:
        ans+='0'
for i in range(len(ans)):
    if ans[i]=='1':
        result+='0'
    else:
        result+='1'
print("The answer of 1st and 2ns number is", result)

