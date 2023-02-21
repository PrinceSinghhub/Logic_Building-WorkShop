player = int(input("Enter count of team member:- "))
count = 0
for i in range(player):
    x = int(input("Enter count number of player:- "))
    count+=x
count=count/player
print("Average count of cricket team is",count)