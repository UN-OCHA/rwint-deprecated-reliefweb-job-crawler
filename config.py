# PORT for the API
PORT = 80

# Debug mode for the messages
DEBUG = True

# URL of the endpoint for tagging each job
TAGGING_URL = "https://rw-tag.herokuapp.com/tag_url?scope=job&url="
MAX_RETRIES = 3  # Number of times to try to tag a url when getting an error

# reliefWeb DICTIONARIES mapping texts and identifiers
