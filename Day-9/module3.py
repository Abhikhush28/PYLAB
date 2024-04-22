import os
directory = "ABHISHEK_TRAINee"
parent_dir = "D:/Pylab/"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "Geeks"
parent_dir = "D:/pylab"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
