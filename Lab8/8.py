import sqlite3
con=sqlite3.connect("StudentDb.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS StudentInfo(USN integer PRIMARY KEY, Name text, branch text, cgpa real)")

def Insert(n):
    for i in range(n):
        usn=input("\nEnter USN: ")
        name=input("\nEnter Name: ")
        branch=input("\nEnter Branch: ")
        cgpa=float(input("\nEnter CGPA: "))
        cur.execute("INSERT INTO StudentInfo VALUES(?,?,?,?)",(usn,name,branch,cgpa))

def Display():
    cur.execute("SELECT * from StudentInfo")
    rows=cur.fetchall()
    for row in rows:
        print(row)

def DisplayStud(usn):
    cur.execute("SELECT * from StudentInfo WHERE USN=?",(usn,))
    row=cur.fetchone()
    print(row)

def Update(usn,name,branch,cgpa):
    cur.execute("UPDATE StudentInfo SET Name=?,Branch=?,cgpa=? WHERE USN=?",(name,branch,cgpa,usn))

def Delete(usn):
    cur.execute("DELETE FROM StudentInfo WHERE USN=?",(usn,))
    
s=1

print("1.Insert\n2.Display\n3.Display Paticular Student\n4.Update\n5.Delete\n6.Exit")
while(s!=6):
    print()
    s=int(input("Enter Choice: "))
    if s==1:
        n=int(input("\nEnter no. of rows: "))
        Insert(n)
        con.commit()
    elif s==2:
        Display()
    elif s==3:
        usn=input("\nEnter USN: ")
        DisplayStud(usn)
    elif s==4:
        usn=input("\nEnter usn: ")
        name=input("\nEnter name: ")
        branch=input("\nEnter branch: ")
        cgpa=float(input("\nEnter cgpa: "))
        Update(usn,name,branch,cgpa)
        con.commit()
    elif s==5:
        usn=input("Enter USN: ")
        Delete(usn)
        con.commit()
    elif s==6:
        break
    else:
        print("\nInvalid Input")

        
con.close()

'''
1.Insert
2.Display
3.Display Paticular Student
4.Update
5.Delete
6.Exit
Enter Choice: 1
Enter no. of rows: 1
Enter USN: 234
Enter Name: xyz
Enter Branch: mech
Enter CGPA: 8.9
Enter Choice: 2
(123, 'xyz', 'cse', 9.22)
(234, 'xyz', 'mech', 8.9)
Enter Choice: 4
Enter usn: 123
Enter name: abc
Enter branch: cse
Enter cgpa: 9.3
Enter Choice: 3
Enter USN: 123
(123, 'abc', 'cse', 9.3)
Enter Choice: 5
Enter USN: 234
Enter Choice: 3
Enter USN: 234
None
Enter Choice: 6
'''
