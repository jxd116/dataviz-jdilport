import csv

# Define the path of the input CSV file
csvpath = "c:/Users/jdilport/OneDrive - Prolink Staffing/Desktop/homework/dataviz-jdilport/Module_3_Python Challenge/PyPoll/analysis/election_data.csv"

# Define the path of the output text file
txtpath = "c:/Users/jdilport/OneDrive - Prolink Staffing/Desktop/homework/dataviz-jdilport/Module_3_Python Challenge/PyPoll/analysis/election_results.txt"


# Initialize variables to store results
total_votes = 0
candidate_votes = {}
candidates = []

# Open the CSV file and read the data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:

        # Count the total number of votes cast
        total_votes += 1
        
        # Add the candidate to the list of candidates if not already present
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        
        # Add the vote to the candidate's total vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes and total number of votes for each candidate
vote_percentages = {}
for candidate in candidates:
    vote_percentages[candidate] = round(candidate_votes[candidate] / total_votes * 100, 3)

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Generate the analysis string
analysis = "Election Results\n"
analysis += "-------------------------\n"
analysis += f"Total Votes: {total_votes}\n"
analysis += "-------------------------\n"
for candidate in candidates:
    analysis += f"{candidate}: {vote_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"
analysis += "-------------------------\n"
analysis += f"Winner: {winner}\n"
analysis += "-------------------------\n"

# Print the analysis to the terminal
print(analysis)

# Export the analysis report to a text file
with open(txtpath, "w") as txtfile:
    txtfile.write(analysis)