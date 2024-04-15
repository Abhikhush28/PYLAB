# Exercise 3: Generate 6 digit random secure OTP

import random
otp = random.randrange(100000, 999999)
print("The 6 digit OTP: ", otp)