#The data we need to retrieve
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. Winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader) 
    print(headers)


#Use the open statement to open the file as a text file.
with open(file_to_save, 'w') as txt_file:

    # Write some data to the file.
    txt_file.write('Counties in the Election\n')
    txt_file.write('-------------------------\n')
    txt_file.write('Arapahoe\nDenver\nJefferson')

    




