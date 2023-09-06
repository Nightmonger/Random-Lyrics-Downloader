import os
import random
import lyricsgenius as lg

# Initialize the Genius API client
genius = lg.Genius('<<YOUR-TOKEN>>', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

# List of artists
artists = ['The Beatles', 'Red Hot Chili Peppers', 'Imagine Dragons', 'Coldplay', 'Led Zeppelin', 'Pink Floyd',
           'Queen', 'The Rolling Stones', 'U2', 'Eagles', 'AC/DC', 'Aerosmith', 'Eminem', 'Scorpions', 'Nirvana',
           'The Doors', 'Pearl Jam', 'Guns And Roses', 'Metallica']

def save_lyrics_to_file(title, artist, lyrics):
    # Create a filename from the song title
    filename = f"{title.lower().replace(' ', '-')}.txt"

    # Get the current working directory
    current_directory = os.getcwd()

    # Create the full path to the file
    full_path = os.path.join(current_directory, filename)

    # Write the lyrics to the file
    with open(full_path, 'w') as file:
        file.write(f"{artist} - {title}\n------------------\n{lyrics.lower()}")

def get_and_save_lyrics(artist, num_songs):
    try:
        # Search for songs by the artist
        artist_info = genius.search_artist(artist, max_songs=num_songs)
        songs = artist_info.songs

        # Choose a random song from the artist's songs
        random_song = random.choice(songs)
        title = random_song.title
        artist = random_song.artist
        lyrics = random_song.lyrics

        # Remove the section headers from lyrics
        lyrics = lyrics.split('\n', 1)[1]

        # Save the lyrics to a file
        save_lyrics_to_file(title, artist, lyrics)

    except Exception as e:
        print(f"An error occurred: {e}")

# Choose a random artist from the list and fetch/save lyrics for one song
random_artist = random.choice(artists)
get_and_save_lyrics(random_artist, num_songs=1)
