import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "https://www.glassdoor.co.in/Job/software-engineer-intern-jobs-SRCH_KO0,24.htm?minRating=4.0"
# URL = "https://www.glassdoor.co.in/Job/software-jobs-SRCH_KO0,24.htm"
# URL = "https://www.glassdoor.co.in/Job/index.htm"
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"}

session = requests.Session()
page = session.get(URL, headers=headers)
# print(page.content)

# print(page.status_code)
content = page.text
soup = BeautifulSoup(content, 'html.parser')

job_titles = []
links = []
company_names = []
locations = []

conn = sqlite3.connect('jobsdata.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM job_listings")
cursor.execute('''CREATE TABLE IF NOT EXISTS job_listings(
               title TEXT,
               company TEXT,
               location TEXT,
               url TEXT 
               )
         ''')

conn.commit()

for element in soup.find_all('div', attrs={'class': 'jobCard JobCard_jobCardContent__0_4vj'}):

    job_titles.append(element.find('a', attrs={'class': 'JobCard_seoLink__WdqHZ'}).text)
    company_names.append(element.find('span', attrs={'class': 'EmployerProfile_employerName__Xemli'}).text)
    links.append(element.find('a', attrs={'class': 'JobCard_seoLink__WdqHZ'})['href'])
    locations.append(element.find('div', attrs={'class': 'JobCard_location__N_iYE'}).text)

    cursor.execute('''INSERT INTO job_listings(title, company, location, url) VALUES(?,?,?,?)''', (job_titles[-1], company_names[-1], locations[-1], links[-1]))
    conn.commit()

# print(job_titles)
# print(company_names)
# print(links)
# print(locations)

for entry in cursor.execute("SELECT * FROM job_listings"):
    print(entry)