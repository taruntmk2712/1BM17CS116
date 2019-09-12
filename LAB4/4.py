class University:
    def __init__(a):
        a.sid = None
        a.age = None
        a.marks = None
        
    def validate_age(a,age):
        if age > 0:
            if age>20:
                return True
        else:
            return False
      

    def validate_marks(a,marks):
        if 0< marks  <= 100: 
            if marks>=65:
                return True
        else:
            return False

    def getter(a):
        a.sid = input("Enter ID:")
        a.age = int(input("Enter age:"))
        a.marks = int(input("Enter marks:"))
        if a.validate_age(a.age) == True and a.validate_marks(a.marks) == True:
            return True
        elif a.validate_age(a.age) == False and a.validate_marks(a.marks) == False:
            return False            
            
uni = University()
if uni.getter() == True:
    print("Congratulations....!You are admitted")
else:
    print("Application rejected")
    
'''
OUTPUT:

Enter ID:a
Enter age:23
Enter marks:89
Congratulations....!You are admitted


Enter ID:a
Enter age:12
Enter marks:18
Application rejected
'''
