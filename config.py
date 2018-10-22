# PORT for the API
PORT = 5000

# Debug mode for the messages
DEBUG = True

# URL of the endpoint for tagging each job
# TAGGING_URL = "https://rw-tag.herokuapp.com/tag_url?scope=job&url="
# TAGGING_URL = "http://0.0.0.0:5001/tag_url?scope=job&url="
TAGGING_URL = "http://reliefweb-tag-assistant.us-east-1.elasticbeanstalk.com/tag_url?scope=job&url="

MAX_RETRIES = 3  # Number of times to try to tag a url when getting an error

REQUEST_TIMEOUT = 300  # Number of seconds to send a response even if not all jobs have been processed // It is 30 seconds for Heroku
# HTTP requests have an initial 30 second window in which the web process must return response data (either the completed response or some amount of response data to indicate that the process is active). Processes that do not send response data within the initial 30-second window will see an H12 error in their logs.

# reliefWeb DICTIONARIES mapping texts and identifiers
theme_dictionary = {"Agriculture": "4587",
                    "Climate Change and Environment": "4588",
                    "Contributions": "4589",
                    "Coordination": "4590",
                    "Disaster Management": "4591",
                    "Education": "4592",
                    "Food and Nutrition": "4593",
                    "Gender": "4594",
                    "Health": "4595",
                    "HIV/Aids": "4596",
                    "Humanitarian Financing": "4597",
                    "Logistics and Telecommunications": "4598",
                    "Mine Action": "12033",
                    "Peacekeeping and Peacebuilding": "4599",
                    "Protection and Human Rights": "4600",
                    "Recovery and Reconstruction": "4601",
                    "Safety and Security": "4602",
                    "Shelter and Non-Food Items": "4603",
                    "Water Sanitation Hygiene": "4604"}

career_category_dictionary = {"Administration/Finance": "6864",
                              "Finance/Accounting/Auditing": "6864",
                              "Donor Relations/Grants Management": "20966",
                              "Donor Relations/Fundraising/Grants Management": "20966",
                              "Human Resources": "6863",
                              "Administration/HR": "6863",
                              "Information and Communications Technology": "6866",
                              "Information Technology": "6866",
                              "Information Management": "20971",
                              "Logistics/Procurement": "36601",
                              "Advocacy/Communications": "6865",
                              "Media/Communication": "6865",
                              "Monitoring and Evaluation": "6868",
                              "Program/Project Management": "6867"}

job_type_dictionary = {"Consultancy": "264",
                       "Job": "263",
                       "Internship": "265",
                       "Volunteer Opportunity": "266"}

experience_dictionary = {"0-2 years": "258",
                         "3-4 years": "259",
                         "5-9 years": "260",
                         "10+ years": "261",
                         "N/A": "262"}
