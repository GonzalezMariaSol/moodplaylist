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

    return options  # ~return the options/menu based on how many or if any songs are in the list



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
    song_name = input("\n Write Song Name:")
    song_artist = input("\n Write Song Artist:")
    song_mood = choose_mood()
    new_song = {"name": song_name, "artist": song_artist, "mood": song_mood}
    songs_list.append(new_song)



# $ This function only evaluate if the user answer is valid or not 

def get_valid_number(max_value, prompt_message):
    while True: # ~ We start a indless loop (will be repeating forever unless we stop it using a return/break)
        user_input = input(prompt_message) # ~ we store user answer
        try:
            number = int(user_input) # ~ we try to turn that answer into a number (if the user decide to type a "hello" will fall into the except)
        except ValueError:
            prompt_message = "\n Please enter a number, not text: " # ~ show error msge
            continue # ~ and start all over from the user_input ⟳
        # ~ once the user actually place a valid answer
        if number < 1 or number > max_value: # ~ if the anser if lower than 1 or greater than max_value (max_value is basically the moods list length)
            prompt_message = f"\n Please choose a number between 1 and {max_value}: " # ~ show error msge
            continue # ~ and start all over from user_input ⟳

        return number  # ~when the user place a valid answer will finish the loop, returning the number that it placed



# $ This function will ask a user to choose a mood based on its number

def choose_mood():
    print("\n SONG MOOD:")
    for i, mood in enumerate(MOODS, start=1): # ~ for each position and mood in moods, starting from position 1
        print(f"{i}. {mood}")
    
    number_mood = get_valid_number(len(MOODS), "\n Choose a mood for your song: ") # ~ we save number chosen from user 
    return MOODS[number_mood - 1] # ~ and we return the mood that belongs to that number (we use - 1 for positions purposes)



# $ This function will go thru the song list, and will show it in a better format for user readability

def view_songs (songs_list):
    for i, song in enumerate(songs_list, start=1): # ~ will go thru the list of songs, starting from the n1
        print(f"{i}. {song['name']} - {song['artist']} ({song['mood']})") # ~ and "re shape it" for a better readability for the user 



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
    while True:  # ~ We start a indless loop asking for a choice until the user exits
        options = show_menu(songs_list) # ~ we save in options the type of menu that is avaible for the amount of songs that are loaded (empty = menu with 2 options, songs avaible = menu with 4 options)
        choice_number = get_valid_number(len(options), "\n Choose an option: ") # ~ user have to chose a numb avaible from the menu (len options is in charge to show whats the limit number, either the 2 menu or the 4 menu), and we use get valid number because will let us insist in get a rigth answer till the user answer with a right number avaible
        chosen_option = options[choice_number - 1] # ~ we turn the number that user chose to a text option from the menu (again using a - 1 for positions purposes, if user chose 1 it really meant it chose the option in position 0)

        if chosen_option == "Add song":
            add_song(songs_list)  # ~ we call add_song, which will ask the user what song they want to add
            save_songs(songs_list, file_name)  # ~ we call save_songs so the song the user just added gets saved in the CSV. Otherwise it will be lost as soon as the console restarts
        elif chosen_option == "Generate playlist":
            generate_playlist(songs_list)
        elif chosen_option == "View songs":
            view_songs(songs_list)
        elif chosen_option == "Exit":
            print("Goodbye! 🎵")
            break  # ~ this is what actually stops the while True loop



list_of_songs = load_songs("songs.csv")
main(list_of_songs, "songs.csv")