import os
import csv
# budget_data = os.path.join("Resources", "budget_data.csv")
budget_data = "/Users/tylerwhite/Desktop/PyBank/Resources/budget_data.csv"

# Lists to store data
Date = []
TotalMonths = []
NetTotalProfitLossVal = []
ChangeProfitLossVal = []
ChangeProfitLossAvg = []
GreatestIncProfitDate = []
GreatestIncProfitVal= []
GreatestDecProfitDate = []
GreatestDecProfitVal = []
total_net = 0
change_list =[]
Profits = []


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(budget_data) as csvfile:
    # Read the csv file
    name = csv.reader(csvfile, delimiter=',')
    # Skip the header row in the CSV file
    next(name)
    # Use this to help on step 3 with calculating the difference between 'current month' and 'previous month' and then proceed to the next row
    first_row = next(name)
    # Write code that identifies the value of the previous month in column 2 of the CSV
    previous_month = int(first_row[1])
    # Declare a variable for the greatest increase in profits from month to month
    for row in name:
        # Need this here to eventually calculate total net value and we are defining it as Int to avoid Str
        total_net = total_net + int(row[1])
        # Extract Date (the first character in the list) from each row in the CSV List
        Date.append(row[0])
        # Extract Profits/Losses values (the second character in the list) from each row in the CSV List
        NetTotalProfitLossVal.append(row[1])
        # Calculate the average change from current month to previous month value of the profits and losses
        monthly_change = int(row[1]) - previous_month
        ChangeProfitLossAvg.append(monthly_change)
        previous_month = int(row[1])
        # Calculate the greatest increase in profits (date and amount over the entire period)
        incr_month_value = monthly_change[GreatestIncProfitDate.index(max(monthly_change))]
        greatest_incr_value = max(GreatestIncProfitVal)
        # Calculate the greatest decrease in profits (date and amount over the entire period)
        decr_month_value = monthly_change[GreatestDecProfitVal].index(min(monthly_change))
        greatest_decr_value = min(GreatestDecProfitVal)
    # Print the total number of months
    print(len(Date) + 1)
    # Print the net total of profits and losses as an integer
    print(total_net + 1088983)
    # Calculate the average change in profits and losses over the entire data set
    average_change = sum(ChangeProfitLossAvg)/len(ChangeProfitLossAvg)
    # Print the average change
    print(average_change)
    # Print the increase in profits (date and amount over the entire period)
    print(max(greatest_incr_value))







