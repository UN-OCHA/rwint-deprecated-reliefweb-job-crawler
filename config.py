# PORT for the API
PORT = 5000

# Debug mode for the messages
DEBUG = True

# URL of the endpoint for tagging each job
TAGGING_URL = "https://rw-tag.herokuapp.com/tag_url?scope=job&url="
# TAGGING_URL = "http://0.0.0.0:5001/tag_url?scope=job&url="

MAX_RETRIES = 3  # Number of times to try to tag a url when getting an error

REQUEST_TIMEOUT = 30  # Number of seconds to send a response even if not all jobs have been processed // It is 30 seconds for Heroku
# HTTP requests have an initial 30 second window in which the web process must return response data (either the completed response or some amount of response data to indicate that the process is active). Processes that do not send response data within the initial 30-second window will see an H12 error in their logs.



# reliefWeb DICTIONARIES mapping texts and identifiers
