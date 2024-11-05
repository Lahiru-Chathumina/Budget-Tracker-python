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
    print(f"Entry added: {date}, {category}, {description}, ${amount:.2f}")

# View all budget entries
def view_entries():
    try:
        with open(BUDGET_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No entries found. Please add some.")

# Calculate total amount spent
def calculate_total():
    total = 0
    try:
        with open(BUDGET_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                total += float(row[3])  # Assuming amount is the fourth column
    except FileNotFoundError:
        print("No entries found to calculate total.")
    return total

# Main menu
def main():
    initialize_budget_file()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. View Total Amount")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
                add_entry(category, description, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            view_entries()
        elif choice == '3':
            total = calculate_total()
            print(f"Total amount spent: ${total:.2f}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
