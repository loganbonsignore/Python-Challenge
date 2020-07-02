# PyBank

# Analyze csv for:
#   the total number of months included in the dataset
#   the total profit/loss over the entire period
#   the average of the changes in profit/loss over the entire period
#   the greatest decrease in losses (date and amount) over the entire period


import os
import csv

input_path = os.path.join("..","resources","budget_data.csv")

num_months = 0
total_profit = 0
profit_change_int = []
profit_change_month = []
previous_month = "Jan"
previous_profit = 867884

with open(input_path, "r") as input_file:
    # create csv reader
    csvreader = csv.reader(input_file)
    # pull header row from iterable data
    header = next(csvreader)
    for row in csvreader:
        # find total number of months
        current_month = row[0].split()[0]
        if previous_month != current_month:
            num_months = num_months + 1
            previous_month = current_month
        # find total profit over entire period
        total_profit = total_profit + int(row[1])
        # find monthly profit/loss
        profit_change = (int(row[1]) - previous_profit)
        profit_change_int.append(profit_change)
        profit_change_month.append(row[0])
        previous_profit = int(row[1])
    # find the average profit
    average_profit = "${:,.2f}".format(sum(profit_change_int) / (len(profit_change_int) -1))
    # find the largest M/M increase and decrease of profit
    decrease_int = min(profit_change_int)
    increase_int = max(profit_change_int)
    # find the index number of greatest increase/decrease values in profit_change_int list
    index_decrease = profit_change_int.index(decrease_int)
    index_increase = profit_change_int.index(increase_int)
    # use index number found above to find the corresponding month in the profit_change_month list
    greatest_decrease_month = profit_change_month[index_decrease]
    greatest_increase_month = profit_change_month[index_increase]

#Print Financial Analysis to terminal
print(f"""Financial Analysis
--------------------------------------
Total Months: {num_months}
Total Profit/Loss: {"${:,.2f}".format(total_profit)}
Average Monthly Profit Change: {average_profit}
Greatest Increase in Profits: {greatest_increase_month} ({"${:,.2f}".format(increase_int)})
Greatest Decrease in Profits: {greatest_decrease_month} ({"${:,.2f}".format(decrease_int)})""")

#Export data to new csv
output_path = os.path.join('output.csv')
#Create lists to zip together
column1 = ["Total Months","Total Profit/Loss","Average Profit Change","Greatest Increase in Profits - Month","Greatest Increase in Profits - Number","Greatest Decrease in Profits - Month","Greatest Decrease in Profits - Number"]
column2 = [num_months, "${:,.2f}".format(total_profit), average_profit, greatest_increase_month, "${:,.2f}".format(increase_int), greatest_decrease_month, "${:,.2f}".format(decrease_int)]
#Open csv writer, zip list and commit output
with open(output_path, "w") as output_file:
    csvwriter = csv.writer(output_file)
    output_final = zip(column1,column2)
    csvwriter.writerows(output_final)
