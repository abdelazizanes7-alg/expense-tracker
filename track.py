print("""welcome to expense tracker
this is our menu:
1_add income
2_add expense
3_show the rest
4_view all transactions
5_view monthly report
6_exit""")
expense_cat=[]
list_expense=[]
choice=int(input("please enter your choice according to the numbers:\n"))
while choice!=6:
    choice=int(input("please enter your choice according to the numbers:\n"))
    if choice ==1:
        income=int(input("please enter your income:\n"))
    elif choice==2:
        expense=int(input("please enter your expense:\n"))
        category=input("please enter your expense category:\n")
        expense_cat.append(category)
        list_expense.append(expense)
    elif choice==3:
        rest=income-sum(list_expense)
        print(f"your rest is {rest}")
    elif choice==4:
        print("your transactions are:")
        for x in range(len(expense_cat)):
            print(f"{x+1}. Category: {expense_cat[x]}, Expense: {list_expense[x]}")
    elif  choice==5:
        print("monthly report:")
        print(f"at first your income was {income}")
        print(f"your total expense is {sum(list_expense)}")
        print(f"and the rest is : {rest}")
    else:
        print("please enter a valid choice")
print("thank you for using our expense tracker")