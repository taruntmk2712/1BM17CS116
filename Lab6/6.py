class Brackets:
    def __init__(s,str1):
        s.str1 = str1

    def func(s):
       open_b = tuple('({[')
       close_b = tuple(')}]')
       balance = dict(zip(open_b,close_b))
       a = []
       for i in s.str1:
           if i in open_b:
               a.append(balance[i])
           elif i in close_b:
               if not a or i != a.pop():
                   return False
       return True
              
str1 = input("Enter Brackets:")
n = len(str1)
if n%2 == 0:
    b1 = Brackets(str1)
    if b1.func() == True:
        print("Valid Pair's")
    elif b1.func() == False:
        print("Invalid Pair's")
else:
    print("Bracket did not form pairs")

'''
OUTPUT:
Enter Brackets:{}[({{}})]
Valid Pair's

Enter Brackets:[](]
Invalid Pair's

Enter Brackets:[](
Bracket did not form pairs
'''
