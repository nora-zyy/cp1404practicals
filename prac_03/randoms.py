import random

print(random.randint(5, 20))  # line 1 The smallest number: 5 ,The largest number: 20
print(random.randrange(3, 10, 2))  # line 2 The smallest number: 3 ,The largest number: 9. Unable produced: 4.
print(random.uniform(2.5, 5.5))   # line 3 The smallest number: 2.5 ,The largest number: 5.5.

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))