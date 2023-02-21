n = input("Enter number:- ")
ans = ''
for i in range(len(n)):
    if n[i]=='1':
        ans+='0'
    else:
        ans+='1'
print("The LOGICAL NOT of number is", ans)
