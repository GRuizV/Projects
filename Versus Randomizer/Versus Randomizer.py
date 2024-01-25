import random
import time
import tkinter as tk


def start_match():

    """
    This function holds the logic of the randomizing of the matches
    """

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



# Creating the main window
root = tk.Tk()
root.title('Versus Match Randomizer')


# Creating the label for the countdown
countdown_label = tk.Label(root, text="")
countdown_label.pack()


# Creating a button to start the match
start_button = tk.Button(root, text="Start Match", command = start_match)
start_button.pack()


# Start the GUI event loop
root.mainloop()