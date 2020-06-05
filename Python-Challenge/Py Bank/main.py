import os
import csv
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