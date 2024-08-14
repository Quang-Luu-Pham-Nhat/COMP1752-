import tkinter as tk
from tkinter import ttk
import json

import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos

# Load translations
with open('languages.json', 'r', encoding='utf-8') as file:
    translations = json.load(file)

current_language = 'en'  # Default language

def set_language(event):
    global current_language
    selected_language = language_combobox.get()
    current_language = 'en' if selected_language == "English" else 'vi'
    update_language()

def update_language():
    language_label.config(text=translations[current_language]["choose_language"])
    header_lbl.config(text=translations[current_language]["select_option"])
    check_videos_btn.config(text=translations[current_language]["check_videos"])
    create_video_list_btn.config(text=translations[current_language]["create_video_list"])
    update_videos_btn.config(text=translations[current_language]["update_videos"])

def check_videos_clicked():
    status_lbl.configure(text=translations[current_language]["check_videos_clicked"])
    CheckVideos(tk.Toplevel(window))

def create_video_list_clicked():
    status_lbl.configure(text=translations[current_language]["create_video_list_clicked"])
    CreateVideoList(tk.Toplevel(window))

def update_videos_clicked():
    status_lbl.configure(text=translations[current_language]["update_videos_clicked"])
    UpdateVideos(tk.Toplevel(window))

window = tk.Tk()
window.geometry("520x200")
window.title("Video Player")

fonts.configure()

# Language switch combobox with label
language_frame = tk.Frame(window)
language_frame.grid(row=0, column=0, columnspan=3, pady=10, sticky="w")

language_label = tk.Label(language_frame, text="", font=("Helvetica", 10))
language_label.grid(row=0, column=0, padx=5)

language_combobox = ttk.Combobox(language_frame, values=["English", "Tiếng Việt"], font=("Helvetica", 10))
language_combobox.set("English" if current_language == 'en' else "Tiếng Việt")
language_combobox.bind("<<ComboboxSelected>>", set_language)
language_combobox.grid(row=0, column=1, padx=5)

header_lbl = tk.Label(window, text="")
header_lbl.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="", command=check_videos_clicked)
check_videos_btn.grid(row=2, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="", command=create_video_list_clicked)
create_video_list_btn.grid(row=2, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="", command=update_videos_clicked)
update_videos_btn.grid(row=2, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

update_language()  # Initialize with default language

window.mainloop()
