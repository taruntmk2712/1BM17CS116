n = int(input("Enter number.:"))
a = [i for i in range(1,n+1) if n%i == 0]
print(a)
/* OUTPUT:
Enter number.:10
[1, 2, 5, 10]*/
