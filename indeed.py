import requests
from bs4 import BeautifulSoup



results = []


def extract_indeed_url(word):
    INDEED_URL = "https://www.indeed.com/jobs?q={word}&start=0"
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("ul", {"class": "pagination-list"}).findAll("li")
    max_page = pagination[-2].string

    for i in range(int(max_page)):
        url = INDEED_URL.split("&start=")[0] + '&start=' + str(i * 10)
        extract_indeed_jobs(url)
    return (results)


def extract_indeed_jobs(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    jobs = soup.find("ul", {
        "class": "jobsearch-ResultsList"
    }).findAll("td", {"class": "resultContent"})
    for job in jobs:
        title = job.find("a", {"class": "jcs-JobTitle"}).string
        link = job.find("a", {"class": "jcs-JobTitle"})["href"]
        company = job.find("span", {"class": "companyName"}).string
        results.append({"title": title, "company": company, "link": link})
