import os
import csv
<<<<<<< Updated upstream
main_file_path = os.path.join("Resources", "budget_data.csv")
with open(main_file_path, "r") as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter = ',')
    csv_header = next(csvreader)
    total = 0
    for row in csvreader:
        table = list(csvreader)
        total_months = str(len(table))
        total += int(row[1])
        print(str(total))
        

print('Financial Analysis')
print('----------------------------')
print(f"Total months: {total_months}")
print(f"Total: ${total}")
=======
# Path to collect data from the Resources folder
main_file_path = os.path.join("Resources", "budget_data.csv")

with open(main_file_path, "r") as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter = ',')
    #Skipping the headers for the other calculations:
    csv_header = next(csvreader)
#Calculating the total number of months
    total = 0
    total_months = 0
#Creatng lists of data to be able to calculate the profit/losses changes
    change_list = []
    profit_list = []
    for row in csvreader:
        total += int(row[1])
#Calculating the sum of profit/losses over the entire period        
        total_months += 1
#Creating the list of profit/losses between each month        
        profit_data = int(row[1])
        profit_list.append(profit_data)
#Calculating and Creating the list of profit/losses change between each month   
    for i in range(len(profit_list)):
        if i >= 1:
            change = int(profit_list[i]) - int(profit_list[i-1])
            change_list.append(change)

#Define the average function to calculate the average change
def average_change(change_list):
    n = len(change_list)
    total_change = 0.00
    for i in change_list:
        total_change += i
    return total_change / n  
    
print('Financial Analysis')
print('----------------------------')
print(f"Total months: {total_months}")
print(f"Total: ${total}")
print(f'Average Change: ${average_change(change_list):.2f}')

#print(change_list) 

print(csv_header)
>>>>>>> Stashed changes
