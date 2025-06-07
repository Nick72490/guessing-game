import tkinter as tk
import random 
                    
root = tk.Tk()
root.title("Number Guessing Game")

entry = tk.Entry(root)
entry.pack()

txt_label = tk.Label(root, text="Enter your guess above")
txt_label.pack()

random_number = random.randint(1,10)
attempts = 0

def check_guess(event=None):
    global attempts
    guess = entry.get()  
    guess_number = int(guess)
    attempts += 1 
    if guess_number < random_number:
        txt_label.config(text=f"higher")
    elif guess_number > random_number:
        txt_label.config(text=f"lower")
    elif guess_number == random_number:
        txt_label.config(text=f"you got it in {attempts} attempts {guess}")
        
button_quit = tk.Button(root, text="quit", command=quit)
button_quit.pack()

button = tk.Button(root, text="Guess", command=check_guess)
button.pack()

entry.bind("<Return>", check_guess) 

root.minsize(200, 40)

root.mainloop()
