import random
import time
from possibility import POSSIBLE_RESPONSES

input("Ask your question to the magic d100 8-ball: ")
print("The 8-ball is thinking")
for i in range(3):
    time.sleep(1)
    print(".")

index = random.randrange(0, 99)
print('\nThe d100 8-ball says: ' + POSSIBLE_RESPONSES[index])

