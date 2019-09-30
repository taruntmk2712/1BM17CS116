class CallDetail:
    def __init__(s,c,r,d,t,c1):
        s.c = c
        s.r = r
        s.d = d
        s.t = t
        s.c1 = c1

    def display(s):
        print("CUSTOMER",str(s.c1).ljust(5),end=" ")
        print(s.c.ljust(20),end=" ")
        print(s.r.ljust(20),end=" ")
        print(s.d.ljust(15),end=" ")
        print(s.t.ljust(17))
        return [int(s.c),int(s.r),int(s.d),s.t]
        
        
class Util:
    def __init__(s):
        s.list_call = []
        
    def prase_customer(s,list_of_call_string):
        count = 0
        for i in list_of_call_string:
            b = i.split(',')
            d = CallDetail(b[0],b[1],b[2],b[3],count+1)
            s.list_call.append(d)
            count +=1
    
    def count_1(s):
        count = [0,0,0]
        for i in s.list_call:
            a = i.display()
            if a[3] == 'STD':
                count[0] += 1
            elif a[3] == 'Local':
                count[1] += 1
            elif a[3] == 'ISD':
                count[2] += 1
        print("\n\nCOUNT:\n")
        print("STD  ".ljust(10),end=" ")
        print("Local".ljust(10),end=" ")
        print("ISD  ".ljust(10))
        print(str(count[0]).ljust(10),end=" ")
        print(str(count[1]).ljust(10),end=" ")
        print(str(count[2]).ljust(15),end=" ")
        

call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'
call4 = '9990000023,9330000003,6,ISD'
print("CALL DETAIL'S:")
print("".rjust(15),end=" ")
print("CALLER".ljust(20),end=" ")
print("RECEIVER".ljust(17),end=" ")
print("DURATION".ljust(17),end=" ")
print("TYPE".ljust(22))
list_of_call_string=[call,call2,call3,call4]
util = Util()
util.prase_customer(list_of_call_string)
util.count_1()


'''
OUTPUT:
CALL DETAIL'S:
                CALLER               RECEIVER          DURATION          TYPE                  
CUSTOMER 1     9990000001           9330000001           23              STD              
CUSTOMER 2     9990000001           9330000002           54              Local            
CUSTOMER 3     9990000001           9330000003           6               ISD              
CUSTOMER 4     9990000023           9330000003           6               ISD              


COUNT:

STD        Local      ISD       
1          1          2 

'''
