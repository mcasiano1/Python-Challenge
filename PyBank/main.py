# Modules
import os
import csv
months=[]
pl=[]
AvgChange=[]
mchange=[]
NetTotal=0

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)
    # Loop through data and calc number of months in ds
    for row in csvreader:
        months.append(row[0])
        pl.append(row[1])  
        TotalMonth=len(months)
        #Calc net total amt of P/L     
        NetTotal=NetTotal + int (row[1]) 

print(f"Total Months: {TotalMonth}")
print(f"Total: ${NetTotal}")

#Calc Average Change
i=0
for i in range(len(pl)-1):
    p_loss= int(pl[i+1])-int(pl[i])
#Append p_loss
    AvgChange.append(p_loss)
Total=sum(AvgChange)
mchange=Total/len(AvgChange)
m_format=mchange
Formatted_m="{:.2f}".format(m_format)
print(f"Average Change: ${Formatted_m}")




