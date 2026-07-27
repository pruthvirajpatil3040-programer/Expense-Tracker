import os
import random as rd
import json

def registration():
    user=str(input("Enter your username:"))
    us_f=f'{user}.json'
    if os.path.exists(us_f):
        print('User already signed in')
        print('Go to login')
        login()
    else:
        print('Register Successfully')
        id=rd.randint(1,1001)
        print(f'your id is:{id}')
        data={'Username':us_f,'Id':id}
        # print(data)
        with open(us_f,'w') as fp:
            return json.dump(data,fp)
# registration() 

def login():
    user=str(input("Enter your username:"))
    file=f'{user}.json'
    id_ent=int(input('Enter id:'))
    if not os.path.exists(file):
        print('User not registered:')
        registration()
    else:
        with open(file,'r') as fp:
            data = json.load(fp)
        if (data['Id'] == id_ent and data['Username'] == file):

            print('Login Sucessfully')
            return data['Username']
