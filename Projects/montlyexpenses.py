#monthly expenses:

print("Welcome to the budget calculator")
income=float(input("Enter your monthly income:Rs."))
additional_income=float(input("Enter your additional(part_time)income:Rs."))

total_income= income + additional_income
print("Your Total income (Rs) is:"+str(total_income))


def gather_expenses():
    housing=float(input("Enter your monthly House rent:Rs."))
    utility=float(input("Enter your monthly Utilities:Rs."))
    food=float(input("Enter your montly food expenses:Rs."))
    other_expenses=float(input("Enter your other expenses:Rs."))
    total_expenses=housing+utility+food+other_expenses
    return total_expenses

expenses_total=gather_expenses()
print("Your total Expenses this month :Rs."+str(expenses_total))

savings=total_income-expenses_total
if savings>=0:
    print("Your savings this month:"+str(savings))
else:
    print("Sorry you have No Savings this month" +  "\nburden:"+str(savings))
    print("Try to make your expenses minimal from the next month")

print("Thanks for using The Monthly expenses Calculator")