import csv
import os
import statistics

filename = os.path.join('Resources', 'budget_data.csv')
output = os.path.join('Analysis','output.txt')

with open(filename) as f:
    reader = csv.reader(f, delimiter=',')
    skip_header = next(reader)

    total_months = 0
    total_net = 0
    delta = 0

    max_profit_date = "Jan-2010"
    max_profit_amount = 0

    max_loss_date = "Jan-2010"
    max_loss_amount = 0

    list_date = []
    list_net = []

    i = 0

    for line in reader:
        total_months += 1
        total_net += int(line[1])

        list_date.append(line[0])
        list_net.append(line[1])



