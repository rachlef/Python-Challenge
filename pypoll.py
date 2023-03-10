import os
import csv

def read_a_csv(csvpath):
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        csv_header= next(csvreader)
        data=[]
        for row in csvreader:
            data.append(row)
    return data

def count_candidate_votes(data):
    candidate_vote_count= {}
    for row in data:
        candidate_name= row[2]
        if candidate_name in candidate_vote_count:
           candidate_vote_count[candidate_name]+=1
        else:
           candidate_vote_count[candidate_name] =1
    return candidate_vote_count

path=os.path.join('Resources', 'election_data.csv')
data= read_a_csv(path)
vote_counts= count_candidate_votes(data)
print(vote_counts)
total_votes= sum(vote_counts.values())
print(total_votes)


print("--------------------------")
print("Election Results")
print("--------------------------")
print(f"total votes:{total_votes}")
print("--------------------------")
winning_total=0
for key, value in vote_counts.items():
    print(f"{key}: {value} [{round((value/total_votes) *100, 3)}%)")
    if value >winning_total:
        winning_total=value
        winning_canidate= key
print("-------------------------")
print(f"Winner: {winning_canidate} with {winning_total} votes")
