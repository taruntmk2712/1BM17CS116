def func(n):
    if n <= 1:
        return 1
    else:
        return func(n-1) + func(n-2)


n = int(input("Enter the no.:"))
for i in range(n):
    print("Fibonacci[",i,"] = ",func(i))
