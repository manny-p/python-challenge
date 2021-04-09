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
    vote_count = []
    vote_percent = []
    vote_total = 0
    candidate = []
    winner = []

    for column in reader:
        vote_count.append(column[0])
        candidate.append(column[2])

        vote_total = (len(vote_count))

        print(vote_total)
