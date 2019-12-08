import os
import csv
count = 0
total = []
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        count = count + 1
print('The total number of months included in the dataset', (count-1))
The total number of months included in the dataset 86
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        total.append(int(row[1]))
        total_revenue += total[row]
        print(total_revenue)
#calculate average_change
        average_change = round(total_revenue/count, 2)
        
    


