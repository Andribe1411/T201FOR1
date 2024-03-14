# Author: <Andri Benedikt>
# Date: <10-03-2024>
# Project: <assignment_04_04>
# Acknowledgements: <mikil hjálp frá chatGPT í b-lið>

votes = {}
collabaration = []
try:
    #filename = input('Filename: ')
    filename = "daemi4\eurovision04.txt"
    input_file = open(filename, 'r')

    for line in input_file:
        line = line.strip()
        giving_country,reciveing_country,points = line.rsplit(" ",2)
        collabaration.append([giving_country,reciveing_country,points])
        if reciveing_country in votes:
            votes[reciveing_country] += int(points)
        else:
            votes[reciveing_country] = int(points)
        
    max_votes = []
    max_votes_value = 0
    for x in sorted(votes):
        print(x, votes[x])
        if max_votes_value == []:
            max_votes_value.append(votes[x])
            max_votes.append(x)
        elif votes[x] > max_votes_value:
            max_votes = []
            max_votes_value =votes[x]
            max_votes.append(x)
        elif votes[x] == max_votes_value:
            max_votes.append(x)

    print("Winner:", ", ".join(max_votes))

    input_file.close()
    input_file = open(filename, 'r')
    collaborations = {}

    for line in input_file:
        giver, receiver, points = line.strip().split()
        points = int(points)
        
        key = tuple(sorted((giver, receiver)))
        
        if key in collaborations:
            collaborations[key] += points
        else:
            collaborations[key] = points

    collaborations_list = [(k[0], k[1], v) for k, v in collaborations.items()]

    unique_countries = set()
    for giver, receiver, _ in collaborations_list:
        unique_countries.update([giver, receiver])

    if len(unique_countries) >= 10:
        for i in range(len(collaborations_list) - 1):
            for j in range(0, len(collaborations_list) - i - 1):
                if collaborations_list[j][2] < collaborations_list[j + 1][2] or \
                (collaborations_list[j][2] == collaborations_list[j + 1][2] and collaborations_list[j][0] > collaborations_list[j + 1][0]):
                    collaborations_list[j], collaborations_list[j + 1] = collaborations_list[j + 1], collaborations_list[j]

    # Raða pörunum eftir stigafjölda í lækkandi röð og síðan í öfuga stafrófsröð ef stigafjöldi er sá sami
        sorted_collaborations = sorted(collaborations, key=lambda x: (-x[1], x[0][1], x[0][0]))

# Prenta út raðaða listann
        for pair in sorted_collaborations:
            print(pair)


except FileNotFoundError:
    print("Invalid filename")