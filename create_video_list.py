import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateVideoList:
    def __init__(self, window):
        window.geometry("750x500")
        window.title("Create Video List")

        self.playlist = []
        self.selected_video_code = None  # Variable to store the selected video code

        self.label = tk.Label(window, text="Available Videos:")
        self.label.pack()

        self.video_listbox = tk.Listbox(window, selectmode=tk.SINGLE, height=1, width=10)
        self.video_listbox.pack(fill=tk.BOTH, expand=True)
        self.video_listbox.bind('<<ListboxSelect>>', self.on_video_select)

        self.update_video_listbox()

        self.entry_label = tk.Label(window, text="Enter video code:")
        self.entry_label.pack()

        self.entry = tk.Entry(window)
        self.entry.pack()

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(window)
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Add to Playlist", command=self.add_to_playlist)
        self.add_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.button_frame, text="Reset Playlist", command=self.reset_playlist)
        self.reset_button.pack(side=tk.LEFT)

        self.play_button = tk.Button(self.button_frame, text="Play Playlist", command=self.play_playlist)
        self.play_button.pack(side=tk.LEFT)

        self.playlist_label = tk.Label(window, text="Playlist:")
        self.playlist_label.pack()

        self.playlist_box = tkst.ScrolledText(window, width=40, height=5)
        self.playlist_box.pack()

        self.info_label = tk.Label(window, text="Video Information:")
        self.info_label.pack()

        self.info_box = tkst.ScrolledText(window, width=40, height=5)
        self.info_box.pack()

    def update_video_listbox(self):
        try:
            all_videos = lib.list_all().splitlines()  # Ensure list_all is a valid method
            for video in all_videos:
                self.video_listbox.insert(tk.END, video)
        except Exception as e:
            print(f"Error updating video list: {e}")

    def on_video_select(self, event):
        selected_index = self.video_listbox.curselection()
        if selected_index:
            selected_video = self.video_listbox.get(selected_index)
            self.selected_video_code = selected_video.split()[0]  # Store the video code
            self.show_video_info(self.selected_video_code)

    def add_to_playlist(self):
        # Get video code from entry or use the selected video code
        video_code_from_entry = self.entry.get().strip()
        video_code = video_code_from_entry if video_code_from_entry else self.selected_video_code

        if video_code:
            try:
                all_videos = lib.library
                if video_code in all_videos:
                    video_name = lib.get_name(video_code)
                    if video_name not in self.playlist:
                        self.playlist.append(video_code)
                        self.playlist_box.insert(tk.END, f"{video_name}\n")
                        self.playlist_box.see(tk.END)
                        print(f"Added {video_name} to playlist.")
                        self.entry.delete(0, tk.END)  # Clear the entry field after adding
                        self.selected_video_code = None  # Clear the selected video code
                    else:
                        print(f"{video_name} is already in the playlist.")
                else:
                    print("Invalid video code. Please try again.")
            except Exception as e:
                print(f"Error adding video: {e}")
        else:
            print("No video selected. Please select a video from the list or enter a video code.")

    def reset_playlist(self):
        self.playlist = []
        self.playlist_box.delete('1.0', tk.END)
        print("Playlist reset.")

    def show_video_info(self, video_code):
        try:
            video_name = lib.get_name(video_code)
            play_count = lib.get_play_count(video_code)  # Ensure get_play_count is a valid method
            video_info = f"Video: {video_name}\nPlay Count: {play_count}"
            self.info_box.delete('1.0', tk.END)
            self.info_box.insert(tk.END, video_info)
        except Exception as e:
            print(f"Error displaying video information: {e}")

    def play_playlist(self):
        if not self.playlist:
            messagebox.showerror("Error", "Playlist is empty. Add videos to the playlist first.")
            return

        for video_code in self.playlist:
            try:
                lib.increment_play_count(video_code)  # Increment play count
                lib.play(video_code)  # Ensure play is a valid method in video_library
                print(f"Playing video: {video_code}")
                self.show_video_info(video_code)  # Update video info after playing
            except Exception as e:
                print(f"Error playing video: {e}")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()  # Configure fonts if necessary
    CreateVideoList(window)
    window.mainloop()
