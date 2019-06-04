import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    
    row_count = 0
    total = 0
    LastRow = 0
    change = 0
    TotalChange =0
    AverageChange = 0
    increase_profit = 0
    decrease_profit = 0
    
    #skip header
    next(csvreader)

    for row in csvreader:
        # count total rows
        row_count += 1
        #keep total profit/loss
        total += float(row[1])
        
        if row_count>1:
            change = float(row[1]) -  LastRow

        if decrease_profit > float(row[1]):
            decrease_profit = float(row[1])
            min_date = row[0]

        if increase_profit < float(row[1]):
            increase_profit = float(row[1])
            max_date = row[0]
        
        #keep running total change
        TotalChange = TotalChange + float(change)
        #holds value to do change
        LastRow=float(row[1])



AverageChange = float(TotalChange)/float(row_count-1)

print(f"Average Change: ${AverageChange:,.2f}")
print(f"TotalMonths: {row_count}")    
print(f"Total: {total}")
print(f"Greatest Increase in Profits: {max_date} ${increase_profit:,.2f}")
print(f"Greatest Decrease in Profits: {min_date} ${decrease_profit:,.2f}")

with open("Output.txt", "w") as text_file:
    text_file.write(f"Average Change: ${AverageChange:,.2f}\n")
    text_file.write(f"TotalMonths: {row_count}\n")
    text_file.write(f"Total: {total}\n")
    text_file.write(f"Greatest Increase in Profits: {max_date} ${increase_profit:,.2f}\n")
    text_file.write(f"Greatest Decrease in Profits: {min_date} ${decrease_profit:,.2f}\n")
