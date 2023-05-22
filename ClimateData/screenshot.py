from PIL import ImageGrab
import tkinter as tk
# Capture the entire screen
screenshot = ImageGrab.grab()

# Save the screenshot as a file
screenshot.save("screenshot.png")

# dimensional window save
window = tk.Tk()

#Screenshot from save state file
window.update()
x, y, width, height = window.winfo_rootx(), window.winfo_rooty(), window.winfo_width(), window.winfo_height()
screenshot = ImageGrab.grab(bbox=(x, y, x+width, y+height))

# Save the screenshot as a file
screenshot.save("save-screenshot.png")
