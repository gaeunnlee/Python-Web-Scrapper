import requests
from bs4 import BeautifulSoup
from save import save_to_file

URL = "https://www.albamon.com/list/gi/mon_store_list.asp?page=1&gubun=71&clickpath=1&optgf=dfplatinumgold"   
jobs = []

def extract_page(URL):
    alba_result = requests.get(URL)
    alba_soup = BeautifulSoup(alba_result.content, 'html.parser', from_encoding='utf-8')
    
    job_count = int(alba_soup.find("div",{"class":"pageSubTit"}).find("em").get_text().replace(',',''))
    page_max = job_count // 20

    page_max = page_max if page_max % 20 == 0 else page_max + 1
    return(page_max)   


def extract_job(link):
    alba_result = requests.get(link)
    alba_soup = BeautifulSoup(alba_result.content, 'html.parser', from_encoding='utf-8')


    job_list = alba_soup.find("div",{"class":"gListWrap"}).find_all("tr")

    job_list.pop(0)

    for job in job_list:

        company = job.select_one('p.cName > a').get_text()
        area = job.select_one('.area > div').get_text()[6:-2]
        pay = job.select_one('.pay')
        pay_type = pay.find("p",{"class":"money"}).find("img")["alt"]
        pay_money = pay.find("p",{"class":"won"}).get_text()
        pay_result = pay_type + " " + pay_money
        time = job.select_one("td:nth-of-type(4)").get_text()
        time = time[7:-7]
        recently = job.select_one('.recently').get_text()
        job = {"place": area,"title": company,"time" :time,"pay": pay_result,"date": recently}
        jobs.append(job)

page_max = extract_page(URL)

for page in range(1,page_max+1):
    URL_split_0 = URL.split("?page=")
    URL_split_1 = URL_split_0[1].split("&")
    newURL = URL_split_0[0] + "?page=" + str(page) + "&" + URL_split_1[1]
    extract_job(newURL)
    
save_to_file(jobs)
