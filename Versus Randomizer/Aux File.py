import tkinter as tk


def base_display_pairings(pairings):
    
    """
    Display Pairings:
        - Will simply show the results
    """
    
    # Create the window for displaying pairings
    pairings_window = tk.Tk()
    pairings_window.title("Final Pairings")

    # Set the size and position of the window
    window_width = 250
    window_height = 400
    window_position_x = (pairings_window.winfo_screenwidth() - window_width) // 2
    window_position_y = (pairings_window.winfo_screenheight() - window_height) // 3

    pairings_window.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")


    # Title Label
    label = tk.Label(pairings_window, text="Final Pairings", font=("Helvetica", 16))
    label.pack(pady=10)

    for i in range(len(pairings)):

        pair_label = tk.Label(pairings_window, text=f"{pairings[i][0]}  vs  {pairings[i][1]}", font=("Helvetica", 10))
        pair_label.pack(pady=0)


    # Function to close the process
    def close_window():
        pairings_window.destroy()

    # Close Window Button
    close_button = tk.Button(pairings_window, text="  Close  ", command = lambda: close_window())
    close_button.pack(pady=10)


    # Start the GUI event loop for this window
    pairings_window.mainloop()


# Dummy input
string = 'ABCDEFGHIJKLMNOPQRSTUVWXABCDEFGHIJ'
player_names = [char for char in string]
pairings = [(player_names[i], player_names[i + 1]) for i in range(0, len(player_names), 2)]

# base_display_pairings(pairings)





def grid_display_pairings(pairings):
    
    """
    Display Pairings:
        - Will simply show the results
    """
    
    # Create the window for displaying pairings
    pairings_window = tk.Tk()
    pairings_window.title("Final Pairings")

    # Set the size and position of the window
    window_width = 250
    window_height = 400
    window_position_x = (pairings_window.winfo_screenwidth() - window_width) // 2
    window_position_y = (pairings_window.winfo_screenheight() - window_height) // 3

    pairings_window.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")

    # Set row and column weights to distribute extra space
    for i in range(4):  # For title, pairings, scrollbar, and button
        pairings_window.grid_rowconfigure(i, weight=1)
        pairings_window.grid_columnconfigure(0, weight=1)
        pairings_window.grid_columnconfigure(1, weight=1)


    # Title Label
    label = tk.Label(pairings_window, text="Final Pairings", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    # Create a canvas with a scrollbar
    canvas = tk.Canvas(pairings_window)
    scrollbar = tk.Scrollbar(pairings_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Grid the canvas and scrollbar
    canvas.grid(row=1, column=1, sticky="nsew")
    scrollbar.grid(row=1, column=2, sticky="ns")

    # Create a frame inside the canvas to hold the widgets
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")


    for i in range(len(pairings)):

        # name1 = pairings[i][0]
        # name2 = pairings[i][1]

        pair_label = tk.Label(inner_frame, text=f"{pairings[i][0]}  vs  {pairings[i][1]}", font=("Helvetica", 10))
        pair_label.grid(row=i, column=0, pady=0, padx=(0,10), sticky='ew')


    # Function to close the process
    def close_window():
        pairings_window.destroy()

    # Close Window Button
    close_button = tk.Button(pairings_window, text="  Close  ", command = lambda: close_window())
    close_button.grid(row=3, column=0, columnspan=2, pady=20)


    # Configure the canvas to update scroll region
    pairings_window.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Bind the canvas to the scrollbar
    canvas.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))



    # Start the GUI event loop for this window
    pairings_window.mainloop()


# Dummy input
string = 'ABCDEFGHIJKLMNOPQRSTUVWXABCDEFGHIJ'
player_names = [char for char in string]
pairings = [(player_names[i], player_names[i + 1]) for i in range(0, len(player_names), 2)]

# grid_display_pairings(pairings)









def edited_display_pairings(pairings):
    
    """
    Display Pairings:
        - Will simply show the results
    """
    
    # Create the display pairings window
    pairings_window = tk.Tk()
    pairings_window.title("Final Pairings")

    # Set the size and position of the window
    window_width = 300
    window_height = 400
    window_position_x = (pairings_window.winfo_screenwidth() - window_width) // 2
    window_position_y = (pairings_window.winfo_screenheight() - window_height) // 3

    pairings_window.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")

    # Set row and column weights to distribute extra space
    for i in range(4):  # For title, pairings, scrollbar, and button
        pairings_window.grid_rowconfigure(i, weight=1)
        pairings_window.grid_columnconfigure(0, weight=1)
        pairings_window.grid_columnconfigure(1, weight=1)

    # Title Label
    title_label = tk.Label(pairings_window, text="Final Pairings", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Create a canvas with a scrollbar
    canvas = tk.Canvas(pairings_window)
    scrollbar = tk.Scrollbar(pairings_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Grid the canvas and scrollbar
    canvas.grid(row=1, column=1, sticky="nsew")
    scrollbar.grid(row=1, column=2, sticky="ns")

    # Create a frame inside the canvas to hold the widgets
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Display pairings
    for i, pairing in enumerate(pairings, start=1):
        pair_label = tk.Label(inner_frame, text=f"{pairing[0]} vs {pairing[1]}", font=("Helvetica", 10))
        pair_label.grid(row=i, column=0, pady=1, sticky="w")

    # Function to close the window
    def close_window():
        pairings_window.destroy()

    # Close Window Button
    close_button = tk.Button(pairings_window, text="  Close  ", command=close_window)
    close_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Configure the canvas to update scroll region
    pairings_window.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    # Start the GUI event loop for this window
    pairings_window.mainloop()



# Dummy input
string = 'ABCDEFGHIJKLMNOPQRSTUVWXABCDEFGHIJ'
player_names = [char for char in string]
pairings = [(player_names[i], player_names[i + 1]) for i in range(0, len(player_names), 2)]

edited_display_pairings(pairings)