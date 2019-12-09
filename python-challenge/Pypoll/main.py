import os
import csv
import numpy as np
csvpath2 = os.path.join('.', 'Resources', 'election_data.csv')
outpath2 = os.path.join('.', 'Resources', 'output_election.csv')
totalvc = 0
candlist = []
count = 0
with open(csvpath2, 'r') as elecfile:
    csvreader = csv.reader(elecfile, delimiter=',')
    next(csvreader)
    num_rows = 0
    for row in csvreader:
    #The total number of votes cast
        totalvc = totalvc + 1
     #A complete list of candidates who received votes
        candlist.append(row[2])
    #The percentage of votes each candidate won 
    
    
#print('Total Votes:', totalvc)
    list = (set(candlist))

output = (
    f"Total Votes: {totalvc}\n"
    f"Complete list of candidates: {list}\n"
)
   
print(output)

#Write to the text path
with open(outpath2, "w") as txt_file:
    txt_file.write(output)
    