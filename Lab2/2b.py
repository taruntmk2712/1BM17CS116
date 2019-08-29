import re
def fun(str1):
    s = " "
    li = list(re.split(r'(\s+)',str1))
    list_f = li.reverse()
    for i in li:
        s += i
    return s
def fun1(s1):
    s = " "
    for i in s1:
        s = i + s
    print(" ",s)

str1 = input("Enter string:\n")
s1 = fun(str1)
print(s1)
fun1(s1)
