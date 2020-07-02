# Pypoll

#analyze csv for:
#   total number of votes
#   complete list of candidates who recieved votes
#   percentage of votes each candidate won
#   total number of votes for each candidate
#   the winner of the election based on popular vote

import os
import csv
from operator import itemgetter

input_path = os.path.join("..","resources","election_data.csv")

vote_count = 0
candidates = []
khan_votes = 0
correy_votes = 0
li_votes = 0
Otooley_votes = 0
other_votes = 0


with open(input_path) as input_file:
    # create csv reader
    csvreader = csv.reader(input_file)
    # pull header from iterable data
    header = next(csvreader)
    for row in csvreader:
        #find total vote count
        vote_count = vote_count + 1
        #create list of candidates who recieved votes
        if row[2] not in candidates:
            candidates.append(row[2])
        #total votes for each candidate
        if row[2].lower() == "khan":
            khan_votes = khan_votes + 1
        elif row[2].lower() == "correy":
            correy_votes = correy_votes + 1
        elif row[2].lower() == "li":
            li_votes = li_votes + 1
        elif row[2].lower() == "o'tooley":
            Otooley_votes = Otooley_votes + 1
    #find percentage of votes recieved for each candidate
    khan_pct = "{:.3%}".format((khan_votes / vote_count))
    correy_pct = "{:.3%}".format(correy_votes / vote_count)
    li_pct = "{:.3%}".format(li_votes / vote_count)
    otooley_pct = "{:.3%}".format(Otooley_votes / vote_count)
    #find winner
    vote_list = [("Khan",khan_votes),("Correy",correy_votes),("Li",li_votes),("O'Tooley", Otooley_votes)]
    winner = max(vote_list, key = itemgetter(1))[0]

print(f"""Election Results
-----------------------------------
Total Votes: {vote_count}
-----------------------------------
Khan: {khan_pct}% ({khan_votes})
Correy: {correy_pct}% ({correy_votes})
Li: {li_pct}% ({li_votes})
O'Tooley: {otooley_pct}% ({Otooley_votes})
-----------------------------------
Winner: {winner}
-----------------------------------""")

output_path = os.path.join("output.csv")

with open(output_path, "w") as output_file:
    #convert to csv writer
    csvwriter = csv.writer(output_file)
    #add header row
    csvwriter.writerow(["Candidate","Percent of Total Vote","Total Vote Count"])
    #create lists to zip
    list1 = ["Khan","Correy","Li","O'Tooley"]
    list2 = [khan_pct, correy_pct, li_pct, otooley_pct]
    list3 = [khan_votes, correy_votes, li_votes, Otooley_votes]
    #zip files and add to spreadsheet
    zipped = zip(list1, list2, list3)
    csvwriter.writerows(zipped)
    #add another row with the winner
    csvwriter.writerow(["Winner:", winner])
