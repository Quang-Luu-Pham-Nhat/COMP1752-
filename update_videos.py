import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos:
    def __init__(self, window):
        window.geometry("850x650")
        window.title("Update Videos")

        self.video_listbox = tk.Listbox(window, height=6, width=40)  # Increase the height of the Listbox
        self.video_listbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="NSW")

        self.code_label = tk.Label(window, text="Enter video code")
        self.code_label.grid(row=1, column=0, padx=(10, 0), pady=5, sticky="W")

        self.code_entry = tk.Entry(window)
        self.code_entry.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="W")

        self.rating_label = tk.Label(window, text="Enter new rating")
        self.rating_label.grid(row=2, column=0, padx=(10, 0), pady=5, sticky="W")

        self.rating_entry = tk.Entry(window)
        self.rating_entry.grid(row=2, column=1, padx=(0, 10), pady=5, sticky="W")

        self.update_button = tk.Button(window, text="Update Rating", command=self.update_rating, state=tk.DISABLED)
        self.update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        self.video_details_lbl = tk.Label(window, text="Video Details:")
        self.video_details_lbl.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.video_details_text = tkst.ScrolledText(window, width=60, height=10)
        self.video_details_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        self.update_video_listbox()

        # Trace changes in the entry widgets
        self.code_entry_var = tk.StringVar()
        self.rating_entry_var = tk.StringVar()
        self.code_entry.config(textvariable=self.code_entry_var)
        self.rating_entry.config(textvariable=self.rating_entry_var)
        self.code_entry_var.trace_add("write", self.check_entries)
        self.rating_entry_var.trace_add("write", self.check_entries)

    def update_video_listbox(self):
        videos = lib.list_all().splitlines()
        for video in videos:
            self.video_listbox.insert(tk.END, video)

    def update_rating(self):
        video_code = self.code_entry.get().strip()
        new_rating = self.rating_entry.get().strip()
        if video_code in lib.library:
            if new_rating.isdigit():
                new_rating = int(new_rating)
                if 0 <= new_rating <= 5:
                    lib.set_rating(video_code, new_rating)
                    self.update_video_details_display(video_code)
                else:
                    messagebox.showerror("Error", "Rating must be between 0 and 5.")
            else:
                messagebox.showerror("Error", "Please enter a valid number.")
        else:
            messagebox.showerror("Error", "Invalid video code. Please try again.")

    def update_video_details_display(self, key):
        name = lib.get_name(key)
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        details = f"Video: {name}\nDirector: {director}\nRating: {rating}"
        set_text(self.video_details_text, details)

    def check_entries(self, *args):
        if self.code_entry_var.get().strip() and self.rating_entry_var.get().strip():
            self.update_button.config(state=tk.NORMAL)
        else:
            self.update_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()  # Configure fonts if necessary
    UpdateVideos(window)
    window.mainloop()
