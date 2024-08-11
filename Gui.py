import tkinter as tk
from tkinter import messagebox
import subprocess

class MPDController:
    def __init__(self, root):
        self.root = root
        self.root.title("MPD Player")
        
        # Anzeige des aktuellen Titels
        self.song_label = tk.Label(root, text="Aktueller Titel: ", font=("Helvetica", 12))
        self.song_label.pack(pady=10)

        # Buttons zur Steuerung
        control_frame = tk.Frame(root)
        control_frame.pack()

        play_button = tk.Button(control_frame, text="Play", command=self.play)
        play_button.grid(row=0, column=0, padx=5)

        pause_button = tk.Button(control_frame, text="Pause", command=self.pause)
        pause_button.grid(row=0, column=1, padx=5)

        stop_button = tk.Button(control_frame, text="Stop", command=self.stop)
        stop_button.grid(row=0, column=2, padx=5)

        next_button = tk.Button(control_frame, text="Next", command=self.next_song)
        next_button.grid(row=0, column=3, padx=5)

        prev_button = tk.Button(control_frame, text="Prev", command=self.prev_song)
        prev_button.grid(row=0, column=4, padx=5)

        update_button = tk.Button(root, text="Update", command=self.update_song_info)
        update_button.pack(pady=10)

        self.update_song_info()

    def run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True).decode('utf-8').strip()
            return output
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Fehler", f"Fehler beim Ausführen von '{command}':\n{e.output.decode('utf-8')}")
            return None

    def update_song_info(self):
        current_song = self.run_command("mpc current")
        if current_song:
            self.song_label.config(text=f"Aktueller Titel: {current_song}")
        else:
            self.song_label.config(text="Aktueller Titel: -")

    def play(self):
        self.run_command("mpc play")
        self.update_song_info()

    def pause(self):
        self.run_command("mpc pause")

    def stop(self):
        self.run_command("mpc stop")
        self.song_label.config(text="Aktueller Titel: -")

    def next_song(self):
        self.run_command("mpc next")
        self.update_song_info()

    def prev_song(self):
        self.run_command("mpc prev")
        self.update_song_info()

if __name__ == "__main__":
    root = tk.Tk()
    app = MPDController(root)
    root.mainloop()
