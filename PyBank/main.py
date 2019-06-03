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
    #reading csv file
    next(csvreader)

    for row in csvreader:
        # count total rows
        row_count += 1
        #keep total profit/loss
        total += float(row[1])
        

        if row_count>1:
            change = float(row[1])-  LastRow

        
        #keep running total change
        TotalChange = TotalChange + float(change)
        #holds value to do change
        LastRow=float(row[1])

increase_profit = max(change)
decrease_profit = min(change)

        if row[1] = float(increase_profit)
            max_date = row[0]
        if row[1] = float(decrease_profit)
            min_date = row[0]

AverageChange = float(TotalChange)/float(row_count-1)
print("Average Change: " + str(AverageChange))
print("TotalMonths: " + str(row_count))    
print("Total: " + str(total)
print("Greatest Increase in Profits: " + str(max_date) + str(increase_profit))
print("Greatest Decrease in Profits: " + str(min_date) + str(decrease_profit))
