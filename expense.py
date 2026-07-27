import json
import os
from datetime import *
from reg import login
from goal import show_bud
user_files = login()

def user_file():
    if not os.path.exists(user_files):
        return {"Username": user_files, "Expenses": []}
    with open(user_files, 'r') as fp:
        return json.load(fp)   #convert in to Json Format
            

def save_file(user):
    with open(user_files,'w') as file:
        return json.dump(user,file)   #Write in JSON format directly
    

def add_expenses():
    try:
        date=input("Enter Date in format (yyyy-mm-dd) or for taking automatically enter 0:").strip()
        if(date=='0'):
            date=datetime.today().strftime("%Y-%m-%d")      #to take time automatically
        else:
            date=datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')        #to validate time
        amount=int(input("Enter amount:"))
        cat=input("Enter Reason like(food, transport, household, etc):").strip()
        bud = show_bud()
        expense={
            'date': date,
            'amount':amount,
            'category':cat,
            'Budget' : bud
        }
        data = user_file()
        if "Expenses" not in data:
            data["Expenses"] = []
            data['Expenses'].append(expense)
        else:
            data['Expenses'].append(expense)
        
        save_file(data)
    except ValueError as v:
        print("Enter valid input:",v)
# add_expenses()  
def show_expense():
    print()
    data = user_file()
    expense1 = data.get("Expenses",[])
    if expense1==[]:
        print("No Expense Record")    
    else:
        
        for e in expense1:
            print(f"Date: {e['date']} | Amount: {e['amount']} | Category: {e['category']} | Budget: {e.get('Budget','N/A')}")
            print('\n')


def recent():
    data = user_file()
    expenses = data.get("Expenses",[])
    try:
        print('........Showing Recent Expenses........')
        rec = int(input('How many recent expenses you want :'))
        print(f'Recent Expenses of {rec}days ')
        if rec<=0:
            print('Enter valid days...')
            exit()
        else:
            for e in expenses[-rec:]:
                print(f"Date: {e['date']} | Amount: {e['amount']} | Category: {e['category']}")
    except ValueError:
        print('INVALID INPUT[Input must be positive integer]')

def month():
    data = user_file()
    expenses = data.get("Expenses",[])
    if expenses ==None:
        print('No expense record')
    else:
        mon = input('Enter Month and year(yyyy-mm):').strip()
        # mon = datetime.strptime(mon,"%Y-%m").strftime('%y-%m')
        found = []
        for e in expenses:
            if e['date'].startswith(mon):
                found.append(e)   
        for e in found:       
            if found == None:
                print('\nNo expenses record')
            else:
                print(f"Date: {e['date']} | Amount: {e['amount']} | Category: {e['category']}")

def category():   
    data = user_file()
    expenses = data.get("Expenses",[])
    if expenses == None:
        print('No Expense Record')
    else:
        cat = input("Enter Category:").strip()
        found = []
        for e in expenses:
            if(e['category'].lower() == cat.lower()):
                found.append(e)
        for e in found:       
            if found == None:
                print('\nNo expenses record')
            else:
                print(f"Date: {e['date']} | Amount: {e['amount']} | Category: {e['category']}")

            
# show_expense()
# show_expense()
def show_total():
    data=user_file()
    ex1 = data.get("Expenses",[])
    result = 0
    res = 0

    for e in ex1:
            result += int(e['amount'])
    print(f'Total Expense is {result}')
    for i in range(0,30):
        for e in ex1:
            res += int(e['amount'])
    if i in range(0,30):
        b = show_bud()
        if b<res:
            print('Warning Your Expense is more than Budget')
        else:
            print(f'Total Expense is {res}')
# show_total()
