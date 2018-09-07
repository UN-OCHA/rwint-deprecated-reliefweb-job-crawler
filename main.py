#### START OF THE FINAL CODE FOR THE MODULE

# https://rw-tag.herokuapp.com/tag_url?scope=job&url=https://www.acted.org/en/jobs/country-transparency-and-compliance-officer-consortium-sanaa/
# https://rw-tag.herokuapp.com/tag_url?scope=job&url=https://rescue.csod.com/ats/careersite/jobdetails.aspx?id=2668

# url = "https://rw-tag.herokuapp.com/tag_url?scope=job&url=https://rescue.csod.com/ats/careersite/jobdetails.aspx?id=2668"
import config

### SAMPLES FOR TESTING
ocha_url = 'https://www.unocha.org/about-us/job-opportunities'  # working
ocha_job_pattern = 'jobdetail'

unicef_url = 'https://www.unicef.org/about/employ/'  # don't ge tthe URL jobs
unicef_job_pattern = '/about/employ'  # trying

google_url = 'https://careers.google.com/jobs#t=sq&q=j&li=20&l=false&jc=DATA_CENTER_OPERATIONS&jc=DEVELOPER_RELATIONS&jc=HARDWARE_ENGINEERING&jc=INFORMATION_TECHNOLOGY&jc=NETWORK_ENGINEERING&jc=TECHNICAL_WRITING&jc=TECHNICAL_SOLUTIONS&jc=TECHNICAL_INFRASTRUCTURE_ENGINEERING&jc=SOFTWARE_ENGINEERING&jc=MANUFACTURING_SUPPLY_CHAIN&jc=PROGRAM_MANAGEMENT&jcoid=7c8c6665-81cf-4e11-8fc9-ec1d6a69120c&jcoid=e43afd0d-d215-45db-a154-5386c9036525&'
google_url_pattern = 'jid=\/google\/'  # not working

wfp_url = 'http://www1.wfp.org/careers/job-openings'  # WORKING
wfp_url_pattern = 'https://career012.successfactors.eu/career?career_ns=job_listing'


### MODULE START


def create_jobs_feed(source_url, job_pattern):
    from lxml import etree
    import datetime

    root = etree.Element('channel')
    root.attrib['generator'] = "auto-job-reader"
    root.attrib['timestamp'] = str(datetime.datetime.now())

    job_links = get_job_links(source_url, job_pattern)
    start_time = datetime.datetime.now()
    job_counter = 0
    for link in job_links:
        n_retries = 0
        completed = False
        while not completed:
            job_json = tag_job_url(link, config.TAGGING_URL)
            completed = (job_json.get("error") is None) & (n_retries < config.MAX_RETRIES)
            if completed:
                append_job_xml(root, job_json)
            n_retries = n_retries + 1

        job_counter = job_counter + 1
        time = datetime.datetime.now()
        print("Processed " + str(job_counter) + " jobs in " + str(
            time - start_time) + " seconds. Estimated time left : " +
              str(((time - start_time) * len(job_links) / job_counter) - (time - start_time)) + " - " +
              str(int(job_counter * 100 / len(job_links))) + "% processed")
        # if job_counter == 2: # to limit the number of calls
        #    break

    # pretty string
    from bs4 import BeautifulSoup
    x = etree.tostring(root, pretty_print=True)
    xml_string = BeautifulSoup(x, "xml").prettify()
    print(xml_string)
    return xml_string


def get_job_links(source_url, job_pattern):
    url = source_url
    pattern = job_pattern

    import urllib.request
    from bs4 import BeautifulSoup  # pip install beautifulsoup4

    links = set()
    try:
        resp = urllib.request.urlopen(url)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="lxml")

        for link in soup.find_all('a', href=True):

            if pattern in link['href']:
                links.add(link['href'])

    except Exception as e:
        print("ERROR: While calling " + url)

    print("Processing " + str(len(links)) + " links to jobs")
    return links


def tag_job_url(url, tagging_endpoint):
    import urllib.request

    print("Tagging: " + url)
    req = urllib.request.Request(tagging_endpoint + url)

    try:
        with urllib.request.urlopen(req) as response:
            json_bytes = response.read()
        import json

        # Decode UTF-8 bytes to Unicode, and convert single quotes
        # to double quotes to make it valid JSON
        my_json = json_bytes.decode('utf8')

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)

    except Exception as e:
        print("ERROR: While calling " + config.TAGGING_URL + url)
        return ({"link": url, "error": str(e)})

    s = json.dumps(data, indent=4, sort_keys=True)  # for debugging and printing
    return data


