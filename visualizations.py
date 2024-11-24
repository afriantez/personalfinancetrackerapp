import matplotlib as mpl
from reports import get_monthly_summary

def plot_monthly_expense(month, year):
    summary = get_monthly_summary(month, year)
    expenses = summary[summary['type'] == 'expense']

    mpl.figure(figsize=(8, 6))
    mpl.pie(expenses['total'], labels=expenses['category'], autopct='%1.1f%%')
    mpl.title(f'Expenses by category for {month}/{year}')
    mpl.show()
