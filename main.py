
# -------------------------------------------------------------------------------------------

# Task-2 - word scramble

import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

selection = random.choice(words)

scrambled_word=''.join(random.sample(selection, len(selection)))

print(scrambled_word)

answer=input("answer the original word")

if (answer.lower()==selection.lower()):
    print("right answer")
else:
    print("wrong answer correct answer is ", selection)
