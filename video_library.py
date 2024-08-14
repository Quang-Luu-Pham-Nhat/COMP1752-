import csv
from library_item import LibraryItem

library = {}
with open('library.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        key = row['key']
        name = row['name']
        director = row['director']
        rating = int(row['rating'])
        library[key] = LibraryItem(key, name, director, rating)
                                         
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_info(key):
    try:
        item = library[key]
        return item.info()
    except KeyError:
        return "Video information not found."

def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def play(key):
    try:
        item = library[key]
        print(f"Playing {item.name} directed by {item.director}")
    except KeyError:
        print("Video not found.")

def add_video(key, name, director, rating):
    library[key] = LibraryItem(key, name, director, rating)

def key_exists(key):
    try:
        with open('library.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == key:
                    return True
    except FileNotFoundError:
        return False
    return False
