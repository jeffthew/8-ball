import random
import threading
import tkinter as tk
from possibility import *

root = tk.Tk()
root.title("100d 8-Ball")
root.minsize(1000, 750)
root.maxsize(1000, 750)
root.geometry("1000x750")

def respond(event=None):
    think_timer = threading.Timer(3.0, gen_response)
    think_timer.start()
    think()

def think():
    # Make the 8-ball think...
    index = random.randrange(0, 5)
    answer.config(text=POSSIBLE_THOUGHTS[index])

def gen_response(event=None):
    # Generate the actual response
    index = random.randrange(0, 99)
    entry.delete(0, tk.END)
    answer.config(text=POSSIBLE_RESPONSES[index])

def on_entry_click(event):
    if entry.get() == "Ask a question...":
        entry.delete(0, tk.END)
        entry.configure(foreground="black")

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Ask a question...")
        entry.configure(foreground="gray")

# Load the 8-ball image
image = tk.PhotoImage(file="images/Magic_eight_ball.png")
label = tk.Label(root, image=image).pack()

# Create prompt for the 8-ball
entry = tk.Entry(root, width=50, font=('Comic Sans MS', 20), foreground="gray")
entry.place(x=0, y=0)
entry.insert(0, "Ask a question...")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)
entry.bind("<Return>", respond)

# Create a button for the 8-ball
button = tk.Button(root, width=25, font=('Comic Sans MS', 0), text="Submit to the 8-ball", command=respond)
button.pack(side="bottom", pady=25)
entry.pack(side="bottom")

# Create an answer box from the 8-ball
answer = tk.Label(root, wraplength=800, font=('Comic Sans MS', 20), text="Speak your mind!")
answer.pack()

root.mainloop()
