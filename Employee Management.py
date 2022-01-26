import pickle 
def main():
    print('\tEmployee Management System')
    print()
    print('1. New Employee')
    print('2. Edit Employee')
    print('3. Delete Employee')
    print('4. Search Employee')
    print('9. Exit')
def add(a):
    for i in range(100,10000):
        if i not in a.keys():
            e_id=i
            break
    print('New ID is:-',e_id)
    try:
        e_na=(input('Enter the employee name:- '))
        e_ph=int(input('Enter the employee phone number:- '))
        e_ad=(input('Enter the employee address:- '))
        e_de=(input('Enter the employee department:- '))
        e_sa=int(input('Enter the employee salary:- '))
        a[e_id]=[e_na,e_ph,e_ad,e_sa,e_de]
        print('The new employee has been registered')
    except:print('Please enter proper values!')
    return a
def edit(a):
    try:
        e_id=int(input('Enter the employee id'))
        if e_id in a.keys:
            a[e_id][1]=int(input('Enter the employee phone number:- '))
            a[e_id][2]=(input('Enter the employee address:- '))
            a[e_id][4]=(input('Enter the employee department:- '))
            a[e_id][3]=int(input('Enter the employee salary:- '))
            print('Employee Successfully Edited')
        else:print('Employee ID not found')
    except:print('Please enter proper values!')
    return a
def delete(a):
    try:
        e_id=int(input('Enter the employee id'))
        if e_id in a.keys:
            del a[e_id]
            print('Employee Successfully Deleted')
        else:print('Employee ID not found')
    except:print('Please enter proper values!')
    return a
def search(a):
    try:
        e_id=int(input('Enter the employee id'))
        if e_id in a.keys:
            print('Name',a[e_id][0])
            print('Phone:',a[e_id][1])
            print('Address:',a[e_id][2])
            print('Department:',a[e_id][4])
            print('Salary: Rs',a[e_id][3])
            print('Employee Successfully Edited')
        else:print('Employee ID not found')
    except:print('Please enter proper values!')
def db_creation():
    f1=open('emp.dat','wb')
    employee={}
    pickle.dump(employee,f1)
    f1.close()
def db_load():
    f2=open('emp.dat','rb')
    a=pickle.load(f2)
    f2.close()
    return a
def db_save(a):
    f3=open('emp.dat','wb')
    pickle.dump(a,f3)
    f3.close()


employee={}#id:name, phone, address, salary, department, 
while True:
    print('\nStartup\n')
    b=input("Is this the first time running this program?(Y/N):- ")
    if b=='y'or b=='Y':
        db_creation()
        break
    elif b=='n'or b=='N':
        employee=db_load()
        break
    else:
        print('Enter a valid input')
while True:
    print('\n\n=========================================')
    main()
    x=input('Enter Your Choice:- ')
    if x=='1':
        employee=add(employee)
    elif x=='2':
        employee=edit(employee)
    elif x=='3':
        employee=delete(employee)
    elif x=='4':
        search(employee)
    elif x=='9':
        break
    db_save(employee)
