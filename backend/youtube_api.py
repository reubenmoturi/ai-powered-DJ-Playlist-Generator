import requests

YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

def get_youtube_data(song_title):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": song_title,
        "key": YOUTUBE_API_KEY,
        "maxResults": 1,
        "type": "video"
    }
    response = requests.get(search_url, params=params)
    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        video_id = data["items"][0]["id"]["videoId"]
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"
        return {"title": song_title, "youtube_link": youtube_link}
    else:
        return {"title": song_title, "youtube_link": "https://www.youtube.com"}
