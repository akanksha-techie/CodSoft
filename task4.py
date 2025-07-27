import tkinter as tk
import random
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "You Lose!"
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's play!")
    score_label.congif(text="Score - You: 0 | Computer: 0")
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.resizable(False, False)
title = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetice", 16, "bold"))
title.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack()
rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
rock_btn.grid(row=0, column=0, padx=5, pady=5)
paper_btn.grid(row=0, column=1, padx=5, pady=5)
scissors_btn.grid(row=0, column=2, padx=5, pady=5)
result_label = tk.Label(root, text="Let's play!", font=("Helvetica", 12))
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=5)
reset_btn = tk.Button(root, text="Play Again", command=reset_game)
reset_btn.pack(pady=10)
root.mainloop()