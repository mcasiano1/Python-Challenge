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
        candidates.append(row[2])            

print(f"Total Votes: {TotalVotes}")

#Complete list of candidates who received votes
candidates_count=[[x,candidates.count(x)] for x in set(candidates)]

vote=[]
name=[]

for row in candidates_count:
    name.append(row[0])
    vote.append(row[1])

zipcandidates= zip(name,votes)
listcandidates=list(zipcandidates)

#Election Winner
candidatewinner = max(vote)
print(f"Winner: {candidatewinner}")

#The total number and percentage of votes each candidate won

Correy_Total_Votes=candidates.count('Correy')
#percentage = total/sum
Correy_Percentage_Votes=int(Correy_Total_Votes)/TotalVotes

Li_Total_Votes=candidates.count('Li')
#percentage = total/sum
Li_Percentage_Votes=int(Li_Total_Votes)/TotalVotes

OTooley_Total_Votes=candidates.count("O'Tooley")
#percentage = total/sum
OTooley_Percentage_Votes=int(OTooley_Total_Votes)/TotalVotes

Khan_Total_Votes=candidates.count('Khan')
#percentage = total/sum
Khan_Percentage_Votes=int(Khan_Total_Votes)/TotalVotes

print(f"Khan: {Khan_Percentage_Votes:.3%} ({Khan_Total_Votes})")
print(f"Correy: {Correy_Percentage_Votes:.3%} ({Correy_Total_Votes})")
print(f"Li: {Li_Percentage_Votes:.3%} ({Li_Total_Votes})")
print(f"O'Tooley: {OTooley_Percentage_Votes:.3%} ({OTooley_Total_Votes})")


















