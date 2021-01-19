# Modules
import os
import csv

votes[]
candidates[]

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)

    #seperate header
    header = next(csvreader)
    # Loop through data and calc number of votes in ds
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[1])  
        TotalVotes=len(votes)
        #Calc net total amt of Candidates     
        NetTotal=NetTotal + int (row[1]) 

print(f"Total Votes: {TotalVotes}")
print(f"Total: ${NetTotal}")