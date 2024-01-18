import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    csvreaderlist = list(csvreader)
    
    # formula for total months
    total_months = len(list(csvreaderlist))
    # formula for total amount
    total_amount = sum(float(row[1]) for row in csvreaderlist)  

    # Populate data (profits/losses column)
    data = []
    for row in csvreaderlist:
        data.append(float(row[1]))

    # add the changes in Profit/Losses to a list
    changes = []
    for index in range(len(data) - 1):
        changes.append(data[index +1] - data[index])

    # formula for average change
    average = (sum(changes)/len(changes))
    # formula for greatest increase and greatest decrease in profits
    maximum = max(changes)
    minimum = min(changes)
    
    # formula to match increase and decrease to the respective dates
    max_index = changes.index(maximum)
    min_index = changes.index(minimum)

    dates = []
    for row in csvreaderlist:
        dates.append(row[0])

    max_date = dates[max_index+1]
    min_date = dates[min_index+1]


# print out to the terminal
print ("Financial Analysis")
print ("-------------------------------")
print (f"Total Months: {total_months}")
print (f"Total: ${total_amount}")
print (f"Average Change: ${average}")
print (f"Greatest Increase in Profits: {max_date} ${maximum}")
print (f"Greatest Decrease in Profits: {min_date} ${minimum}")

#  Specify the file to write to
output_path = os.path.join("Analysis", "budget_data_results.txt")

#  Open the file using "write" mode. Specify the variable to hold the contents
#  source for below: https://blog.enterprisedna.co/python-write-to-file/
with open(output_path, 'w', newline='') as file:
    file.write ("Financial Analysis \n") 
    file.write ("------------------------------- \n") 
    file.write (f"Total Months: {total_months} \n") 
    file.write (f"Total: ${total_amount} \n") 
    file.write (f"Average Change: ${average} \n") 
    file.write (f"Greatest Increase in Profits: {max_date} ${maximum} \n")
    file.write(f"Greatest Decrease in Profits: {min_date} ${minimum} \n")