import csv
import os
# Define File Path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# 1. Get total number of votes
# 2. Get the complete list of candidates who received votes
# 3. Get the percentage of votes of each candidate received
# 4. Get the total number of votes each candidate received
# 5. Define the winner of the election