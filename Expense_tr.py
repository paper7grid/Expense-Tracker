from colorama import Fore, Style, init
import pyfiglet
import csv
import os
from datetime import datetime

# Initialize colorama
init(autoreset=True)

#art banner
banner = pyfiglet.figlet_format("Expense Tracker")
print(Fore.CYAN + banner)
print(Fore.YELLOW + "Welcome to the Expense Tracker!")

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
 