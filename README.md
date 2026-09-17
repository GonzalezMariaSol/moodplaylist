# MoodPlaylist 🎵

Mood Playlist is a console Python app that lets you save songs tagged with a mood, and generate a playlists based on your mood on demand.

This project was built as a practice of core Python fundamentals: functions, file I/O, CSV handling, input validation, and program flow control, without relying on any external frameworks or libraries beyond Python's standard library.

## Features

- **Add songs** : save a song's name, artist, and mood
- **Fixed mood categories** : choose from `Happy`, `Sad`, `Emotional`, `Chill`, `Party`, or `Workout` (no free text, to keep data consistent)
- **View all songs** : see every song currently saved, nicely formatted
- **Generate a playlist** : pick a mood and get back only the songs that match with it
- **Persistent storage** : songs are saved to a CSV file, so theres a memory there the next time the app is run
- **Input validation** : the app won't accept invalid menu choices or mood numbers, it keeps asking until you give it something valid

## How to run it

**Requirements:** Python 3.x (no external packages needed, everything if from the standard library).

1. Clone this repository:
   ```bash
   git clone https://github.com/GonzalezMariaSol/moodplaylist.git
   ```
2. Run the app:
   ```bash
   python main.py
   ```

The first time you run it, `songs.csv` doesn't exist yet, the app will create it automatically once you add your first song.

## Project structure

```
moodplaylist/
├── main.py         # all the app code lives here
├── songs.csv        # auto generated file where songs are stored
├── .gitignore
└── README.md
```

Everything is contained in a single file (`main.py`), split into clearly separated functions, each with one responsibility:

| Function | Responsibility |
|---|---|
| `load_songs()` | Reads the CSV file and loads existing songs into memory |
| `save_songs()` | Writes the current list of songs back to the CSV file |
| `add_song()` | Asks the user for song details and adds it to the list |
| `choose_mood()` | Displays the fixed mood options and validates the user's choice |
| `get_valid_number()` | Reusable input  that validate the answer (keeps asking until it gets a valid number in range) |
| `view_songs()` | Displays all currently loaded songs in a readable format |
| `generate_playlist()` | Filters songs and displays the ones that match with chosen mood as a playlist |
| `show_menu()` | Displays the available menu options (adjusts based on whether songs exist yet) |
| `main()` | The main program loop, ties everything together |

## Design decisions

- **Fixed moods over free text:** early on, I considered letting users type in any mood they wanted. I decided against it, free text input leads to inconsistent data, e.g: "Happy", "Feliz", "Super Happy" all meaning the same thing, which makes filtering unreliable. A fixed list keeps the data clean and predictable, at the cost of some flexibility.
- **CSV over plain text:** I chose CSV because each song has multiple fields (name, artist, mood), and CSV is already built to handle columns like that. With plain text, I would have had to invent my own separator and handle edge cases myself.
- **Bottom-up development approach:** I built this project from the bottom up — writing and testing each small function on its own before moving to the next, rather than building the full structure first and filling it in later. This let me confirm each piece worked correctly as I went, instead of only being able to test the program once most of it was written, when a bug would have been much harder to track down.
- **Single file, function-based (no classes):** given the scope of this project, a class-based (OOP) design would have added complexity without a clear benefit. Each function has a single, clear responsibility instead.

## Possible future improvements

- Allow editing or deleting existing songs
- Add song duration and show total playlist length (I considered this early on, but decided against it since manually asking for a song's duration would add unnecessary extra steps to the form, this is a feature I'd revisit if I integrated with a platform like Spotify, where duration could be retrieved automatically. Let users create multiple named playlists instead of generating one on the fly)
- Add a simple GUI or web interface

## About this project

Built as part of my learning path through Python 3 fundamentals from Codecademy, working toward AI/Python-focused roles. This was my first project pushed to GitHub and I have tried a step-by-step commit history.
