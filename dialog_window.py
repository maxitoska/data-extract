import tkinter as tk


def creating_a_dialog_box():
    # Initialize the result variable to None
    result = None

    # Define the function to be called when the OK button is clicked
    def ok_button_click():
        nonlocal result
        # Retrieve the value of the entry field
        date_str = date_var.get()

        # Check if the value is a string
        if type(date_str) == str:
            result = date_str
        else:
            result = True
        # Close the dialog box
        root.destroy()

    # Define the function to be called when the Cancel button is clicke
    def cancel_button_click():
        nonlocal result
        # Set the result variable to False
        result = False
        # Close the dialog box
        root.destroy()

    # Create a new root window
    root = tk.Tk()
    # Set the size of the window
    root.geometry("430x125")

    # Create a label with instructions for the user
    message = (
        "Please confirm adding the daily sync task to the Windows Scheduler\n"
        "or enter in the field the date by which you want to sort the example (02-04-2022)\n"
        "by default sort sorting will be by today's date"
    )
    label = tk.Label(root, text=message)
    label.pack(pady=10)

    # Create an entry field for the user to enter a date
    date_var = tk.StringVar()
    date_entry = tk.Entry(root, textvariable=date_var)
    date_entry.pack()

    # Create a frame to hold the OK and Cancel buttons
    frame = tk.Frame(root)
    frame.pack()

    # Create an OK button that will call the ok_button_click function
    ok_button = tk.Button(
        frame,
        text="OK",
        command=ok_button_click
    )
    ok_button.pack(side=tk.LEFT, padx=5)

    # Create a Cancel button that will call the cancel_button_click function
    cancel_button = tk.Button(
        frame, text="Cancel",
        command=cancel_button_click
    )
    cancel_button.pack(side=tk.RIGHT, padx=5)

    # Configure the window to call the cancel_button_click function when the user clicks the close button
    root.protocol("WM_DELETE_WINDOW", cancel_button_click)

    # Start the main event loop for the window
    root.mainloop()

    # Return the value of the result variable
    return result
