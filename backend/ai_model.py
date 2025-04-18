def recommend_songs(mood):
    mood_songs = {
        "happy": ["Ed Sheeran - Shape of You", "Pharrell Williams - Happy", "Dua Lipa - Levitating"],
        "sad": ["Adele - Someone Like You", "Billie Eilish - Ocean Eyes"],
        "energetic": ["Eminem - Lose Yourself", "Drake - God's Plan"],
        "party": ["Black Eyed Peas - I Gotta Feeling", "Pitbull - Fireball"],
        "chill": ["Coldplay - Fix You", "John Mayer - Gravity"]
    }
    
    return mood_songs.get(mood.lower(), ["Random Song 1", "Random Song 2"])
