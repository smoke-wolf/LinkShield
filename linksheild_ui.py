import tkinter as tk
from tkinter import ttk
import requests

# Function to check if the URL starts with http:// or https://
def url_checker(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        result_label.config(text="Invalid URL. Please use http or https.", foreground="red")
        return False
    return True

# Function to create a LinkShield URL
def create_linkshield_url():
    phishing_url = phishing_url_entry.get()
    mask = mask_entry.get()
    words = words_entry.get()

    if not url_checker(phishing_url) or not url_checker(mask):
        return

    response = requests.get(f"https://is.gd/create.php?format=simple&url={phishing_url}")
    short = response.text.strip()
    shorter = short.replace("https://", "")

    if not words:
        result_label.config(text="No words provided.", foreground="red")
        final_url = f"{mask}@{shorter}"
    elif ' ' in words:
        result_label.config(text="Invalid words. Please avoid spaces.", foreground="red")
        final_url = f"{mask}@{shorter}"
    else:
        final_url = f"{mask}-{words}@{shorter}"
    print(f"Here is the LinkShield URL:\n{final_url}")
    result_label.config(text=f"Here is the LinkShield URL:\n{final_url}", foreground="green")

# GUI Setup
root = tk.Tk()
root.title("LinkShield - URL Protection Tool")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

phishing_url_label = ttk.Label(mainframe, text="Phishing URL:")
phishing_url_label.grid(column=1, row=1, sticky="W")
phishing_url_entry = ttk.Entry(mainframe, width=50)
phishing_url_entry.grid(column=2, row=1, sticky=("W", "E"))

mask_label = ttk.Label(mainframe, text="Domain to mask the Phishing URL:")
mask_label.grid(column=1, row=2, sticky="W")
mask_entry = ttk.Entry(mainframe, width=50)
mask_entry.grid(column=2, row=2, sticky=("W", "E"))

words_label = ttk.Label(mainframe, text="Social engineering words separated by '-':")
words_label.grid(column=1, row=3, sticky="W")
words_entry = ttk.Entry(mainframe, width=50)
words_entry.grid(column=2, row=3, sticky=("W", "E"))

generate_button = ttk.Button(mainframe, text="Generate LinkShield URL", command=create_linkshield_url)
generate_button.grid(column=2, row=4, sticky="E")

result_label = ttk.Label(mainframe, text="", foreground="green")
result_label.grid(column=1, row=5, columnspan=2, sticky="W")

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

phishing_url_entry.focus()

root.mainloop()
