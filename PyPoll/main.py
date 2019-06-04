import os
import csv
import collections

csvpath = os.path.join("election_data.csv")

voter_id = 0
total_votes =0
LastRow = 0
candidates = []
uniquecandidates = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next (csvreader)
    
    for row in csvreader:
        # count total votes
        voter_id += 1

        cands = row[2]
        candidates.append (row[2])

        if cands not in uniquecandidates:
            uniquecandidates.append(cands)
  
vote_counter = collections.Counter(candidates)

#create list of dict's keys and values and find key with max value
v=list(vote_counter.values())
k=list(vote_counter.keys())
winner = (k[v.index(max(v))])

print(f'Election Results')
print(f'------------------------------------')
print(f'Total Votes: {voter_id}')
print(f'------------------------------------')

s = sum(vote_counter.values())
for candidate, v in vote_counter.items():
    pct = v * 100.0 / s
    print(f'{candidate} : {pct:,.2f}% ({v})')
print(f'------------------------------------')
print(f'Winner: {winner}')
print(f'------------------------------------')

with open("Output.txt", "w") as text_file:
    text_file.write(f'Election Results\n')
    text_file.write(f'------------------------------------\n')
    text_file.write(f'Total Votes: {voter_id}\n')
    text_file.write(f'------------------------------------\n')
    text_file.write(f'{candidate} : {pct:,.2f}% ({v})\n')
    text_file.write(f'------------------------------------\n')    
    text_file.write(f'Winner: {winner}\n')
    text_file.write(f'------------------------------------\n')