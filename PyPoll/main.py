# Modules
import os
import csv

votes=[]
candidates=[]


# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)

# Loop through data and calc total number of votes in ds, similar to PyBank 
    for row in csvreader:
        votes.append(row[0])
        TotalVotes=len(votes)            

print(f"Total Votes: {TotalVotes}")

#Complete list of candidates who received votes
candidates.append(row[2])



