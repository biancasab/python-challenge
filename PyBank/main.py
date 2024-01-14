import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print (f"CSV Header: {csv_header}")
    
    total_months = len(list(csvreader))
    #print (total_months)

    #for row in csvreader:
        #total_amount = sum(int(row[1]))
        #total_amount += float(row[1])
        #print (row)   
    total_amount = sum(float(row[1]) for row in csvreader)
    #NEED TO CORRECT THIS. NOT WORKING. Why is it 0?       

print ("Financial Analysis")
print ("-------------------------------")
print (f"Total Months: {total_months}")
print (f"Total: {total_amount}")
print (f"Average Change:")
print (f"Greatest Increase in Profits:")
print (f"Greatest Decrease in Profits:")