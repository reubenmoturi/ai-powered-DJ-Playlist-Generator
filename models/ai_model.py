import random

# Sample song dataset with moods
songs = [
    {"title": "Happy Tune", "mood": "happy"},
    {"title": "Sad Melody", "mood": "sad"},
    {"title": "Energetic Beat", "mood": "energetic"},
    {"title": "Calm Vibes", "mood": "calm"},
]

def recommend_songs(user_mood):
    filtered_songs = [song for song in songs if song["mood"] == user_mood]
    return filtered_songs if filtered_songs else random.sample(songs, 2)
