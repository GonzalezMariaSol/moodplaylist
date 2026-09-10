import csv


# $ This function open and read a CSV file, and turn each row into a dict and adds it to a list (empty or with data)

def load_songs(file_name): #~ load_songs waits for a CSV file name
    songs = []
    try: #~once have the file name, will try to open it in reading mode and call it file
        with open(file_name, mode="r") as file: 
            reader = csv.DictReader(file) #~ reader is an iterator that will yield each row as a DICT when we loop through it
            for row in reader: 
                songs.append(row)   #~ we will push that row into the list songs
    except FileNotFoundError: #~and if the file doesn't exist
        pass #~i just keep it as it is
    return songs #~after all this, i will return the list songs (empty or with songs but will return it)


list_of_songs = load_songs("songs.csv") #~create a variable of list of songs that will save the dictionary created in it
print(f"You have {len(list_of_songs)} songs saved") #~we display how many songs have the list




# $ This function will add existing songs in the list to the csv file

def save_songs(song_list, file_name): # ~ save songs will need the list of songs that already exist and the file CSV where we gonna be pushing it 
    fields = ["name", "artist", "mood"] # ~ we set that the headers of each column will be the ones inside this variable called fields
    with open(file_name, mode="w") as file: # ~ we open the file CSV as writing mode (bc we will be OVERWRITING songs to it), and we call it file
        writer = csv.DictWriter(file, fieldnames=fields) # ~ writer will save the file and tell it which column to expect from fields
        writer.writeheader() # ~ here we are like putting headers at the top of an Excel table
        for song in song_list: # ~ for each song that exist in song_list
            writer.writerow(song) # ~ in the file saved in writer, we gonna add a row with the song that we are currently on


def add_song(songs_list): # ~ the functions is waiting for a list of songs where we gonna save new ones too
    song_name = input("Write Song Name:") # ~ we ask the user some info
    song_artist = input("Write Song Artist:")
    song_mood = input("Write Song Mood:")
    new_song = {"name": song_name, "artist": song_artist, "mood": song_mood} # ~ we create our dict for A song
    songs_list.append(new_song) # ~ we add that new song to our existing list


# ? TEST - DELETE LATER
my_list = [
    {"name": "Bohemian Rhapsody", "artist": "Queen", "mood": "Epic"},
    {"name": "Gasolina", "artist": "Daddy Yankee", "mood": "Happy"},
]
add_song(my_list)  # > agrega la canción nueva a la lista en memoria
print(my_list)
save_songs(my_list, "songs.csv")


MOODS = ["Happy", "Sad", "Emotional", "Chill", "Party", "Workout"]

def choose_mood () :
    for i, mood in enumerate(MOODS, start=1):
        print(f"{i}. {mood}")
    user_mood = input("Choose numer of the mood:")
    while int(user_mood) < 1 or int(user_mood) > len(MOODS) or user_mood == str :
        print("Please write a number that belongs to a mood")
        user_mood = input("Choose numer of the mood:")

choose_mood()