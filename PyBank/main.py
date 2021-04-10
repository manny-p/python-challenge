# import modules
import csv
import os
import statistics

# define paths
filename = os.path.join('Resources', 'budget_data.csv')
output = os.path.join('Analysis', 'output.txt')

# read csv
with open(filename) as f:
    reader = csv.reader(f, delimiter=',')
    skip_header = next(reader)

    # initialize variables
    total_months = []
    net_profits_loss = []
    delta_profits_loss = []

    # loop / append values to lists
    for row in reader:
        total_months.append(row[0])
        net_profits_loss.append(int(row[1]))

# calculate total profits & losses
total_profit_loss: int = 0
for i in net_profits_loss:
    total_profit_loss = i + total_profit_loss

# use list comprehension to create new list
# new_list = [expression for_loop_one_or_more conditions]
delta_profits_loss = [net_profits_loss[i + 1] - net_profits_loss[i] for i in range(0, len(net_profits_loss) - 1)]

# calculate average
delta_mean = round(statistics.mean(delta_profits_loss), 2)

# insert given element at given index (index, element)
delta_profits_loss.insert(0, 0)

# calculate max / min for profits/loss & dates
max_profits_delta = max(delta_profits_loss)
increase_date = total_months[delta_profits_loss.index(max_profits_delta)]

min_profits_delta = min(delta_profits_loss)
decrease_date = total_months[delta_profits_loss.index(min_profits_delta)]

separator = '-------------------------'
tm = f'Total Months: {len(total_months)}'
tpl = f'Total: ${total_profit_loss:,}'
dm = f'Average Change: ${delta_mean:,}'
increase = f'Greatest Increase in Profits: {increase_date} (${max_profits_delta:,})'
decrease = f'Greatest Decrease in Profits: {decrease_date} (${min_profits_delta:,})'

print('Financial Analysis', separator, tm, tpl, dm, increase, decrease, sep='\n')


