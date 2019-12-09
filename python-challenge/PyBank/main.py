import os
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
outpath = os.path.join('.', "Resources", "output_analysis.txt")
count=0
greatestincrease = ["", 0]
greatestdecrease = ["", 999999]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    rowtotal = 0
    for row in csvreader:
        pl.append(row[1])
   #The total number of months included in the datase
        count = count + 1
   #The net total amount of "Profit/Losses" over the entire period
        rowtotal += int(row[1])
    #The average of the changes in "Profit/Losses" over the entire period
        average_pl_change = round(rowtotal/count, 2)
        
      
    #Greatest Increase
        
    #Greatest Decrease
      
    
#print the outcomes
output = (
    f"Total Months: {count}\n"
    f"Total Revenue: ${rowtotal}\n"
    f"Average Revenue Change: ${average_pl_change}\n"
    f"Greatest increase in profits: {greatestincrease[0]} ${greatestincrease[1]}\n"
    f"Greatest decrease in profits: {greatestdecrease[0]} ${greatestdecrease[1]}\n"

)

print(output)

#Write to the text path
with open(outpath, "w") as txt_file:
    txt_file.write(output)
        
        
    


