import random
# num,alp,ALp,sym variables have mixed values to create password
num = (7, 5, 9, 3, 1)
alp = ("a", "g", "h", "m", "l")
ALP = ("A", "I", "J", "N", "Q")
sym = ("@", "!", "~", "-", "#")
# first,second variables are randomly choose our values from variables(num,alp,ALp,sym)
first = str(random.choice(num)) + str(random.choice(alp)) + str(random.choice(sym)) + random.choice(ALP)
second = str(random.choice(sym)) + str(random.choice(num)) + str(random.choice(alp)) + random.choice(ALP)
password = first + second
print(f"Your Temporary Password is :{password}")
