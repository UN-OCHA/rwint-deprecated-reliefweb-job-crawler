# reliefweb-job-crawler
ReliefWeb Job Crawler - A simple web crawler to grab jobs from a website
Uses reliefweb-job-assistant endpoint to tag the job information


## Structure

- main.py - *Main file* 
- setup.py - *Python setup for setuptools*

## Requirements

- python - Available from the [Python Homepage](https://www.python.org/)
- an endpoint with reliefweb-tag-assistant


- Modules required

```
$ sudo apt-get install python3-pip
$ pip install -r requirements.txt

```

- Main reliefweb-tag 

```
# if you install from your home path, there is no need to change the config file
$ git clone https://github.com/reliefweb/reliefweb-tagjob-crawler/
$ gedit config.py # configure the URL of the tagging endpoint 
$ sudo python3 setup.py install
$ python3 main.py &
```

## How to use the service

There are 2 parameters to the /web_crawl endpoint:

- url - *URL starting with http where the list of jobs is displayed*
- job_pattern - *String which is contained in **all the job URLs** so the crawler can identify what links refer to a 
job*

Once the backend is running you can use the following endpoints:

- http://localhost:5000/web_crawl?url=https://www.unocha.org/about-us/job-opportunities&job_pattern=jobdetail
- http://localhost:5000/web_crawl?url=http://www1.wfp.org/careers/job-openings&job_pattern=job_listing

(Updated information and last names for the endpoints in the ```main.py``` file)
