import csv

MOODS = ["Happy", "Sad", "Emotional", "Chill", "Party", "Workout"]


# $This fuction will show a type of menu based if in the list of songs have or have not songs in it

def show_menu(songs_list):
    print("\n Welcome to MoodPlaylist 🎵")
    print("---------------------------")
    if len(songs_list) > 0:
        options = ["Add song", "Generate playlist", "View songs", "Exit"]
    else:
        options = ["Add song", "Exit"]

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    return options  



# $ This function open and read a CSV file, and turn each row into a dict and adds it to a list (empty or with data)

def load_songs (file_name): 
    songs = []
    try: 
        with open(file_name, mode="r") as file: 
            reader = csv.DictReader(file) 
            for row in reader: 
                songs.append(row)   
    except FileNotFoundError: 
        pass
    return songs 



# $ This function will add existing songs in the list to the csv file

def save_songs (list_of_songs, file_name):  
    fields = ["name", "artist", "mood"] 
    with open(file_name, mode="w") as file: 
        writer = csv.DictWriter(file, fieldnames=fields) 
        writer.writeheader() 
        for song in list_of_songs: 
            writer.writerow(song)



# $ This function collects the info from user to add a song to the csv file

def add_song (songs_list):
    song_name = input("\n Write Song Name:")
    song_artist = input("\n Write Song Artist:")
    song_mood = choose_mood()
    new_song = {"name": song_name, "artist": song_artist, "mood": song_mood}
    songs_list.append(new_song)



# $ This function only evaluate if the user answer is valid or not 

def get_valid_number(max_value, prompt_message):
    while True: 
        user_input = input(prompt_message)
        try:
            number = int(user_input) 
        except ValueError:
            prompt_message = "\n Please enter a number, not text: " 
            continue 
        if number < 1 or number > max_value: 
            prompt_message = f"\n Please choose a number between 1 and {max_value}: " 
            continue 

        return number  



# $ This function will ask a user to choose a mood based on its number

def choose_mood():
    print("\n SONG MOOD:")
    for i, mood in enumerate(MOODS, start=1): 
        print(f"{i}. {mood}")
    
    number_mood = get_valid_number(len(MOODS), "\n Choose a mood for your song: ") 
    return MOODS[number_mood - 1] 



# $ This function will go thru the song list, and will show it in a better format for user readability

def view_songs (songs_list):
    for i, song in enumerate(songs_list, start=1): 
        print(f"{i}. {song['name']} - {song['artist']} ({song['mood']})")  



# $ This function will generate a playlist based on the users mood

def generate_playlist(songs_list):
    mood_user_input = choose_mood()
    songs_mood = []
    for song in songs_list:
        if song["mood"] == mood_user_input:
            songs_mood.append(song)

    print(f"\n{mood_user_input.upper()} PLAYLIST")
    print("---------------------------")
    for i, song in enumerate(songs_mood, start=1):
        print(f"{i}. {song['name']} / {song['artist']}")



# $ This function is the main lopp that will show a menu, will catch users answer and will run the rigth action based on user picks (add song, generate playlist, view songs, or exit) the loop ends only when user choose exit

def main(songs_list, file_name):
    while True:  
        options = show_menu(songs_list) 
        choice_number = get_valid_number(len(options), "\n Choose an option: ") 
        chosen_option = options[choice_number - 1] 

        if chosen_option == "Add song":
            add_song(songs_list)  
            save_songs(songs_list, file_name)  
        elif chosen_option == "Generate playlist":
            generate_playlist(songs_list)
        elif chosen_option == "View songs":
            view_songs(songs_list)
        elif chosen_option == "Exit":
            print("Goodbye! 🎵")
            break  



list_of_songs = load_songs("songs.csv")
main(list_of_songs, "songs.csv")