import csv

#This function open and read a CSV file, and turn each row into a dict and adds it to a list (empty or with data)
def load_songs(file_name):
    songs = []
    try:
        with open(file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                songs.append(row)
    except FileNotFoundError:
        pass
    return songs

list_of_songs = load_songs("songs.csv")
print(f"You have {len(list_of_songs)} songs saved")

#This function will add existing songs to the csv file
def save_songs(song_list, file_name):
    fields = ['name', 'artist', 'mood']
    with open(file_name, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for item in song_list :
            writer.writerow(item)

# test_songs=[{"name": "Bohemian Rhapsody", "artist": "Queen", "mood": "Epic"},{"name": "Gasolina", "artist": "Daddy Yankee", "mood": "Happy"}]
# save_songs(test_songs, "songs.csv")

def add_song (songs_list) :
    song_name = input("Write Song Name:")
    song_artist = input ("Write Song Artist:")
    song_mood = input ("Write Song Mood:")
    new_song = {"name": song_name, "artist": song_artist, "mood": song_mood}
    songs_list.append(new_song)

my_list = [{"name": "Bohemian Rhapsody", "artist": "Queen", "mood": "Epic"},{"name": "Gasolina", "artist": "Daddy Yankee", "mood": "Happy"},]
add_song(my_list) #→ agrega la canción nueva a la lista en memoria
print(my_list)
save_songs(my_list, "songs.csv")