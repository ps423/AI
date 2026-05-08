'''
Q.1) Write a python program to generate Calendar for the given month and year?
[10 Marks]
'''

import calendar

def generate_calendar(year, month):
    print(calendar.month(year, month))

# Example usage
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
generate_calendar(year, month)