def append_job_xml(xml_root, job_json):
    # TODO: are all fields values ordered by probablity? It doesn't seem so for job type
    from lxml import etree

    data = job_json
    root = xml_root

    # create XML
    job_item = etree.Element('item')
    root.append(job_item)

    element = etree.Element('link')
    job_item.append(element)
    element.text = "Not available"
    element.attrib['notes'] = "TODO - To add to the JSON result"

    if data.get("error") is not None:
        element = etree.Element('status')
        element.text = "ERROR"
        element.attrib['description'] = data["error"]
        job_item.append(element)
        return root  # Finish processing
    else:
        element = etree.Element('status')
        element.text = "OK"
        job_item.append(element)

    element = etree.Element('title')
    job_item.append(element)
    element.text = str(data["title"])

    element = etree.Element('field_job_closing_date')
    job_item.append(element)
    element.text = "Not available"
    element.attrib['notes'] = "TODO - Not possible from source"

    element = etree.Element('field_country')
    job_item.append(element)
    element.text = "ISO-3 pending"  # MUST BE ISO-3 and not ISO-2
    element.attrib['full_name'] = str(data["primary_country"][0])
    element.attrib['iso-2'] = str(data["primary_country"][1])
    element.attrib['notes'] = "TODO - To return ISO-3 code from the JSON"

    element = etree.Element('field_city')
    job_item.append(element)
    element.text = str(data["cities"][0])
    element.attrib['all-cities'] = str(data["cities"])
    element.attrib['notes'] = "TODO - Is the first city the most relevant?"

    element = etree.Element('field_source')
    job_item.append(element)
    element.text = "Not available"  # MUST MAP THE ORGANZATIONS ID OF RELIEFWEB
    element.attrib['complete-name'] = "Not available"
    element.attrib['source-url'] = "Not available"
    element.attrib['notes'] = "TODO - To add to the JSON result - Can use newspaper.create()"

    element = etree.Element('field_how_to_apply')
    job_item.append(element)
    element.text = "Not available"
    element.attrib['notes'] = "TODO - How to fill in this?"

    i_theme = 0
    for theme in data["job-theme"]:
        element = etree.Element('field_theme')
        element.text = str(data["job-theme"][i_theme][0])
        element.attrib['probability'] = str(data["job-theme"][i_theme][1])
        element.attrib['all-themes'] = str(data["job-theme"])
        job_item.append(element)
        i_theme = i_theme + 1
        if i_theme == 0:
            break

    element = etree.Element('field_job_type')
    element.text = str(data["job-type"][0][0])
    element.attrib['probability'] = str(data["job-type"][0][1])
    element.attrib['all-job-types'] = str(data["job-type"])
    job_item.append(element)

    element = etree.Element('field_career_categories')
    element.text = str(data["job-category"][0][0])
    element.attrib['probability'] = str(data["job-category"][0][1])
    element.attrib['all-job-categories'] = str(data["job-category"])
    job_item.append(element)

    element = etree.Element('field_job_experience')
    element.text = str(data["job-experience"][0][0])
    element.attrib['probability'] = str(data["job-experience"][0][1])
    element.attrib['all-job-experiences'] = str(data["job-experience"])
    job_item.append(element)

    element = etree.Element('body')
    job_item.append(element)
    element.text = str(data["body_markdown"])
    element.attrib['notes'] = "Body in markdown format"

    return root


# Initializing the model
import socket

from flask import Flask, request
from flask import make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-type'
# Content-type: application/json
app.debug = False
app.threaded = config.DEBUG


# Creating the API endpoints
@app.route("/")
# Instructions ENDPOINT
@cross_origin()
def main():
    return "Please, use the /web_crawl endpoint with the param url to tag a url or pdf. Example: http://IP:PORT/web_crawl?url=URL_WITH_HTTP&job_pattern=PATTERN_IN_JOB_LINKS"


@app.route("/web_crawl", methods=['POST', 'GET'])
# sample http://localhost:5000/web_crawl?url=https://www.unocha.org/about-us/job-opportunities&job_pattern=jobdetail
@cross_origin()
def call_and_create_jobs_feed():
    if request.method == 'POST':  # TODO: Support for GET calls
        return "No support for GET requests"
    else:
        url = request.args.get('url')
        job_pattern = request.args.get('job_pattern')

    output = create_jobs_feed(url, job_pattern)

    response = make_response(output)
    response.headers['content-type'] = 'text/xml'
    return response


if __name__ == '__main__':
    # get public IP -- if needed
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", config.PORT))
    publicIP = s.getsockname()[0]
    s.close()

    # app.run(debug=reliefweb_config.DEBUG, host=publicIP, port=reliefweb_config.PORT)  # use_reloader=False
    app.run(debug=config.DEBUG, host='0.0.0.0')  # use_reloader=False // This does not call to main