import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        #print (row)


print ("Election Results")
print ("-------------------------")
print ("Total Votes: ")
print ("-------------------------")
print ("-------------------------")
print ("Winner" )
print ("-------------------------")


#set variable for output file
output_file = os.path.join("budget_data_final.csv")

#Open the output file
with open(output_file, "w", newline='') as datafile
    writer = csv.writer(datafile)