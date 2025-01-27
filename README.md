# YoutubeTracker
Project for python development course. Track youtube stats for various channels

## App description
    - Offer a way to keep track of various youtube channels
    - Channel statics tracked over time. View count for VODS
    subscriber count over time
    - Data management and representation via Pandas and Numpy

## Project documentation
    - What are the available statistics publically available from YT. These will decide the scope of the project.
    - Start out by making the API requests work so that data 
    can be acquired. 
    - Next step will include collection and storage of the available data
    - START SMALL and work outwards. Implement basic functionality and get a MVP before expanding scope
    - Keep functions simple for simple tests

## TODO checklist
    STAGE 1: Basic functionality
    - Setup an environment to get basic requets from youtube
    - Get data from one video
    - Get data from one user/channel
    - Create a history over user stats for a simple concept: 
        Subscribers over time or views over time for a user
    - Store data in some form of database
    - Create a visual representation of data
    
    STAGE 2: Interfacing with user
    - Build a simple webapp with FLASK 

### Libraries
Official Google API python client: google-api-python-client
`Used to handle the API requests to youtube`
'https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md'

### Workflow - log
1. Adding the google developer console YT API key to system variables (WIN 10)
2. Had some issues with installing the module for google api python client. 
Resolved by setting python interpreter from anaconda to venv in vscode settings
3. Managed to figure out a way to get a channel and video ids using search. Were able to use
these to get ccv data for an active livestream. The daily API quota is 10000 calls, a 
search call costs 100 units while a video listing call costs 1 unit.
I can now effectively track a livestream manually. In order to avoid needless API calls
to gather mock data I will build a simple mock-data app do generate timestamps and ccv
within a set interval. Also need to start work on the login and register function as well
as tests.
5. Built a simple mock data and plotter to somewhat visualize CCV tracking without sending 
unnecessary requests.