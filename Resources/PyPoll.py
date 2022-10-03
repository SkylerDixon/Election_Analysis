#The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies 
import csv 

import os 

import random

import numpy


# Assign a variable for the file to load and the path. 

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path. 

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file. 

with open(file_to_load) as election_data:
    
    

    # To do: read and analyze the data here. 

# Read the file object with the reader function. 

    file_reader = csv.reader(election_data) 

# Print the header row.  

    headers = next(file_reader) 

    print(headers) 

# Using the open () function with the "w" mode we will write data to this file. 

open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file. 

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file. 

with open(file_to_save, "w") as txt_file:

    # Write some data to the file. 

    txt_file.write("Hello World") 

# Write three counties to the file. 
 
    txt_file.write("Arapahoe, ") 

    txt_file.write("Denver, ") 

    txt_file.write("Jefferson, ") 


