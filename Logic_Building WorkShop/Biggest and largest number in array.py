a = int(input("Enter the size of the array:- "))
array = []
for i in range(a):
    x = int(input("Enter the elements of the array:- "))
    array.append(x)
print("The smallest number of array = ", min(array))
print("The largest number of array = ", max(array))
