from goal import Goal,budget,show_bud
import expense
print("1.set Goal\n2.Budget\n3.Add Expenses\n4.See Expenses\n5.See Total Expenses")
a=int(input("Enter Your choice:"))


def main(choice_number):
    while(1):
        match choice_number:
            case 1:
                return Goal()
            case 2:
                print("Taking Budget")
                budget()
                print("Final Budget")
                show_bud()
            case 3:
                return expense.add_expenses()
            case 4:
            
                print('1.Show All Expenses\n2.Show recent expenses\n3.Show monthly expenses\n4.Show Category Wise Expenses')
                x = int(input('Enter your choice:'))
                if x==1:
                    return expense.show_expense()
                elif x==2:
                    return expense.recent()
                elif x==3:
                    return expense.month()
                elif x==4:
                    return expense.category()
            case 5:
                return expense.show_total()
        
if __name__ == "__main__":
    main(a)
