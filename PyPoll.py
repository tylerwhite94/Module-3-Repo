import os
import csv
# election_data = os.path.join("..", "Resources", "election_data.csv")
election_data = "/Users/tylerwhite/Desktop/PyPoll/Resources/election_data.csv"
#Create empty lists to store data
total_votes = 0
individual_candidates = []
all_candidates = []
percent_list = []
data = []
candidate_votes = {}

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_data) as csvfile:
# Read the CSV File
    reader = csv.reader(csvfile, delimiter=',')
    # Skip the header row in the CSV File
    header = next(reader)
    # iterate through each row
    for row in reader:
        # Count the total number of votes cast by incrementing the total number of rows
        total_votes = total_votes + 1
        # Provide a complete list of candidates who received votes by appending
        all_candidates.append(row[2])
        # Check to see that names are matching
        if row[2] in individual_candidates:
            # Have it increment by 1
            candidate_votes[row[2]] += 1
        # Else condition starts over with new candidate name
        else: 
            # Set an initiatl count for the candidate
            candidate_votes[row[2]] = 1
            individual_candidates.append(row[2])
# Print the total number of votes cast
print(total_votes)
print(candidate_votes)
# Print the total number of votes each candidate received
print(len(individual_candidates))
# Calculate the percentage for each candidate
for i in individual_candidates:
    percentage = (candidate_votes[i]/total_votes)*100
    # Use append to help gather the right percentage
    percent_list.append(percentage)
    # Calculate who has the most votes to eventually declare a winner
    winner = max(candidate_votes)
    winner_index = candidate_votes.index(winner)
    most_votes = all_candidates[winner_index]
# Print the percentage totals
print(percentage)
# Declare who the winner is based on the moste votes
print(max(winner))