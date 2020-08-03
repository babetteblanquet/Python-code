import os
import csv

# Path to collect data from the Resources folder
main_file_path = os.path.join("Resources", "election_data.csv")

with open(main_file_path, "r") as election_data_file:
    csvreader = csv.reader(election_data_file, delimiter = ',')
    #Skipping the headers for the other calculations:
    csv_header = next(csvreader)
#Setting up the variables
    total_votes = 0
#Creating lists for candidates:
    Khan_list = []
    Correy_list = []
    Li_list = []
    OTooley_list = []
    for row in csvreader:
        total_votes += 1
        if row[2] =='Khan':
            Khan_list.append(row[2])
        if row[2] =='Correy':
            Correy_list.append(row[2])   
        if row[2] =='Li':
            Li_list.append(row[2])    
        if row[2] =="O'Tooley":
            OTooley_list.append(row[2])
  #Calculating the number of votes and percentage for each candidates 
    Khan_votes = (len(Khan_list))
    Khan_percent =  (Khan_votes / total_votes)*100
    Correy_votes = (len(Correy_list))
    Correy_percent =  (Correy_votes / total_votes)*100
    Li_votes = (len(Li_list))
    Li_percent =  (Li_votes / total_votes)*100
    OTooley_votes = (len(OTooley_list))
    OTooley_percent =  (OTooley_votes / total_votes)*100
#Announcing the winner
    Candidates = ['Khan', 'Correy', 'Li', "O'Tooley"]
    Results = [Khan_votes, Correy_votes, Li_votes, OTooley_votes]
    for i in range(len(Results)):
        winner = max(Results)
        if Results[i]== winner:
            theWinner = Candidates[i]

            
#Printing outputs:
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f'Khan: {Khan_percent:.3}% ({Khan_votes})')
print(f'Correy: {Correy_percent:.3}% ({Correy_votes})')
print(f'Li: {Li_percent:.3}% ({Li_votes})')
print(f"O'Tooley: {OTooley_percent:.3}% ({OTooley_votes})")
print("----------------------------")
print(f"Winner: {theWinner}")
print("----------------------------")

# Specify the path to write to
output_path = os.path.join("Analysis", "new.csv")

with open(output_path, "w") as new_file:
#Initialise CSV writer
   csvwriter = csv.writer(new_file, delimiter = ',')
#Writing the first row
   csvwriter.writerow(["Election Results"])
   csvwriter.writerow(['-----------------------------'])
   csvwriter.writerow([f"Total Votes: {total_votes}"])
   csvwriter.writerow(['-----------------------------'])
   csvwriter.writerow([f'Khan: {Khan_percent:.3}% ({Khan_votes})'])
   csvwriter.writerow([f'Correy: {Correy_percent:.3}% ({Correy_votes})'])
   csvwriter.writerow([f'Li: {Li_percent:.3}% ({Li_votes})'])
   csvwriter.writerow([f"O'Tooley: {OTooley_percent:.3}% ({OTooley_votes})"])
   csvwriter.writerow(['-----------------------------'])
   csvwriter.writerow([f"Winner: {theWinner}"])
   csvwriter.writerow(['-----------------------------'])