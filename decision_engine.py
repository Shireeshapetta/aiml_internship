import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Decision Logic ----------
def evaluate():

    try:
        c = int(correctness_entry.get())
        d = int(depth_entry.get())
        cl = int(clarity_entry.get())

        difficulty = difficulty_box.get()
        qcount = int(question_entry.get())

        if c < 0 or d < 0 or cl < 0 or c > 10 or d > 10 or cl > 10:
            messagebox.showerror("Error", "Scores must be between 0 and 10")
            return

        avg = (c + d + cl) / 3

        if max(c, d, cl) - min(c, d, cl) >= 5:
            action = "FOLLOW UP"
            next_diff = difficulty
            reason = "Inconsistent scores detected"
            color = "orange"

        elif avg >= 8:
            action = "INCREASE DIFFICULTY"

            if difficulty == "easy":
                next_diff = "medium"
            elif difficulty == "medium":
                next_diff = "hard"
            else:
                next_diff = "hard"

            reason = "Excellent performance"
            color = "green"

        elif avg >= 6:
            action = "CONTINUE SAME LEVEL"
            next_diff = difficulty
            reason = "Stable performance"
            color = "blue"

        elif avg >= 4:
            action = "FOLLOW UP"
            next_diff = difficulty
            reason = "Need more probing"
            color = "orange"

        else:
            action = "SWITCH TOPIC"
            next_diff = "easy"
            reason = "Very low score"
            color = "red"

        result_label.config(
            fg=color,
            text=f"Average Score : {avg:.2f}\n\n"
                 f"Action : {action}\n"
                 f"Next Difficulty : {next_diff}\n"
                 f"Reason : {reason}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid inputs")


# ---------- Reset ----------
def reset():
    correctness_entry.delete(0, tk.END)
    depth_entry.delete(0, tk.END)
    clarity_entry.delete(0, tk.END)
    question_entry.delete(0, tk.END)
    difficulty_box.current(1)
    result_label.config(text="", fg="black")


# ---------- UI ----------
root = tk.Tk()
root.title("Decision Engine Dashboard")
root.geometry("550x650")
root.config(bg="#1e1e2f")

title = tk.Label(root,
                 text="Decision Engine Core Logic",
                 font=("Arial", 20, "bold"),
                 fg="white",
                 bg="#1e1e2f")
title.pack(pady=20)

frame = tk.Frame(root, bg="#2d2d44", padx=20, pady=20)
frame.pack(pady=10)

# Labels + Entries
labels = ["Correctness (0-10)", "Depth (0-10)", "Clarity (0-10)", "Question Count"]

entries = []

for text in labels:
    tk.Label(frame, text=text, fg="white", bg="#2d2d44",
             font=("Arial", 11)).pack(anchor="w", pady=5)

    e = tk.Entry(frame, width=30, font=("Arial", 11))
    e.pack(pady=3)
    entries.append(e)

correctness_entry = entries[0]
depth_entry = entries[1]
clarity_entry = entries[2]
question_entry = entries[3]

# Difficulty Dropdown
tk.Label(frame, text="Current Difficulty",
         fg="white", bg="#2d2d44",
         font=("Arial", 11)).pack(anchor="w", pady=5)

difficulty_box = ttk.Combobox(frame,
                              values=["easy", "medium", "hard"],
                              state="readonly",
                              width=27)
difficulty_box.pack(pady=5)
difficulty_box.current(1)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

tk.Button(btn_frame,
          text="Evaluate",
          command=evaluate,
          bg="green",
          fg="white",
          width=15,
          font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10)

tk.Button(btn_frame,
          text="Reset",
          command=reset,
          bg="red",
          fg="white",
          width=15,
          font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10)

# Result Box
result_label = tk.Label(root,
                        text="",
                        font=("Arial", 13, "bold"),
                        bg="#1e1e2f",
                        justify="left")
result_label.pack(pady=30)

root.mainloop()