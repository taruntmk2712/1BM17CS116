import random
import string
def func():
    length = random.randrange(8,15)
    count = 0
    pwd = " "
    while count != length:
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        pun = [random.choice(string.punctuation)]
        p_all = upper + lower + num + pun
        pwd += random.choice(p_all)
        count += 1
        continue
    if count == length :
        print("Password:",pwd)


func()
''' 
OUTPUT:
Password:  _`NFGm2rwf%1]5
'''
