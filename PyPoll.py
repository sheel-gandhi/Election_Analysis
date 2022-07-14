# We need to retrieve data
# 1. Find total number of votes cast
# 2. List of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candiates won
# 5. Winner of election based on popular vote


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election resuls and read the file
with open(file_to_load) as election_data:   
    file_reader = csv.reader(election_data)


    with open(file_to_save, "w") as txt_file:

        headers = next(file_reader)
        print(headers)
