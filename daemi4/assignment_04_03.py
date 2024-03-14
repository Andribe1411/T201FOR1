# Author: <Andri Benedikt>
# Date: <10-03-2024>
# Project: <assignment_04_03>
# Acknowledgements: <>


votes = {}
total_votes = 0

on = True
while on:
    user_input = input("Candidate and votes: ")
    if user_input == "":
        on = False
        break

    try:
        candidate, vote = user_input.rsplit(" ")
        vote = int(vote)
        candidate_key = candidate.lower()

        if candidate_key in votes:
            votes[candidate_key] += vote
        else:
            votes[candidate_key] = vote

        total_votes += vote

    except ValueError:
        print("Invalid no. of votes!")
        continue

# Printing the results
for candidate, vote in sorted(votes.items()):
    print(f"{candidate}: {vote}")
print(f"Total no. of votes: {total_votes}")

