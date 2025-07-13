from tkinter import Tk
from tkinterweb import HtmlFrame

# Initialize the main window
root = Tk()

# Create an HTMLFrame
frame = HtmlFrame(root)
frame.pack(fill="both", expand=True)

# Load a webpage
frame.load_website("https://www.google.com")

# Function to retrieve the current URL
def get_current_url():
    print(frame.webview.url)  # Get the current URL from the webview

# Add a button or trigger the function
root.after(3000, get_current_url)  # Example: Check URL after 3 seconds

root.mainloop()