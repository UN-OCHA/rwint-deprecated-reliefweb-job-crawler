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

- UNICEF http://localhost:5000/web_crawl?url=https://www.unicef.org/about/employ/&job_pattern=/employ/&org_id=1979 # ERROR - JavaScript lazy load
- IRC
- ACTED http://localhost:5000/web_crawl?url=https://www.acted.org/en/get-involved/join-us/vacancies/&job_pattern=/jobs/&org_id=823
- SOLIDARITE http://localhost:5000/web_crawl?url=https://www.solidarites.org/en/since-1980/join-us/jobs/&job_pattern=/job-detail/&org_id=823
- SAVE THE CHILDREN http://localhost:5000/web_crawl?url=https://recruiting.ultipro.com/SAV1002STCF/JobBoard/7d92e82b-af74-464d-859b-c5b8cba6e92e/&job_pattern=OpportunityDetail&org_id=2865 # ERROR - javascript lazy load
- PALLADIUM GROUP http://localhost:5000/web_crawl?url=http://thepalladiumgroup.com/jobs&job_pattern=jobs&org_id=25696 # ERROR - relative urls
- PREMIERE URGENCE (Employees) http://localhost:5000/web_crawl?url=https://www.premiere-urgence.org/en/recruitment/our-vacancies/?types%5B%5D=Employee&job_pattern=/offres-emploi/&org_id=8593 -- ERROR connecting
# TODO: More searches
- IOM https://recruit.iom.int/sap/bc/webdynpro/sap/hrrcf_a_unreg_job_search?sap-client=100&sap-language=EN&sap-wd-configid=ZHRRCF_A_UNREG_JOB_SEARCH# - 1255 - ERROR: ASP
- RELIEF INTERNATIONAL http://localhost:5000/web_crawl?job_pattern=requisition.jsp&org_id=2024&url=https://chp.tbe.taleo.net/chp01/ats/servlet/Rss?org=RI&cws=4 - TODO: Support for RSS 
- MERCY CORPS
- HANDICAP INTERNATIONAL
- MEDECINS DU MONDE

- OCHA http://localhost:5000/web_crawl?url=https://www.unocha.org/about-us/job-opportunities&job_pattern=jobdetail&org_id=1503
- WFP http://localhost:5000/web_crawl?url=http://www1.wfp.org/careers/job-openings&job_pattern=job_listing&org_id=1741


(Updated information and last names for the endpoints in the ```main.py``` file)
