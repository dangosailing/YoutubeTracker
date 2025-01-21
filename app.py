# File to develop and use testing of YT API
from config import Config
from googleapiclient.discovery import build

# Stores the API KEY
conf = Config()
developer_key = conf.YTT_API_KEY

# Create service
youtube = build("youtube", "v3", developerKey=developer_key)

request = youtube.channels().list(
    part = "statistics",
    forUsername="schafer5"
)

response = request.execute()

print(response)