import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda e: clear_placeholder(entry, placeholder))
    entry.bind("<FocusOut>", lambda e: add_placeholder(entry, placeholder))

def clear_placeholder(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def add_placeholder(entry, placeholder):
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(fg='grey')

class CheckVideos():
    def __init__(self, window):
        window.geometry("800x450")
        window.title("Check Videos")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=1, pady=5)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=1, pady=5)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Add video section
        add_video_lbl = tk.Label(window, text="Add New Video")
        add_video_lbl.grid(row=3, column=0, padx=10, pady=10)

        self.new_video_key = tk.Entry(window, width=10, fg='grey')
        self.new_video_key.grid(row=3, column=1, padx=10, pady=10)
        set_placeholder(self.new_video_key, "Key")

        self.new_video_name = tk.Entry(window, width=20, fg='grey')
        self.new_video_name.grid(row=3, column=2, padx=5, pady=10)
        set_placeholder(self.new_video_name, "Name")

        self.new_video_director = tk.Entry(window, width=20, fg='grey')
        self.new_video_director.grid(row=4, column=2, padx=5, pady=10)
        set_placeholder(self.new_video_director, "Director")

        self.new_video_rating = tk.Entry(window, width=10, fg='grey')
        self.new_video_rating.grid(row=4, column=1, padx=10, pady=10)
        set_placeholder(self.new_video_rating, "Rating")

        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=4, column=0, padx=10, pady=10)

        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def add_video_clicked(self):
        key = self.new_video_key.get()
        name = self.new_video_name.get()
        director = self.new_video_director.get()
        rating_str = self.new_video_rating.get()

        if lib.key_exists(key):
            self.status_lbl.configure(text="Error: Key already exists!")
            return

        try:
            rating = int(rating_str)
            if rating < 0 or rating > 5:  # Phạm vi rating từ 0 đến 5
                self.status_lbl.configure(text="Error: Rating must be between 0 and 5.")
                return
        except ValueError:
            self.status_lbl.configure(text="Error: Rating must be a valid integer.")
            return

        lib.add_video(key, name, director, rating)
        self.list_videos_clicked()
        self.status_lbl.configure(text="Add Video button was clicked!")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CheckVideos(window)
    window.mainloop()

