import random

score = 0
for i in range(5):
  a = random.randint(1, 10)
  b = random.randint(1, 10)
  c = int(input(str(a) + "+" + str(b) + " = "))
  if c == a + b:
    score = score + 1
print("Your score: " + str(score))
