import secrets

# Getting systemRandom class instance  out of secrets modules
secretsGenerator = secrets.SystemRandom()

# secure random integer numbers
random_number = secretsGenerator.randint(0, 50)
# print(random_number)

# secure random integer numbers within given
random_number2 = secretsGenerator.randrange(0, 40, 3)
# print(random_number2)

# Secure Random choice using secrets
number_list = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
# secure_choice = secretsGenerator.choice(number_list)
secure_choice = secretsGenerator.sample(number_list, 3)
# print(secure_choice)

# Secure Random float number 
secure_float = secretsGenerator.uniform(2.5, 25.5)
# print(secure_float)

# Generate a secure random integer number
random_integer = secrets.randbelow(100) # random number generate below 100
# print(random_integer)


# returns a secure unsigned integer with k random bits
# print(secrets.randbits(5))

# Return a secure random byte string
list = [1,2,4,5,66,]
print(secrets.token_bytes([nbytes=list]))
