import json
from datetime import datetime
import os


class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []

    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, description=""):
        """Add a new expense"""
        expense = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': float(amount),
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added expense: ${amount} for {category}")

    def get_summary(self):
        """Get summary of expenses by category"""
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']
        return summary

    def show_summary(self):
        """Display summary of expenses"""
        summary = self.get_summary()
        print("\nExpense Summary:")
        for category, amount in summary.items():
            print(f"{category}: ${amount:.2f}")
        print(f"\nTotal: ${sum(summary.values()):.2f}")

    def view_all_expenses(self):
        """Display all expenses"""
        print("\nAll Expenses:")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense['date']} - {expense['category']}: "
                  f"${expense['amount']:.2f} - {expense['description']}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Show summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_all_expenses()
        elif choice == '3':
            tracker.show_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()