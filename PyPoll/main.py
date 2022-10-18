#Creating modules
import os
import csv


#Declaring variables
count_votes = 0
candidate_list = {}
candidate_won = ""
candidate_vote_count = 0
candidate_percent_won = 0

#setting path for csv resource file
csvpath = os.path.join("Resources", "election_data.csv")

#Open and read CSV file, using the comma as delimiter between the two columns in dataset
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

#Listing header columns for resource file
    csv_header = next(csv_file)



    for row in csv_reader: 
       
       #Function for counting the total number of votes
        count_votes += 1 
        
#If the name listed in row 3 is not in the candidate list directory, then it would add the name to the directory, if it is, it adds the count under that entry. 
        if(row[2] not in candidate_list):
            candidate_list[row[2]] = 1
        else:
            candidate_list[row[2]] += 1
#The for statement intended to dictate the candidate who received the most votes and won, by determining if the vote count is less than the vote count under a certain candidate
#it would assign itself the value of that higher value candidate
    for candidate in candidate_list:
        if(candidate_vote_count < candidate_list[candidate]):
            candidate_vote_count = candidate_list[candidate]
            candidate_won = candidate


#Printing the outcome to both the terminal and the external text file under "analysis"
with open(os.path.join("analysis","output.txt"), 'w') as outfile:
    
    print("Election Results")
    outfile.write('Election Results\n')
    print(f"Total Votes: {count_votes}")
    outfile.write(f"Total Votes: {count_votes}"+'\n')
    for k,v in candidate_list.items():
        print(f"{k}:{round(v/count_votes * 100, 3)}% ({v})")
        outfile.write(f"{k}:{round(v/count_votes * 100, 3)}% ({v})"+'\n')
    print(f"Winner: {candidate_won}")
    outfile.write(f"Winner: {candidate_won}"+'\n')
    
