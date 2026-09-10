from datetime import datetime
expenses = []
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            date, amount, category, description = line.strip().split(",")
            expense = {
                "date" : date,
                "amount" : float(amount),
                "category" : category,
                "description" : description
            }
            expenses.append(expense)
except FileNotFoundError:
    pass

def add_expense():
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Please enter only valid Amounts.")
        return 
    if amount <= 0:
        print("Amount must be greater than zero.")
        return 

    date = datetime.now().strftime("%d-%m-%Y")
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "date" : date,
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    expenses.append(expense)

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{amount},{category},{description}\n")

    print("EXPENSE ADDED!")
    print("Amount: ", amount)
    print("Category: ", category)
    print("Description: ", description)

def view_expenses():
    if len(expenses) == 0:
        print("No Expenses")
    else:
        for i, expense in enumerate(expenses, start=1):
            print("-" * 30)
            print(f"#{i}")
            print("Date        :", expense["date"])
            print("Amount      : ", "₹",  expense["amount"])
            print("Category    : ", expense["category"])
            print("Description : ", expense["description"])

def view_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print("The Total is: ", "₹", total)

def view_category():
    if len(expenses) == 0:
        print("No expenses to show")
        return

    else:
        enter_category = input("Enter the category you want to search:  ")
        found = False
        category_total = 0

        for i, expense in enumerate(expenses, start=1):
            if enter_category.lower() == expense["category"]:
                category_total = category_total + expense["amount"]
                print("-" * 30)
                print(f"#{i}")
                print("Date        :", expense["date"])
                print("Amount      : ", "₹",  expense["amount"])
                print("Category    : ", expense["category"])
                print("Description : ", expense["description"])

                found = True
        if found:
            print("-" * 30)
            print(f"The Total of {enter_category} section is ₹{category_total}")

        if not found:
            print("No expenses found in this category.")

def search_expense():
    if len(expenses) == 0:
        print("No expenses to search")
        return 
    else:
        search = input("Enter the word you want to search: ")
        found = False
        for i, expense in enumerate(expenses,  start=1):
            if search.lower() in expense["description"].lower():
                print("-" * 30)
                print(f"#{i}")
                print("Date        :", expense["date"])
                print("Amount      : ", "₹",  expense["amount"])
                print("Category    : ", expense["category"])
                print("Description : ", expense["description"])

                found = True
        if not found:
            print("No matching expenses found.")

def edit_expense():
    if len(expenses) == 0:
        print("No expenses")
        return 
    for i, expense in enumerate(expenses, start=1):
        print("-" * 30)
        print(f"#{i}")
        print("Date        :", expense["date"])
        print("Amount      : ", "₹",  expense["amount"])
        print("Category    : ", expense["category"])
        print("Description : ", expense["description"])

    try:
        number = int(input("Enter the number of expense you want to edit: "))
    except ValueError:
        print("Please enter a valid expense number.")
        return 
    
    if number < 1 or number > len(expenses):
        print("INVALID EXPENSE NUMBER")
        return 

    expense = expenses[number - 1]

    print("\nEnter the new details")

    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Please enter only valid amounts: ")
    if amount <= 0:
        print("Amount must be greater than zero: ")
        return
    
    category = input("Enter the category")
    description = input("Enter the description")

    expense["amount"] = amount
    expense["category"] = category
    expense["description"] = description

    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['date']},{expense['amount']},{expense['category']},{expense['description']}\n")
    print("Expense edited successfully!")

def spending_report():
    if len(expenses) == 0:
        print("No expenses")
        return 

    category_totals = {}

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    print("\n" + "=" * 30)
    print("       SPENDING REPORT")
    print("=" * 30)

    total = 0

    for category, amount in category_totals.items():
        print(f"{category:<15} : {amount:.2f}")
        total = total + amount
    print("-" * 30)
    print(f"{'Total':<15}: ₹{total:.2f}")
    print("=" * 30)

def monthly_report():
    if len(expenses) == 0:
        print("No expenses")
        return 
    month = input("Enter month (MM-YYYY): ")

    monthly_expenses = []

    for expense in expenses:
        expense_month = expense["date"][3:]
        if expense_month == month:
            monthly_expenses.append(expense)

    if len(monthly_expenses) == 0:
        print("No expenses found in this month.")
        return 

    monthly_total = 0
    for expense in monthly_expenses:
        monthly_total = monthly_total + expense["amount"]

    category_totals = {}

    for expense in monthly_expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    print("\n" + "=" * 30)
    print("       MONTHLY REPORT")
    print("=" * 30)

    for category, amount in category_totals.items():
        print(f"{category:<15}: ₹{amount:.2f}")

    print("-" * 30)
    print(f"{'Total':<15}: ₹{monthly_total:.2f}")
    print("=" * 30)


def del_expense():
    if len(expenses) == 0:
        print("No expenses to Delete.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. ₹{expense['amount']} - {expense['category']} - {expense['description']}")
        try:
            number = int(input("Enter the number of expense you want tot delete."))
        except ValueError:
            print("Please enter a valid expense number.")
            return
        
        if number >= 1 and number <= len(expenses):
            expenses.pop(number - 1)
            with open("expenses.txt", "w") as file:
                for expense in expenses:
                    file.write(f"{expense['date']},{expense['amount']},{expense['category']},{expense['description']}\n")

            print("Expense Deleted")
        else:
            print("INVALID EXPENSE NUMBER")

while True:
    print("\n" + "=" * 30)
    print("       EXPENSE TRACKER")
    print("=" * 30)
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total")
    print("4. View by Category")
    print("5. Search Expenses")
    print("6. Edit Expenses")
    print("7. Delete Expense")
    print("8. Spending Report")
    print("9. monthly Report")
    print("10. Exit ")
    print("=" * 30)

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter only numbers(1 - 5)")
        continue
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        view_total()
    elif choice == 4:
        view_category()
    elif choice == 5:
        search_expense()
    elif choice == 6:
        edit_expense()
    elif choice == 7:
        del_expense()
    elif choice == 8:
        spending_report()
    elif choice == 9:
        monthly_report()
    elif choice == 10:
        print("\nThanks for using Expense-Tracker!")
        break
    else:
        print("INVALID CHOICE")