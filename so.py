import requests
from bs4 import BeautifulSoup

results = []

def extract_so_url(word):
  SO_URL = "https://stackoverflow.com/jobs/companies?tl=python&pg=1"
  result = requests.get(SO_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "s-pagination"})
  links = pagination.findAll("a")
  max_page = links[-2]["href"].split("pg=")[1]

  for i in range(1,int(max_page)+1):
    URL = SO_URL.split("pg=")[0] + 'pg=' + str(i)
    extract_so_jobs(URL)
  return results

def extract_so_jobs(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  jobs = soup.findAll("div",{"class":"dismissable-company"})
  for job in jobs:
    company = job.find("a",{"class":"s-link"}).string
    link = "https://stackoverflow.com" + job.find("a",{"class":"s-link"})["href"]
    title = job.find("div",{"class":"gs12"}).findAll("div",{"class":"fs-body1"})[1].get_text()
    results.append({"title": title, "company": company, "link": link})