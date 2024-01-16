import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print (f"CSV Header: {csv_header}")
    csvreaderlist = list(csvreader)
    #print (csvreaderlist)
    
    total_months = len(list(csvreaderlist))
    total_amount = sum(float(row[1]) for row in csvreaderlist)  

    # total_amount = 0
    # for row in csvreaderlist:
    # total_amount = total_amount + float(row[1])

    # Populate data
    data = []
    for row in csvreaderlist:
        data.append(float(row[1]))
    # print(data)
    changes = []
    for index in range(len(data) - 1):
        # print(index)
        # print(index + 1)
        # print(test[index])
        # print(test[index + 1])
        changes.append(data[index +1] - data[index])
    # print(changes)
    average = (sum(changes)/len(changes))
    maximum = max(changes)
    minimum = min(changes)
    
    max_index = changes.index(maximum)
    min_index = changes.index(minimum)

    dates = []
    for row in csvreaderlist:
        dates.append(row[0])
    # print(dates)

    max_date = dates[max_index+1]
    min_date = dates[min_index+1]

    print(min_date)
    print(max_date)

print ("Financial Analysis")
print ("-------------------------------")
print (f"Total Months: {total_months}")
print (f"Total: ${total_amount}")
print (f"Average Change: ${average}")
print (f"Greatest Increase in Profits: {max_date} ${maximum}")
print (f"Greatest Decrease in Profits: {min_date} ${minimum}")

# # Specify the file to write to
# output_path = os.path.join("..", "output", "budget_data_results.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as csvfile:
