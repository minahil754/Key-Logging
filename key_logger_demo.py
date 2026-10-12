
import tkinter as tk
from datetime import datetime

LOG_FILE = "keystroke_demo.txt"


def log_keystroke(event):
    """Record keys pressed only inside this test window."""
    key = event.keysym

    # Do not record typed text; demonstrate key events only.
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Key pressed: {key}\n")

    status_label.config(text=f"Recorded key event: {key}")


def clear_input():
    test_input.delete(0, tk.END)
    test_input.focus_set()


root = tk.Tk()
root.title("Safe Key Logging Demonstration")
root.geometry("500x300")

heading = tk.Label(
    root,
    text="Key Logging — Safe Demonstration",
    font=("Arial", 15, "bold")
)
heading.pack(pady=12)

instructions = tk.Label(
    root,
    text="Type sample text in the box below.\n"
         "Only key events in this window are recorded.\n"
         "Do not enter passwords or private information.",
    justify="center"
)
instructions.pack(pady=5)

test_input = tk.Entry(root, width=45)
test_input.pack(pady=12)
test_input.bind("<KeyPress>", log_keystroke)
test_input.focus_set()

status_label = tk.Label(root, text="Ready for testing")
status_label.pack(pady=5)

clear_button = tk.Button(
    root, text="Clear Test Box", command=clear_input
)
clear_button.pack(pady=8)

root.mainloop()
