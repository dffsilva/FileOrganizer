import tkinter as tk
from tkinter import filedialog

def browse_path(is_file=True):
    """Browse for a file or directory and update the corresponding label."""
    if is_file:
        path = filedialog.askopenfilename()
        if path:
            selected_file.set(path)
    else:
        path = filedialog.askdirectory()
        if path:
            selected_directory.set(path)

# Create the main window
root = tk.Tk()
root.title("File Explorer")

def create_label_and_button(text, command):
    """Helper function to create a label and a button for browsing."""
    var = tk.StringVar()
    label = tk.Label(root, textvariable=var, font=('Helvetica', 12))
    label.pack(pady=10)
    
    button = tk.Button(root, text=text, font=('Helvetica', 12), command=command)
    button.pack()
    
    return var

# Create labels and buttons for browsing files and directories
selected_file = create_label_and_button("Browse File", lambda: browse_path(is_file=True))
selected_directory = create_label_and_button("Browse Directory", lambda: browse_path(is_file=False))

# Start the GUI main loop
root.mainloop()