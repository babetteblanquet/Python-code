import os
import csv

# Path to collect data from the Resources folder
main_file_path = os.path.join("Resources", "budget_data.csv")

with open(main_file_path, "r") as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter = ',')
    #Skipping the headers for the other calculations:
    csv_header = next(csvreader)
#Calculating the total number of months
    total = 0
    total_months = 0
#Creating lists of data to be able to calculate the profit/losses changes
    change_list = []
    profit_list = []
    date_list = []
    for row in csvreader:
        total += int(row[1])
#Calculating the sum of profit/losses over the entire period        
        total_months += 1
#Creating the lists of profit/losses between each month and dates       
        profit_data = int(row[1])
        profit_list.append(profit_data)
        date_data = row[0]
        date_list.append(date_data)
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

                        
#Returning the greatest increase and greatest decrease:
    for x in range(len(change_list)):
            greatest_increase = max(change_list)
            greatest_decrease = min(change_list)
#Returning the months matching the greatest increase and decrease:
            #For the greatest increase
            if change_list[x] == int(greatest_increase):
                profit_greatestinc = profit_list[x+1]
                date_greatestinc = date_list[x+1]
            #For the greatest decrease
            if change_list[x] == int(greatest_decrease):
                profit_greatestdec = profit_list[x+1]
                date_greatestdec = date_list[x+1]
              
    #for row in csvreader:
           # if row[1] == profit_greatestinc:
                #date_found = row[0]
                
#print(date_found)
                                
#Printing outputs:
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total}")
print(f'Average Change: ${average_change(change_list):.2f}')
print(f'Greatest increase: {date_greatestinc} (${greatest_increase})')
print(f'Greatest decrease: {date_greatestdec} (${greatest_decrease})')

# Specify the path to write to
output_path = os.path.join("Analysis", "new.csv")

with open(output_path, "w") as new_file:
    #Initialise CSV writer
    csvwriter = csv.writer(new_file, delimiter = ',')
    #Writing the first row
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f"Total months: {total_months}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f'Average Change: ${average_change(change_list):.2f}'])
    csvwriter.writerow([f'Greatest increase: {date_greatestinc} (${greatest_increase})'])
    csvwriter.writerow([f'Greatest decrease: {date_greatestdec} (${greatest_decrease})'])


