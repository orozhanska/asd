# Let’s try to invent a simple hashing function. 
# Your task will be to write a function that accepts
# a string and returns the sum of the ASCII values of the characters in the string 
# (i.e. the sum of the ord() of the characters) modulo 256.
# ● The function should return 0 if the string is empty.
# ● Strings will contain only letters (uppercase and lowercase) and digits, 
# without spaces and special characters.

def hash(some_str):
    output = sum([ord(x) for x in some_str]) % 256
    return output

# this is hash function will be full of collisions as 
# - the decimal representations of letters are incrementing by 1 unit. 
# so there are, for example, how many 2-symbol units is there with sum 200:
# if we consider elements from 65 to 122 (omitting the special 
# charachters in between)
# 122 + 78
# 121 + 79
# 120 + 80
# ...
# 78 + 122
# we have (122 - 77 - 6) * 2 = 39 * 2 = 78 diferent 2-symbol units which
#  will have the same sum of 200

# - also,  % will return the same vaue for even different sums:
# - there are words that contain same charachters but in the different order

# all this will lead to the collision
print(hash("kse"))
print(hash("Ozz"))

# we will need to go through each element in the string to calculte hash() 
# <- so the complexity is growing linearly

assert hash("kse") == 67, f"Results are different {hash('kse')} != 67"
assert hash("KSE") == 227, f"Results are different {hash('KSE')} != 227"  # Case-sensitive gives different results
assert hash("Algorithm2") == 217, f"Results are different {hash('Algorithm2')} != 217"
assert hash("") == 0, f"Results are different {hash('')} != 0"
