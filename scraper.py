import pandas as pd
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


def extract(url="", page=0, job="financial analyst"):

    if page:
        url = f"https://www.naukri.com/{'-'.join(job.split())}-jobs-{page}?k={'%20'.join(job.split())}"
    else:
        url = f"https://www.naukri.com/{'-'.join(job.split())}-jobs?k={'%20'.join(job.split())}"

    print(url)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    driver.close()

    results = soup.find(class_='list')

    job_elems = results.find_all('article', class_='jobTuple bgWhite br4 mb-8')
    len(job_elems)

    datalist = []
    for idx, job_elem in enumerate(job_elems):
        print(idx)
        # URL to apply for the job
        URL = job_elem.find('a', class_='title fw500 ellipsis').get('href')
    #     print(URL.strip())

        # Post Title
        Title = job_elem.find('a', class_='title fw500 ellipsis')

        # Company Name
        Company = job_elem.find('a', class_='subTitle ellipsis fleft')

        # Ratings
        rating_span = job_elem.find('span', class_='starRating fleft dot')
        if rating_span is None:
            continue
        else:
            Ratings = rating_span.text

        # Reviews Counts
        Review_span = job_elem.find(
            'a', class_='reviewsCount ml-5 fleft blue-text')
        if Review_span is None:
            continue
        else:
            Reviews = Review_span.text

        # Years of experience Required
        Exp = job_elem.find(
            'li', class_='fleft grey-text br2 placeHolderLi experience')
        Exp_span = Exp.find('span', class_='ellipsis fleft fs12 lh16')
        if Exp_span is None:
            continue
        else:
            Experience = Exp_span.text

        # Salary offered for the job
        Sal = job_elem.find(
            'li', class_='fleft grey-text br2 placeHolderLi salary')
        Sal_span = Sal.find('span', class_='ellipsis fleft fs12 lh16')
        if Sal_span is None:
            continue
        else:
            Salary = Sal_span.text

        # Location for the job post
        Loc = job_elem.find(
            'li', class_='fleft grey-text br2 placeHolderLi location')
        Loc_exp = Loc.find('span', class_='ellipsis fleft fs12 lh16')
        if Loc_exp is None:
            continue
        else:
            Location = Loc_exp.text

        # Number of days since job posted
        Hist = job_elem.find(
            "div", ["type br2 fleft grey", "type br2 fleft green"])
        Post_Hist = Hist.find('span', class_='fleft fw500')
        if Post_Hist is None:
            continue
        else:
            Post_History = Post_Hist.text

        datalist.append({'URL': URL, 'Title': Title.text, 'Company': Company.text, 'Ratings': Ratings, 'Reviews': Reviews,
                        'Experience': Experience, 'Salary': Salary, 'Location': Location, 'Job_Post_History': Post_History})

    #   Appending data to the DataFrame
    return datalist


if __name__ == '__main__':

    data = []
    for i in range(1, 2):
        if i == 1:
            data = data+extract()
        else:
            data = data+extract(page=i)

    df = pd.DataFrame(data)
    df.to_csv("jobs.csv")
    print(data)
