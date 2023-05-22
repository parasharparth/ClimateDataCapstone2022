import tkinter as tk
import getpass

# Create a Tkinter window
window = tk.Tk()

# Set the window title
window.title("User Session Details")

# Get the username and hostname
username = getpass.getuser()
hostname = getpass.gethostname()

# Create labels for the username and hostname
username_label = tk.Label(window, text=f"Username: {username}")
hostname_label = tk.Label(window, text=f"Hostname: {hostname}")

# Pack the labels into the window
username_label.pack()
hostname_label.pack()

# Run the main loop to display the window
window.mainloop()