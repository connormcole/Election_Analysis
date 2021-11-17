counties = ['Arapahoe', 'Denver', 'Jefferson']
"""
if "Arapahoe" in counties or "El Paso" in counties:
    print('Arapahoe or El Paso are in the list of counties')
else:
    print('Arapahoe and El Paso is not in the list of counties')
"""
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)