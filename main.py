import requests
from bs4 import BeautifulSoup

# URL = "https://www.glassdoor.co.in/Job/software-engineer-intern-jobs-SRCH_KO0,24.htm?minRating=4.0"
URL = "https://www.glassdoor.co.in/Job/software-jobs-SRCH_KO0,8.htm"
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"}

page = requests.get(URL, headers=headers)
# print(page.content)

# print(page.status_code)
content = page.text
soup = BeautifulSoup(content, 'html.parser')

job_titles = []
links = []
company_names = []
locations = []

for element in soup.find_all('div', attrs={'class': 'jobCard JobCard_jobCardContent__0_4vj'}):

    job_titles.append(element.find('a', attrs={'class': 'JobCard_seoLink__WdqHZ'}).text)
    company_names.append(element.find('span', attrs={'class': 'EmployerProfile_employerName__Xemli'}).text)
    links.append(element.find('a', attrs={'class': 'JobCard_seoLink__WdqHZ'})['href'])
    locations.append(element.find('div', attrs={'class': 'JobCard_location__N_iYE'}).text)

# print(job_titles)
# print(company_names)
# print(links)
print(locations)
