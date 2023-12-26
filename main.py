from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

firefox_driver_path = "/usr/bin/fierfox"
driver = webdriver.Firefox(executable_path=firefox_driver_path)

url = "https://www.glassdoor.co.in/Job/software-engineer-intern-jobs-SRCH_KO0,24.htm?minRating=4.0"

# url = input("Enter the url of the job you want to apply for")

driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

job_titles = []
links = []
company_names = []
locations = []
job_id = []


for element in soup.find_all('div', attrs={'class': 'jobCard JobCard_jobCardContent__0_4vj'}):
    job_titles.append(element.find('a', attrs={'class': 'JobCard_seoLink__WdqHZ'}).text)
    company_names.append(element.find('span', attrs={'class': 'EmployerProfile_employerName__Xemli'}).text)
    links.append(element.find('a', attrs={'class': 'JobCard_seoLink__WdqHZ'})['href'])
    locations.append(element.find('div', attrs={'class': 'JobCard_location__N_iYE'}).text)


print(job_titles)
