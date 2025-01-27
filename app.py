# File to develop and use testing of YT API
from config import Config
from googleapiclient.discovery import build
import pprint
import datetime

# Stores the API KEY
conf = Config()
developer_key = conf.YTT_API_KEY

# Create service
youtube = build("youtube", "v3", developerKey=developer_key)

channel_request = youtube.search().list(
    part="snippet,id, contentDetails",
    channelId="UCuI_opAVX6qbxZY-a-AxFuQ",
    eventType="live",
    type="video"
)

video_request = youtube.videos().list(
    part="liveStreamingDetails",
    id="vhxtAtZnTb8"
)

#channel_response = request.execute()
video_response = video_request.execute()
livestreamDetails = video_response["items"][0]["liveStreamingDetails"]
ccv = livestreamDetails["concurrentViewers"]

# DAILY QUOTA 10 000 UNITS
# SEARCH LIST REQUEST = 100 UNIT -channel_request
# VIDEO REQUEST = 1 UNIT -video_request
