import os
import csv

# Files to Load
csvpath = "C:/Users/David/Desktop/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
file_to_output = "Resources/budget_data.txt"

#Variables
total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
revenue_changes = []

# Read Files
with open(csvpath) as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:
        
     # Keep track of changes
        if(total_months == 0):
             revenue_change = 0
        else:
             revenue_change = int(row["Profit/Losses"]) - prev_revenue
     # print(revenue_change)

        # Calculate number of months and changes
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        # print(row)


        # value to subtract from the next change, receiving "KeyError" for "Profit/Losses"
        prev_revenue = int(row["Profit/Losses"]) 
        #print(prev_revenue)

        # Determine the greatest increase and date
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        # Add to the revenue_changes list
        revenue_changes.append(revenue_change)

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    
with open("C:/Users/David/Desktop/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv", "w") as text:    
    text.write("Financial Analysis")
    text.write("-------------------------")
    text.write("Total Months: " + str(total_months))
    text.write("Total Revenue: " + "$" + str(total_revenue))
    text.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    text.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    text.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
 

