with open("happynumber.txt","r") as f1:
    a = f1.read()
    a = a.strip()
    a=a.split(' ')
    

with open("prime.txt","r") as f2:
    b = f2.read()
    b = b.strip()
    b=b.split(' ')
print("Overlapping numbers:")
for i in a:
    if i in b:
        print(i)
'''
OUTPUT:
Overlapping numbers:
7
13
19
23
31
79
97
103
109
139
167
193
239
263
293
313
331
367
379
383
397
409
487
563
617
653
673
683
709
739
761
863
881
907
937
'''
