#Creating modules
import os
import csv

#Declaring variables
#Variable for counting number of months
count_months = 0

#Calculating total amount of "Profit/Losses"
Total_overall = 0

#Tracking the profit/loss changes
#monthly_change is for the change between months
#previous_month is the value of the preceeding month
#average_change is intended to be the value for the average change
#month_profit_change is the list for tracking the values of differences between the profit/loss values in monthly-change

monthly_change = 0
previous_month = 0
average_change = 0
month_profit_change = []

#Tracking Highest Gains and Losses
month_highest_gain = 0
month_high_name = ""
month_highest_loss = 0
month_low_name = ""

#setting path for csv resource file
csvpath = os.path.join("Resources", "budget_data.csv")

#Open and read CSV file, using the comma as delimiter between the two columns in dataset
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)

    for row in csv_reader: 
        
       #The line for calculating the number of months in the data set
        count_months += 1 

        # Calculating the total revenue
        Total_overall = Total_overall + int(row[1])

        #In lines 47 and 48, in assigning the values for the first row number so that it can be included in tracking differences
        #If the entry in count months is equal to the first row, then assign the value of that row to previous_month
        if(count_months == 1):
            previous_month = int(row[1])
        #For all values equal to and greater than 2 in count_months
        if (count_months >=2):
            
        #Tracking revenue change, lines 54 and 55 subtract from the preceeding row and apply it to monthly_change, month_profit_change is appended to include this new integer at each step
         monthly_change = int(row[1]) - previous_month
         previous_month = int(row[1])
         month_profit_change.append(monthly_change)
         #Tracking the highest gain value in the set, by comparing monthly changes to value, and assigning monthly_changes to highest_gain if it is greater
         if(monthly_change>month_highest_gain):
            month_highest_gain = monthly_change
            month_high_name = row[0]
        #Tracking the highest loss value in set, comparing monthly change to highest loss, assigning monthly_changes to the loss value if change is lesser
         if(monthly_change<month_highest_loss):
            month_highest_loss=monthly_change
            month_low_name = row[0]

        #Finding the average change
    average_change = sum(month_profit_change) / len(month_profit_change)
        
      
# Printing out the results in the terminal and the exported text file
with open(os.path.join("analysis", "output.txt"), "w") as outfile:
    
    print("Financial Analysis")
    outfile.write('Financial Analysis\n')
    print(f"Total Months: {count_months}")
    outfile.write(f"Total Months: {count_months}"+'\n')
    print(f"Total: ${Total_overall}")
    outfile.write(f"Total: ${Total_overall}"+'\n')
    print(f"Average Change: ${round(average_change, 2)}")
    outfile.write(f"Average Change: ${round(average_change, 2)}"+'\n')
    print(f"Greatest Increase in Profits: {month_high_name}, ${month_highest_gain}")
    outfile.write(f"Greatest Increase in Profits: {month_high_name} ${month_highest_gain}"+'\n')
    print(f"Greatest Decrease in Profits: {month_low_name} (${month_highest_loss})")
    outfile.write(f"Greatest Decrease in Profits: {month_low_name} (${month_highest_loss})"+'\n')
