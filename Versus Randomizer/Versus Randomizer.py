"Let's create a versus randomizer"

import random
import time

competitors = list()
no_comp = int(input('Enter the number of competitors: \n'))


for comp in range(no_comp):

    competitors.append(input(f'Enter the name of the # {comp+1} competitor: '))


positions = list(range(no_comp))

random.shuffle(positions)

matches = list()

print()

print("Randomizing... Get Ready!\nIn...")

for i in range(3,0,-1):
    print(f'{i}')
    time.sleep(1)

print()

print('Here are the matches:\n')

for match in range(no_comp//2):
    print(f'Match # {match+1}: {competitors[ positions[(2*match)] ]} vs {competitors[ positions[(2*match+1)] ]}')