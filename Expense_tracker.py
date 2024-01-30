# Import necessary libraries
import json
from collections import defaultdict

# Initialize data structures
expense_data = defaultdict(list)
expense_categories = set()

# Function to get user input for expenses
def get_user_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category (e.g., food, transportation, entertainment): ").lower()

    # Validate and store user input
    if category not in expense_categories:
        print("Invalid category. Please choose a valid category.")
    else:
        expense_data[category].append({"amount": amount, "description": description})
        print("Expense added successfully.")

# Function to display monthly summaries and category-wise expenditure
def display_summary():
    for category, expenses in expense_data.items():
        total_amount = sum(expense["amount"] for expense in expenses)
        print(f"\nCategory: {category.capitalize()}")
        print(f"Total Expenses: ${total_amount:.2f}")

# Function to create a user-friendly interface
def user_interface():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Summary")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            get_user_input()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Sample expense categories
expense_categories = {"food", "transportation", "entertainment"}

# Main program
if __name__ == "__main__":
    user_interface()

# Store data to a JSON file for persistent storage
with open("expense_data.json", "w") as file:
    json.dump(dict(expense_data), file, indent=2)

