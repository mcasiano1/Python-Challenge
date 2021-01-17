# Modules
import os
import csv
months=[]
pl=[]
Totalpl=[]
NetTotal=0

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)
    # Loop through data
    for row in csvreader:
        months.append(row[0])
        pl.append(row[1])       
        NetTotal=NetTotal + int (row[1]) 

TotalMonth=len(months)
print(f"Total Months: {TotalMonth}")
print(f"Total: ${NetTotal}")