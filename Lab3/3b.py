import random
import string
def pwd():
    pwd = []
    pass1 = " "
    pwd1 = []
    length = random.randrange(8,15)
    count = 0
    upper = [random.choice(string.ascii_uppercase)]
    lower = [random.choice(string.ascii_lowercase)]
    num = [random.choice(string.digits)]
    symbol = [random.choice(string.punctuation)]
    p_all = upper + lower + num + symbol
    for i in range(0,length-4):
        pwd1 += random.sample([random.choice(string.ascii_uppercase)]+[random.choice(string.ascii_lowercase)]+[random.choice(string.digits)]+[random.choice(string.punctuation)],1)
    pwd = random.sample(p_all,4)+pwd1
    for i in pwd:
        pass1 += i
    print("Password:",pass1)
    
pwd()
''' 
OUTPUT:
Password:  _`NFGm2rwf%1]5
'''
