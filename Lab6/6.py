class Brackets:
    def __init__(s,a):
        s.a = a 

    def func(s,a):
        count = 0
        b = []
        for i,j in zip(range(0 , n-1) , range(1 ,n) ):
            if s.a[i] == '{':
                if s.a[j] == '}':
                    b.append(1)
                else:
                    b.append(0)
            elif s.a[i] == '(':
                if s.a[j] == ')':
                    b.append(1)
                else:
                    b.append(0)
            elif s.a[i] == '[':
                if s.a[j] == ']':
                    b.append(1)
                else:
                    b.append(0)
        if all( i == 1 for i in b):
            return True
        else:
            return False
   

a = []
str1 = input("Enter Brackets:")
n = len(str1)
if n%2 == 0:
    a = list(str1)
    b1 = Brackets(a)
    if b1.func(a) == True:
        print("Valid Pair's")
    elif b1.func(a) == False:
        print("Invalid Pair's")
else:
    print("Bracket did not form pairs")
