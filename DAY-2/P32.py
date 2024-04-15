# Question 4:
# Sum the Scores
# Three friends are playing a game, where each player has three rounds to score. 
# At the end, the player whose total score (i.e. the sum of each round) is the highest wins.
# Consider the scores below (formatted as a list of tuples):
 
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('John', 8), ('Tom', 8), ('Tom', 9)]

total_scores = {}

# Calculate the total  score  for each  player
for player, score in scores:
 if player in total_scores:
   total_scores[player]+= score
 else:
  total_scores[player] = score


#Print  the total scores  for  each player

for player, total_score in total_scores.items():
 print(f"{player}: {total_score}")
