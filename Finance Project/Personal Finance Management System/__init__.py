import csv

class Transaction:
    def __init__(self, date, amount, type, category):
        self.date = date
        self.amount = amount
        self.type = type
        self.category = category

    def displayInfo(self):
        return f"Date: {self.date}, Amount: {self.amount}, Type: {self.type}, Category: {self.category}"

class FinanceManager:
    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        print(f"Adding transaction: {transaction.displayInfo()}")
        self.transactions.append(transaction)

    def generateReport(self):
        print("Generating financial report...")
        total_income = sum(t.amount for t in self.transactions if t.type == "income")
        total_expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        total_savings = total_income - total_expenses
        return {
            "Total Income": total_income,
            "Total Expenses": total_expenses,
            "Total Savings": total_savings
        }

    def filterByCategory(self, category):
        print(f"Filtering transactions by category: {category}")
        return [t for t in self.transactions if t.category == category]

    def saveToFile(self, filename):
        print(f"Saving transactions to file: {filename}")
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Type", "Category"])
            for t in self.transactions:
                writer.writerow([t.date, t.amount, t.type, t.category])

    def loadFromFile(self, filename):
        print(f"Loading transactions from file: {filename}")
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.transactions.append(Transaction(row['Date'], float(row['Amount']), row['Type'], row['Category']))

    def getTopExpenses(self, n):
        expenses = [t for t in self.transactions if t.type == "expense"]
        return sorted(expenses, key=lambda x: x.amount, reverse=True)[:n]

    def getCategorySummary(self):
        summary = {}
        for t in self.transactions:
            if t.category not in summary:
                summary[t.category] = {"income": 0, "expense": 0}
            summary[t.category][t.type] += t.amount
        return summary

def main():
    manager = FinanceManager()
    while True:
        print("Welcome to the Personal Finance Management System.")
        print("1. Add Transaction")
        print("2. Generate Report")
        print("3. Filter by Category")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Get Top Expenses")
        print("7. Get Category Summary")
        print("8. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            type = input("Type (income/expense): ")
            category = input("Category: ")
            manager.addTransaction(Transaction(date, amount, type, category))
            print("Transaction added successfully.")

        elif choice == "2":
            report = manager.generateReport()
            print(f"Total Income: ${report['Total Income']}")
            print(f"Total Expenses: ${report['Total Expenses']}")
            print(f"Total Savings: ${report['Total Savings']}")

        elif choice == "3":
            category = input("Enter category to filter: ")
            filtered = manager.filterByCategory(category)
            for t in filtered:
                print(t.displayInfo())

        elif choice == "4":
            filename = input("Enter filename to save: ")
            try:
                manager.saveToFile(filename)
                print("Transactions saved successfully.")
            except Exception as e:
                print(f"Error saving to file: {e}")

        elif choice == "5":
            filename = input("Enter filename to load: ")
            try:
                manager.loadFromFile(filename)
                print("Transactions loaded successfully.")
            except Exception as e:
                print(f"Error loading file: {e}")

        elif choice == "6":
            try:
                n = int(input("Enter the number of top expenses to view: "))
                top_expenses = manager.getTopExpenses(n)
                for t in top_expenses:
                    print(t.displayInfo())
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "7":
            summary = manager.getCategorySummary()
            for category, data in summary.items():
                print(f"Category: {category}, Income: ${data['income']}, Expense: ${data['expense']}")

        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
