import tkinter as tk
from tkinter import ttk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Stopwatch")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variable to track time
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Time display
        self.time_label = tk.Label(self.root, text="00:00:00.00", font=("Arial", 30))
        self.time_label.pack(pady=20)

        # Buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=30)

        # Start button
        self.start_button = ttk.Button(
            button_frame, 
            text="Start", 
            command=self.start_timer,
            width=10
        )
        self.start_button.grid(row=0, column=0, padx=10)

        # Pause button
        self.pause_button = ttk.Button(
            button_frame, 
            text="Pause", 
            state="disabled",
            command=self.pause_timer,
            width=10
        )
        self.pause_button.grid(row=0, column=1, padx=10)

        # Reset button
        reset_button = ttk.Button(
            button_frame, 
            text="Reset", 
            command=self.reset_timer,
            width=10
        )
        reset_button.grid(row=0, column=2, padx=10)

        # Lap button
        lap_button = ttk.Button(
            self.root, 
            text="Record Lap", 
            command=self.record_lap,
            width=15
        )
        lap_button.pack(pady=5)

        # Lap times frame
        lap_frame = tk.Frame(self.root)
        lap_frame.pack()

        # Lap listbox
        scrollbar = tk.Scrollbar(lap_frame)
        self.lap_list = tk.Listbox(
            lap_frame, 
            yscrollcommand=scrollbar.set,
            height=5,
            width=45,
            font=("Arial", 10)
        )
        scrollbar.config(command=self.lap_list.yview)

        self.lap_list.pack(side=tk.LEFT)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def start_timer(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")

    def pause_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time
            self.start_button.config(state="normal")
            self.pause_button.config(state="disabled")

    def reset_timer(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00.00")
        self.lap_list.delete(0, tk.END)
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")

    def record_lap(self):
        if self.running or self.elapsed_time > 0:
            lap_time = self.time_label.cget("text")
            lap_number = self.lap_list.size() + 1
            self.lap_list.insert(tk.END, f"Lap {lap_number}: {lap_time}")

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            hours, rem = divmod(self.elapsed_time, 3600)
            minutes, rem = divmod(rem, 60)
            seconds = rem % 60
            formatted_time = f"{int(hours):02d}:{int(minutes):02d}:{seconds:05.2f}"
            self.time_label.config(text=formatted_time)
            self.root.after(10, self.update_time)

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
