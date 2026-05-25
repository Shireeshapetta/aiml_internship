import tkinter as tk
from tkinter import ttk, messagebox

# Interview stages and progress
stages = {
    "Scheduled": 10,
    "Screening": 25,
    "Technical Round": 50,
    "HR Round": 80,
    "Completed": 100,
    "Incomplete": 0
}

# Function to track interview
def track_interview():

    name = name_entry.get()
    interview_id = id_entry.get()
    status = status_var.get()

    if name == "" or interview_id == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    progress = stages[status]

    result_text.set(
        f"Candidate: {name}\n"
        f"Interview ID: {interview_id}\n"
        f"Current Status: {status}\n"
        f"Progress: {progress}%"
    )

    progress_bar["value"] = progress

    # Log events
    with open("events.txt", "a") as file:
        file.write(
            f"Candidate: {name}, "
            f"Interview ID: {interview_id}, "
            f"Status: {status}, "
            f"Progress: {progress}%\n"
        )

# Main Window
root = tk.Tk()
root.title("Interview Lifecycle Tracker")
root.geometry("500x500")

# Candidate Name
tk.Label(root, text="Candidate Name").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Interview ID
tk.Label(root, text="Interview ID").pack(pady=5)
id_entry = tk.Entry(root, width=40)
id_entry.pack(pady=5)

# Status Dropdown
tk.Label(root, text="Interview Status").pack(pady=5)

status_var = tk.StringVar()

status_dropdown = ttk.Combobox(
    root,
    textvariable=status_var,
    values=list(stages.keys())
)

status_dropdown.current(0)
status_dropdown.pack(pady=5)

# Button
track_button = tk.Button(
    root,
    text="Track Interview",
    command=track_interview
)

track_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate"
)

progress_bar.pack(pady=20)

# Result
result_text = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=result_text,
    justify="left"
)

result_label.pack(pady=10)

# Run App
root.mainloop()