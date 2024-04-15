# Write a Python program to find the  frequency of each  word  in a given text

def word_frequency(text):
 # Convert the text to lowercase and split it into words
 words = text.lower().split()

 # Create an empty  dictionary to store word frequency
 word_freq = {}


 #Iterate through each  word  in the list
 for word in words:
  #remove punctuation from words
  word = word.strip('.,!?')

  # check  if the word  is  already in the dictionary
  if word in word_freq:
   word_freq[word] +=1
  else:
   word_freq[word] =1 
 

 return word_freq



text = "Hello, how are you? Are you doing well? Hello there!"

frequency = word_frequency(text)


for word, freq in frequency.items():
 print(f"{word} : {freq}")

 # filter , reduce lamda 