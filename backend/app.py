from flask import Flask, request, jsonify
from flask_cors import CORS
from googleapiclient.discovery import build

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Replace with your YouTube API Key
YOUTUBE_API_KEY = "AIzaSyDbqSEDoql-ukbmei2fPi8YsmStCFil7sY"

# Function to fetch YouTube videos
def search_youtube(query):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=query, part="snippet", maxResults=5, type="video"
    )
    response = request.execute()
    
    results = []
    for item in response.get("items", []):
        results.append({
            "title": item["snippet"]["title"],
            "youtube_link": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })
    return results

@app.route("/")
def home():
    return """
    <h1>🎧 AI DJ Playlist Generator Backend is Running! 🚀</h1>
    <p>Use <b>/recommend</b> endpoint to get song recommendations.</p>
    <p>Example: Send a POST request to <b>/recommend</b> with a mood.</p>
    """

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "").lower()

    # Search for YouTube videos based on mood
    recommendations = search_youtube(f"{mood} music mix")
    
    return jsonify(recommendations)

if __name__ == "__main__":
    print("🔥 AI DJ Playlist Generator Backend is Running!")
    print("🌍 Open in browser: http://127.0.0.1:5000")
    print("📡 Send a POST request to /recommend with a mood.")
    print("⚡ Example: curl -X POST http://127.0.0.1:5000/recommend -H \"Content-Type: application/json\" -d '{\"mood\": \"happy\"}'")
    app.run(debug=True)
