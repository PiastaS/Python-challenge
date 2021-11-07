	import os, csv
	from pathlib import Path 
	
	# Assign the file location
	csv_file_path = Path("python-challenge", "PyPoll", "election_data.csv")
	
	# Declare the variables 
	total_votes = 0 
	khan_votes = 0
	correy_votes = 0
	li_votes = 0
	otooley_votes = 0
	
	# Open csv in default read mode
	with open(csv_file_path,newline="", encoding="utf-8") as elections:
	
	    # Store data under the csvreader
	    csvreader = csv.reader(elections,delimiter=",") 
	
	    # Skip the header for iterate the actual values
	    header = next(csvreader)     
	
	    # Iterate through each row in the csv
	    for row in csvreader: 
	
	        # Count the unique voter ID's
	        total_votes +=1

	        # Count the times four candidates appears and store in a list
	        if row[2] == "Khan": 
	            khan_votes +=1
	        elif row[2] == "Correy":
	            correy_votes +=1
	        elif row[2] == "Li": 
	            li_votes +=1
	        elif row[2] == "O'Tooley":
	            otooley_votes +=1
	
	# Make a dictionary out of the two lists we previously created 
	candidates = ["Khan", "Correy", "Li","O'Tooley"]
	votes = [khan_votes, correy_votes,li_votes,otooley_votes]
	
	# Zip the list of candidate(key) and total votes(value)
	# Return the winner using a max function of the dictionary 
	dict_candidates_and_votes = dict(zip(candidates,votes))
	key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
	

	# Print a the summary of the analysis
	khan_percent = (khan_votes/total_votes) *100
	correy_percent = (correy_votes/total_votes) * 100
	li_percent = (li_votes/total_votes)* 100
	otooley_percent = (otooley_votes/total_votes) * 100
	
	# Print the summary table
	print(f"Election Results")
	print(f"----------------------------")
	print(f"Total Votes: {total_votes}")
	print(f"----------------------------")
	print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
	print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
	print(f"Li: {li_percent:.3f}% ({li_votes})")
	print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
	print(f"----------------------------")
	print(f"Winner: {key}")
	print(f"----------------------------")
	
	# Output the files and assign the location and with the pathlib library
	output_file = Path("python-challenge", "PyPoll", "Election_Results.txt")
	
	with open(output_file,"w") as file:

	# Write methods to print to Elections_Results 
	    file.write(f"Election Results")
	    file.write("\n")
	    file.write(f"----------------------------")
	    file.write("\n")
	    file.write(f"Total Votes: {total_votes}")
	    file.write("\n")
	    file.write(f"----------------------------")
	    file.write("\n")
	    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
	    file.write("\n")
	    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
	    file.write("\n")
	    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
	    file.write("\n")
	    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
	    file.write("\n")
	    file.write(f"----------------------------")
	    file.write("\n")
	    file.write(f"Winner: {key}")
	    file.write("\n")
	    file.write(f"----------------------------")
