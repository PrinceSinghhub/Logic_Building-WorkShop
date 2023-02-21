n = int(input("Enter number:-"))
n = str(n)
ans = 0
for i in range(len(n)):
    ans+=int(n[i])
print("The sum of all integer is", ans)
