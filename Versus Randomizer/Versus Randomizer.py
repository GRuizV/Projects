import random
import time

# Competitors population
competitors = list()

no_comp = int(input('Enter the number of competitors: '))

for comp in range(no_comp):
    competitors.append(input(f'Enter the name of the # {comp+1} competitor: '))


# Creating and shuffling the positions to later pair the matches
positions = list(range(no_comp))
random.shuffle(positions)


# Signaling the user the matches pairing is about to start
print("\nRandomizing... Get Ready!\nIn...")

for i in range(3,0,-1):
    print(f'{i}')
    time.sleep(1)


# Outputting the results
print('\nHere are the matches:\n')

for match in range(no_comp//2):
    print(f'Match # {match+1}: {competitors[ positions[(2*match)] ]} vs {competitors[ positions[(2*match+1)] ]}')