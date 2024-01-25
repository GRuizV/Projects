import random
import time
import tkinter as tk




def display_pairings(pairings):
    
    """
    Display Pairings:

        - Will simply show the results
    """
    

    # Create the window for displaying pairings
    pairings_window = tk.Tk()
    pairings_window.title("Final Pairings")

    # Label for pairings
    label = tk.Label(pairings_window, text="Final Pairings", font=("Helvetica", 16, "bold"))
    label.pack(pady=10)

    # Display pairings
    for pairing in pairings:
        pair_label = tk.Label(pairings_window, text=f"{pairing[0]} vs {pairing[1]}")
        pair_label.pack()

    # Start the GUI event loop for this window
    pairings_window.mainloop()


def randomize_players(player_names):

    """
    This is simply the randomizing logic
    """

    random.shuffle(player_names)
    pairings = [(player_names[i], player_names[i + 1]) for i in range(0, len(player_names), 2)]
    display_pairings(pairings)




def num_players_window():
    
    """
    Number of Players Window:

        - After clicking the "Start Match" button, it will close the main menu window.
        - Will open a new window asking for the number of players participating.
        - Will include an entry field for the user to input the number.
        - Will Provide a button to proceed to the next step.
    """

    # Create the number of players window
    num_players_window = tk.Tk()
    num_players_window.title("Enter Number of Players")

    # Label and Entry for the number of players
    label = tk.Label(num_players_window, text="Enter the number of players:")
    label.pack(pady=10)

    entry = tk.Entry(num_players_window)
    entry.pack(pady=10)

    # Button to proceed to entering names
    proceed_button = tk.Button(num_players_window, text="Proceed", command=lambda: enter_names_window(int(entry.get())))
    proceed_button.pack(pady=20)

    # Start the GUI event loop for this window
    num_players_window.mainloop()


def enter_names_window(num_players):
   
    """
    Enter Player Names Window:

        - After entering the number of players, it will close the number of players window.
        - Will Open a new window with entry fields for each player's name.
        - Will include an entry field for the user to input the number.
        - Will Include a button to save the names and proceed to the randomization.
    """


    # Create the enter names window
    names_window = tk.Tk()
    names_window.title("Enter Player Names")

    # Set the size of the window
    window_width = 300
    window_height = 400
    window_position_x = (names_window.winfo_screenwidth() - window_width) // 2
    window_position_y = (names_window.winfo_screenheight() - window_height) // 2

    names_window.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")



    # Create a frame inside the canvas to hold the widgets
    frame = tk.Frame(names_window)
    frame.pack(expand=True, fill='both')


    # Create a canvas with a scrollbar
    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Create a frame inside the canvas to hold the widgets
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=inner_frame, anchor="nw")


    # Label and Entry for each player
    player_labels = []
    player_entries = []

    # Title
    txt = "Players Names"
    txt_len = len(txt)+6
    title_label = tk.Label(inner_frame, text=f"{txt:^{txt_len}}", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    for i in range(1, num_players + 1):

        label = tk.Label(inner_frame, text=f"Enter name for Player {i}:")
        entry = tk.Entry(inner_frame)

        player_labels.append(label)
        player_entries.append(entry)

        label.pack(pady=5, anchor= "center")
        entry.pack(pady=5, anchor= "center")

    # Button to save names and proceed to randomization
    save_button = tk.Button(inner_frame, text="Save Names", command=lambda: randomization_window([entry.get() for entry in player_entries]))
    save_button.pack(pady=20, side=tk.BOTTOM)
   
    # Configure the canvas to update scroll region
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Bind the canvas to the scrollbar
    canvas.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))


    # Start the GUI event loop for this window
    names_window.mainloop()

enter_names_window(8)






def randomization_window(player_names):
    
    """
    Randomization Window:

        - Will Perform the randomization logic.
        - Will Open a new window with entry fields for each player's name.
        - Will Display the match outcomes.
        - Will Include a button to close the window or start over.
    """

    # Create the randomization window
    randomization_window = tk.Tk()
    randomization_window.title("Randomization Results")

    # Button to start randomization
    randomize_button = tk.Button(randomization_window, text="Randomize Players", command=lambda: randomize_players(player_names))
    randomize_button.pack(pady=20)

    # Start the GUI event loop for this window
    randomization_window.mainloop()




def main_menu():

    """
    Main Menu Window:

        - Will display the title.
        - Will show a brief description of what the randomizer does.
        - Will have a button to start the randomization process.
    """

    # Creating the main menu window
    menu_window = tk.Tk()
    menu_window.title("Versus Match Randomizer")

    # Title
    txt = "Versus Match Randomizer"
    txt_len = len(txt)+6
    title_label = tk.Label(menu_window, text=f"{txt:^{txt_len}}", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    # Description
    description_label = tk.Label(menu_window, text="Welcome!\n This is a randomizer to help you pair versus matches.", wraplength=200)
    description_label.pack(pady=10)

    # Start Match button
    start_button = tk.Button(menu_window, text="Start Match", command=lambda: enter_names_window(4), padx=10, pady=5)  # You can change 4 to any default number of players
    
    start_button.pack(pady=20)

    # Starting the GUI event loop
    menu_window.mainloop()


# Calling the main menu func to run the app
# main_menu()

