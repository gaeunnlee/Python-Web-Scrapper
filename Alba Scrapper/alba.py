import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr/"

def extract_links() :
    alba_result = requests.get(URL)

    alba_soup = BeautifulSoup(alba_result.text, 'html.parser')

    # pagination이라는 클래스명을 지닌 div를 찾는다
    super_brand = alba_soup.find("div", {"id":"MainSuperBrand"})

    pages = super_brand.find_all("li",{"class": "impact"})
    links = []

    for page in pages:
        link = page.find("a")["href"]
        links.append(link)
    
    return links

def extract_jobs(links):
    for link in links:
        brand_result = requests.get(link)
        brand_soup = BeautifulSoup(brand_result.text, 'html.parser')
        job = brand_soup.find("div",{"id":"NormalInfo"})
        locals = job.find_all("td",{"class":"local"})
        local_result = []
        for local in locals:
            local_result.append(local.get_text())
        print(local_result)

        companys = job.find_all("td",{"class":"local"})
        company_result = []
        for company in companys:
            company_result.append(company.get_text())
        print(company_result)
        

link_result = extract_links()
extract_jobs(link_result)