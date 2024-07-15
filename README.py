import csv
from datetime import datetime

# File to store budget data
BUDGET_FILE = 'budget.csv'

# Initialize budget file if it doesn't exist
def initialize_budget_file():
    try:
        with open(BUDGET_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])
    except FileExistsError:
        pass

# Add a new budget entry
def add_entry(category, description, amount):
    date = datetime.now().strftime('%Y-%m-%d')
    with open(BUDGET_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print(f"Entry added: {date}, {category}, {description}, ${amount}")

# View all budget entries
def view_entries():
    with open(BUDGET_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Main menu
def main():
    initialize_budget_file()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_entry(category, description, amount)
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
