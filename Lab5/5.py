class CallDetail:
    def __init__(s,c,r,d,t):
        s.c = c
        s.r = r
        s.d = d
        s.t = t

    def display(s):
        return [int(s.c),int(s.r),int(s.d),s.t]
        
        
class Util:
    def __init__(s):
        s.list_call = []
        
    def prase_customer(s,list_of_call_string):
        for i in list_of_call_string:
            b = i.split(',')
            d = CallDetail(b[0],b[1],b[2],b[3])
            s.list_call.append(d)
        
    def print(s):
        count = 0
        for i in s.list_call:
            print("CUSTOMER",count+1,":",i.display())
            count +=1
    def count_1(s):
        count = 0
        count1 = 0
        count2 = 0
        for i in s.list_call:
            a = i.display()
            if a[3] == 'STD':
                count += 1
            elif a[3] == 'Local':
                count1 += 1
            elif a[3] == 'ISD':
                count2 += 1
        print("\nCOUNT:\n")
        print("STD:",count)
        print("Local:",count1)
        print("ISD:",count2)
        

call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'
call4 = '9990000023,9330000003,6,ISD'
list_of_call_string=[call,call2,call3,call4]
util = Util()
util.prase_customer(list_of_call_string)
print("Call Details:")
util.print()
util.count_1()


'''
OUTPUT:
Call Details:
CUSTOMER 1 : [9990000001, 9330000001, 23, 'STD']
CUSTOMER 2 : [9990000001, 9330000002, 54, 'Local']
CUSTOMER 3 : [9990000001, 9330000003, 6, 'ISD']
CUSTOMER 4 : [9990000023, 9330000003, 6, 'ISD']

COUNT:

STD: 1
Local: 1
ISD: 2

'''
