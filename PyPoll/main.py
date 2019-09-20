
import csv
file_to_load = "C:/Users/David/Desktop/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"
file_to_output= "Resources/election_data.txt"

#variables
vote_total = 0
candidates = []
candidate_votes = {}
winner = " "
winner_votes = {}

#csv format from class activities
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)
    #go throw each row, receiving error in "reader"
    for row in reader
    #total votes
        vote_total = vote_total + 1
    #select candidate name
        candidate_name = row[2]
    #if candidate name does not equal other names
    if candidate_name not in candidates:
        #add to list
        candidates.append(candidate_name)
        #count votes for the candidate
        candidate_votes[candidate_name] = 0
        #add up votes for the candidates
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    #go throw votes to get winner
    for candidate in candidate_votes
        #get votes an percents for candidates
        votes = candidate_votes.get(candidate)
        vote_percent = votes / vote_total *100
        #winner votes
        if (votes > winner_votes):
            winner_votes = votes
            winner = candidate 

    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(vote_total))
    print("-------------------------")
        for i in range(len(candidate)):
                print(candidate[i] + ": " + str(round(vote_percent[i],3)) +"% (" + str(round(candidate_votes[i],3)+ ")"))    
    print("Winner: ") + str(winner))
    
with open("C:/Users/David/Desktop/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv", "w") as text:
    text.write("Election Results")
    text.write("-------------------------")
    text.write("Total Votes: " + str(vote_total))
    text.write("-------------------------")
        for i in range(len(candidate)):
                print(candidate[i] + ": " + str(round(vote_percent[i],3)) +"% (" + str(round(candidate_votes[i],3)+ ")"))    
    text.write("Winner: ") + str(winner))