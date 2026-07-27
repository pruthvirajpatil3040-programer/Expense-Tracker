def  Goal():
    des=str(input('What is your goals for future:')).strip()
    amount=int(input('Amount of that goal object you want:'))
    year=int(input('In how many years you want to buy:'))
    print('This is the amount you have to store daily.')
    total = float(amount/(year*365))
    print(f'You want to save {total} daily')
    
    return Goal1
def show_bud():  # sourcery skip: inline-immediately-returned-variable
    bud1 =  int(input("Enter your final budget:"))
    return bud1
print('Taking Budget')
def budget():
    income=int(input('What is your Income?:'))
    bud=int(input('How much is your budget?:'))
    if bud>income:
        print('Your budget is higher than income')
        print('please reduce your budget if you want')
        bud1=int(input('if you want to reduce please enter your budget otherwise enter 0'))
        if bud1==0:
            print('previous budget added successfully')
        else:
            bud=bud1
            print('budget added successfully')
    else:
        print('budget added successfully')
    return bud

    
