import requests

YOUTUBE_API_KEY = "your-youtube-api-key"

def get_youtube_data(song_name):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={song_name}&key={YOUTUBE_API_KEY}"
    response = requests.get(url).json()
    
    if "items" in response and len(response["items"]) > 0:
        return f"https://www.youtube.com/watch?v={response['items'][0]['id']['videoId']}"
    
    return None
