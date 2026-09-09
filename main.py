expenses = []
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            amount, category, description = line.strip().split(",")
            expense = {
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
    
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    expenses.append(expense)

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{description}\n")

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
            print("Amount      : ", "₹",  expense["amount"])
            print("Category    : ", expense["category"])
            print("Description : ", expense["description"])

def view_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print("The Total is: ", "₹", total)

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
                    file.write(f"{expense['amount']},{expense['category']},{expense['description']}\n")

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
    print("4. Delete Expense")
    print("5. Exit ")
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
        del_expense()
    elif choice == 5:
        print("\nThanks for using Expense-Tracker!")
        break
    else:
        print("INVALID CHOICE")