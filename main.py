import csv

MOODS = ["Happy", "Sad", "Emotional", "Chill", "Party", "Workout"]


def show_menu (songs_list):
    print("Welcome to MoodPlaylist 🎵")
    print("---------------------------")
    if len(songs_list) > 0:
        print("1. Add song")
        print("2. Generate playlist")
        print("3. View songs")
        print("4. Exit")
    else:
        print("1. Add song")
        print("2. Exit")



# $ This function open and read a CSV file, and turn each row into a dict and adds it to a list (empty or with data)

def load_songs (file_name): #~ load_songs waits for a CSV file name
    songs = []
    try: #~once have the file name, will try to open it in reading mode and call it file
        with open(file_name, mode="r") as file: 
            reader = csv.DictReader(file) #~ reader is an iterator that will yield each row as a DICT when we loop through it
            for row in reader: 
                songs.append(row)   #~ we will push that row into the list songs
    except FileNotFoundError: #~and if the file doesn't exist
        pass #~i just keep it as it is
    return songs #~after all this, i will return the list songs (empty or with songs but will return it)



# $ This function will add existing songs in the list to the csv file

def save_songs (list_of_songs, file_name): # ~ save songs will need the list of songs that already exist and the file CSV where we gonna be pushing it 
    fields = ["name", "artist", "mood"] # ~ we set that the headers of each column will be the ones inside this variable called fields
    with open(file_name, mode="w") as file: # ~ we open the file CSV as writing mode (bc we will be OVERWRITING songs to it), and we call it file
        writer = csv.DictWriter(file, fieldnames=fields) # ~ writer will save the file and tell it which column to expect from fields
        writer.writeheader() # ~ here we are like putting headers at the top of an Excel table
        for song in list_of_songs: # ~ for each song that exist in list_of_songs
            writer.writerow(song) # ~ in the file saved in writer, we gonna add a row with the song that we are currently on



# $ This function collects the info from user to add a song to the csv file

def add_song (songs_list):
    song_name = input("Write Song Name:")
    song_artist = input("Write Song Artist:")
    song_mood = choose_mood()
    new_song = {"name": song_name, "artist": song_artist, "mood": song_mood}
    songs_list.append(new_song)



# $ This function asks the user to choose a mood for the song they just added, and keeps asking again if the input isn't a valid option

def choose_mood () : 
    print("Songs Mood:")
    for i, mood in enumerate(MOODS, start=1): # ~ for each position and value in MOODS (starting position in 1)
        print(f"{i}. {mood}")
    prompt_message = "Choose a mood for your song: " # ~ The question that we gonna ask at first to users

    while True: # ~ do an infinite loop that
        user_mood = input(prompt_message) # ~ ask users to chose a number
        try:
            number_mood = int(user_mood) # ~ try to save users answer as a number
        except ValueError: # ~ unless that the answer is anything but a number
            prompt_message = "Please enter a number, not a text: "  # ~ update the message for next loop
            continue # ~ we ask again

        if number_mood < 1 or number_mood > len(MOODS): # ~ if the number doesnt fit between 1 to 6
            prompt_message = "Please choose a number between 1 and 6: "  # ~ update the message for next loop
            continue # ~ we ask again 

        break # ~we cut the loop once we have a valid answer (a int from 1 to 6)

    return MOODS[number_mood - 1] # ~ our function will return the mood that is under that number (the number has a -1 for position purposes)    



# $ This function will go thru the song list, and will show it in a better format for user readability

def view_songs (songs_list):
    for i, song in enumerate(songs_list, start=1): # ~ will go thru the list of songs, starting from the n1
        print(f"{i}. {song['name']} - {song['artist']} ({song['mood']})") # ~ and "re shape it" for a better readability for the user 



# $ This function will generate a playlist based on the users mood

def generate_playlist (songs_list):
    mood_user_input = choose_mood() # ~ we reuse the funcion choose_mood to ask again which mood wants to choose and get a right answer without mistakes
    songs_mood = []
    for song in songs_list: 
        if song["mood"] == mood_user_input: # ~ if the song mood is same as the mood that the user choosed
            songs_mood.append(song) # ~ we add it to the list of songs that are the same mood
            print(f"{song['name']} - {song['artist']}") # ~ and we show to the user the songs that belong the same mood, mood that it chose



list_of_songs = load_songs("songs.csv") #~create a variable of list of songs that will save the dictionary created in it
print(f"You have {len(list_of_songs)} songs saved")

add_song(list_of_songs) #! D
save_songs(list_of_songs, "songs.csv") #! D
view_songs(list_of_songs) #! D
generate_playlist(list_of_songs) #! D
show_menu(list_of_songs)
