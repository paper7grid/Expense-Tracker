from colorama import Fore, Style, init
import pyfiglet
import csv
import os
from datetime import datetime

# Initialize colorama
init(autoreset=True)

#art banner
banner = pyfiglet.figlet_format("Expense Tracker", font="slant", width=100)
print(Fore.BLUE + banner)
print(Fore.WHITE + "Welcome to the Expense Tracker!")

FILE_NAME = "expenses.csv"
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = input(Fore.GREEN + "Enter the date (YYYY-MM-DD): ")
    category = input(Fore.GREEN + "Enter the category: ")
    description = input(Fore.GREEN + "Enter the description: ")
    amount = float(input(Fore.GREEN + "Enter the amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print(Fore.MAGENTA + "Expense added successfully!")

def view_expenses():
    print(Fore.YELLOW + "\nAll Expenses:")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(Fore.CYAN + f"Date: {row[0]}, Category: {row[1]}, Description: {row[2]}, Amount: ${row[3]}")

def view_summary():
    summary = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[3])
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print(Fore.YELLOW + "\nExpense Summary by Category:")
    for category, total in summary.items():
        print(Fore.CYAN + f"Category: {category}, Total Amount: ${total:.2f}")
    total_expense = sum(summary.values())
    print(Fore.MAGENTA + f"\nTotal Expense: ${total_expense:.2f}")
    



    
