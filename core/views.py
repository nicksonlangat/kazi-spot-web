from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    jobs=[]
    url='https://retro.ihub.co.ke/jobs'
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    rows=soup.find_all(class_='jobsboard-row')
    for r in rows:
        title=r.find('h3').text
        location=r.find(class_='job-location').text
        cat=r.find(class_='job-cat').text
        company=r.find(class_='post-company').text
        company_url=r.find('a',class_='post-company')['href']
        description=r.find(class_='post-description').text
        detail=r.find('a', class_='job-more')
        detail2=detail.get('href')
        time=r.find(class_='job-time').text
        # print(title,time,description,detail, '\n')
        job={
             'title':title,
             'cat':cat,
             'location':location,
             'company':company,
             'description':description,
             'detail':detail2,
             'time':time,
             'company_url':company_url,
        }
        jobs.append(job)
    return jobs

def load_jobs(request):
    jobs=scrape_jobs()
    context={
        'jobs':jobs,
    }
    return render(request, 'index.html', context )