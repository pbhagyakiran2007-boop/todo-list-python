import csv

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])

    print("Expense Added Successfully")

def view_expenses():
    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row[0], "-", row[1])
                total += float(row[1])

        print("Total Expense:", total)

    except FileNotFoundError:
        print("No expenses found")

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")