
# celcius=[23,25,28,30,35,40,44,45]
 
# create new list fahren that contains temp in fahren , which are 100 and above.
 
# fah=cel*1.8+32

# fahren =[]

# def checkfahren():
#  for cel in celcius:
#   fah=cel*1.8+32
#   fahren.append(fah)

# newFahren = fahren.filter(lambda x:x>=100, fahren)

# print(list(newFahren))

# [9:59 AM] N Murugadoss (Unverified)
celcius=[23,25,28,30,35,40,44,45]

fah=filter(lambda x: (x*1.8+32)>=100 , celcius)

print(celcius)

print(list(fah))
