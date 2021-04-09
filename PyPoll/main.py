#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import modules
import csv
import os  


# In[2]:


# define paths
filename = os.path.join('Resources', 'election_data.csv')
output = os.path.join('Analysis', 'poll_results.txt')


# In[3]:


# with open(filename) as f:
#       for line in f:
#         print(line)

#     for line in f.readlines():
#         values = line.replace('\n','').split(',')
#         print(values)


# In[4]:


# read csv
with open(filename) as f:
    # add params
    reader = csv.reader(f, delimiter=',')
    
    # initialize variables
    vote_total = 0
    vote_percent = []
    candidate = []
    candidate_vote_count = []
    
    # skip header
    header = next(reader)
    
    for column in reader:
        candidate_vote_count.append(column[0])
        candidate.append(column[2])

    vote_total = (len(candidate_vote_count))
    


# In[5]:


# calculate vote count per candidate
correy_vote_count = candidate.count('Correy')
li_vote_count = candidate.count('Li')
khan_vote_count = candidate.count('Khan')
o_tooley_vote_count = candidate.count("O'Tooley")


# print(f'Correy Votes:{correy_vote_count: ,}')
# print(f'Li Votes:{li_vote_count: ,}')
# print(f'Khan Votes:{khan_vote_count: ,}')
# print(f"O'Tooley Votes:{o_tooley_vote_count: ,}")


# In[6]:


# calculate vote % per candidate
correy_vote_percent = correy_vote_count / vote_total
li_vote_percent = li_vote_count / vote_total
khan_vote_percent = khan_vote_count / vote_total
o_tooley_vote_percent = o_tooley_vote_count / vote_total

# print('{:.0%}'.format((correy_vote_percent)))
# print('{:.0%}'.format((li_vote_percent)))
# print('{:.0%}'.format((khan_vote_percent)))
# print('{:.0%}'.format((o_tooley_vote_percent)))

correy_vote_percent_formatted = '{:.0%}'.format((correy_vote_percent))
li_vote_percent_formatted = '{:.0%}'.format((li_vote_percent))
khan_vote_percent_formatted = '{:.0%}'.format((khan_vote_percent))
o_tooley_vote_percent_formatted = '{:.0%}'.format((o_tooley_vote_percent))

# print(correy_vote_percent_formatted, li_vote_percent_formatted, khan_vote_percent_formatted, o_tooley_vote_percent_formatted, sep='\n')


# In[7]:


# calculate winner using guard clause 

def is_winner(): 
    candidate_vote_count_results = [correy_vote_count, li_vote_count, khan_vote_count, o_tooley_vote_count]
    candidate_winner = max(candidate_vote_count_results)
    
    if candidate_winner == correy_vote_count:
        return('Winner: Correy')        
    if candidate_winner == li_vote_count:
        return('Winner: Li')
    if candidate_winner == khan_vote_count:
        return('Winner: Khan')
    if candidate_winner == o_tooley_vote_count:
        return("Winner: O'Tooley")

winner=is_winner

separator = '-------------------------'
        
correy = (f'Correy: {correy_vote_percent_formatted} ({correy_vote_count: ,})')
li = (f'Li: {li_vote_percent_formatted} ({li_vote_count: ,})')
khan = (f'Khan: {khan_vote_percent_formatted} ({khan_vote_count: ,})')
o_tooley = (f"O'Tooley: {o_tooley_vote_percent_formatted} ({o_tooley_vote_count: ,})")

vote_total_formatted = (f'Total Votes: {vote_total:,}')

print('Election Results', separator, vote_total_formatted, separator, khan, correy, li, o_tooley,separator, winner(),separator, sep='\n')



   



# In[8]:


# output 

with open('output.txt', 'w') as text_file:
          print('Election Results', separator, vote_total_formatted, separator, khan, correy, li, o_tooley,separator, winner(),separator, sep='\n', file=text_file)
    
          
    
    
    
    
    
    

