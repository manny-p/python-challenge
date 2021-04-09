# import modules
import csv
import os

# define paths

input_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', 'poll_results.txt')

# read csv
with open(input_path) as file:
    # add params
    reader = csv.reader(file, delimiter=',')

    # initialize variables

    vote_total = 0
    vote_percent = []
    candidate = []
    candidate_vote_count = []
    candidate_winner = []

    for column in reader:
        candidate_vote_count.append(column[0])
        candidate.append(column[2])

        vote_total = (len(candidate_vote_count))

    # calculate vote count per candidate
    correy_vote_count = candidate.count('Correy')
    li_vote_count = candidate.count('Li')
    khan_vote_count = candidate.count('Khan')
    o_tooley_vote_count = candidate.count("O'Tooley")

    # calculate vote % per candidate
    correy_vote_percent = correy_vote_count / vote_total
    li_vote_percent = li_vote_count / vote_total
    Khan_vote_percent = khan_vote_count / vote_total
    o_tooley_vote_percent = o_tooley_vote_count / vote_total


    print('Election Results')
    print('-------------------------')
    print(f'Total Votes:{vote_total:,}')
    print('-------------------------')




