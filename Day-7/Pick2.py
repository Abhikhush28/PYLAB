# [11:00 AM] N Murugadoss (Unverified)
import pickle
 
# load the data from a file

with open('person.pickle', 'rb') as f:

	data = pickle.load(f)
 
# print the data

print(data)
