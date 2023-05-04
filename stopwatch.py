import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        # Initialize variables
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        # Create GUI elements
        self.time_label = tk.Label(master, text="00:00.00", font=("Arial", 36))
        self.start_button = tk.Button(master, text="Start", command=self.start_stop)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset)

        # Add GUI elements to window
        self.time_label.pack()
        self.start_button.pack(side=tk.LEFT)
        self.reset_button.pack(side=tk.RIGHT)

    def start_stop(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update()
        else:
            self.running = False

    def update(self):
        self.elapsed_time = time.time() - self.start_time
        minutes = int(self.elapsed_time // 60)
        seconds = int(self.elapsed_time % 60)
        hundredths = int((self.elapsed_time % 1) * 100)
        time_string = f"{minutes:02d}:{seconds:02d}.{hundredths:02d}"
        self.time_label.config(text=time_string)
        if self.running:
            self.master.after(10, self.update)

    def reset(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.time_label.config(text="00:00.00")

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()