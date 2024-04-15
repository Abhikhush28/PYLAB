
# Q4
# Count the Votes
# Let’s try counting the number of occurrences in a list. The list below represent the results of 
# a poll where students were asked for their favorite programming language:


poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]

# Initialize an empty dictionary to store counts
vote_counts = {}

# Count the occurrences of each language
for language in poll_results:
    if language in vote_counts:
        vote_counts[language] += 1
    else:
        vote_counts[language] = 1

# Print the vote counts
for language, count in vote_counts.items():
    print(f"{language}: {count}")


