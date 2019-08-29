def func(a, key,n):
    flag = False
    first = 0
    last = n-1
    item = key
    while last >= first:
        mid = int((first+last)/2)
        if a[mid] == key:
            flag = True
            return flag
        elif a[mid] < key:
            first = mid+1
        elif a[mid] > key:
            last = mid-1
        else :
             return flag

a = list(map(int,input().split(" ")))
print(a)
key = int(input("Enter the key:"))
if func(a,key,len(a)) == True:
    print("Element found")
else:
    print("Element not found")
