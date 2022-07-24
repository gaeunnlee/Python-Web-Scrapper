import requests
from bs4 import BeautifulSoup

results = []

def extract_remotely_jobs(word):
    REMOTELY_URL = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
    result = requests.get(REMOTELY_URL)
    soup = BeautifulSoup(result.text, "html.parser")
    jobs = soup.findAll("li", {"class": "feature"})
    for job in jobs:
        title = job.find("span", {"class": "title"}).string
        company = job.find("span", {"class": "company"}).string
        links = job.findAll("a")
        link = "https://weworkremotely.com" + links[1]["href"]
        results.append({"title": title, "company": company, "link": link})
    return results
