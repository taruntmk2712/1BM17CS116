def func(a):
    b = []
    for i in a:
        if i%2 == 0:
            b.append(i)
    print("Even List:")
    print(b)


a = []
n = int(input("Enter the size of list:"))
print("Enter elements:")
for i in range(n):
    item = int(input())
    a.append(item)
print("List:")
print(a)
func(a)
