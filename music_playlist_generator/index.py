import random

# Define music playlists based on mood/activity
playlists = {
    'relaxing': [
        "Artist - Song 1",
        "Artist - Song 2",
        "Artist - Song 3",
        # Add more songs as needed
    ],
    'upbeat': [
        "Artist - Song 4",
        "Artist - Song 5",
        "Artist - Song 6",
        # Add more songs as needed
    ],
    'focus': [
        "Artist - Song 7",
        "Artist - Song 8",
        "Artist - Song 9",
        # Add more songs as needed
    ]
}

def generate_playlist(mood):
    if mood in playlists:
        playlist = playlists[mood]
        random.shuffle(playlist)
        print(f"Generated {mood} playlist:")
        for index, song in enumerate(playlist, start=1):
            print(f"{index}. {song}")
    else:
        print(f"No playlist found for '{mood}'.")

# Example usage
generate_playlist('relaxing')
generate_playlist('upbeat')
generate_playlist('focus')
