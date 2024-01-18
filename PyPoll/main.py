import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    csvreaderlist = list(csvreader)

    #add ballot ids to a list and get the count of that list
    ballot_id = []
    for row in csvreaderlist:
        ballot_id.append(row[0])
    total_votes = len(ballot_id)


    # # make a list for counties - not needed?
    # county = []
    # for row in csvreaderlist:
    #     county.append(row[1])

    # make a list of candidates and get the unique values
    candidate = []
    for row in csvreaderlist:
        candidate.append(row[2])
    
    #list to store unique candidates 
    unique_candidates = []
    for name in candidate:
        if name not in unique_candidates:
            unique_candidates.append(name)
    
    candidate_0_count = candidate.count(unique_candidates[0])
    candidate_1_count = candidate.count(unique_candidates[1])
    candidate_2_count = candidate.count(unique_candidates[2])

    #list to store unique candidate vote counts
    candidate_counts = [candidate_0_count, candidate_1_count, candidate_2_count]

    candidate_0_percent = (candidate_0_count / total_votes) * 100
    candidate_1_percent = (candidate_1_count / total_votes) * 100
    candidate_2_percent = (candidate_2_count / total_votes) * 100
    
    name_count = dict(zip(unique_candidates, candidate_counts))
    winner = (max(name_count, key=name_count.get))


print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {total_votes}")
print ("-------------------------")
print(f"{unique_candidates[0]}: {candidate_0_percent}% ({candidate_0_count})")
print(f"{unique_candidates[1]}: {candidate_1_percent}% ({candidate_1_count})")
print(f"{unique_candidates[2]}: {candidate_2_percent}% ({candidate_2_count})")
print ("-------------------------")
print (f"Winner: {winner}")
print ("-------------------------")


# Specify the file to write to
output_path = os.path.join("Analysis", "election_data_results.txt")

#  Open the file using "write" mode. Specify the variable to hold the contents
#  source for below: https://blog.enterprisedna.co/python-write-to-file/
with open(output_path, 'w', newline='') as file:
    file.write ("Financial Analysis \n") 
    file.write ("Election Results \n")
    file.write ("------------------------- \n")
    file.write (f"Total Votes: {total_votes} \n")
    file.write ("------------------------- \n")
    file.write (f"{unique_candidates[0]}: {candidate_0_percent}% ({candidate_0_count}) \n")
    file.write (f"{unique_candidates[1]}: {candidate_1_percent}% ({candidate_1_count}) \n")
    file.write (f"{unique_candidates[2]}: {candidate_2_percent}% ({candidate_2_count}) \n")
    file.write ("------------------------- \n")
    file.write ("------------------------- \n")
    file.write (f"Winner: {winner} \n")
    file.write ("------------------------- \n")