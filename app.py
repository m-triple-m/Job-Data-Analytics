from flask import Flask, render_template, request, redirect, url_for
from gen_Charts import GenChart
from scraper import extract
import pandas as pd

app = Flask(__name__)

chart_obj = GenChart()


charts = []


@app.route('/')
def Home():
    # initCharts()
    job = request.args.get('message')
    charts = []
    chart_obj.loadData('jobs.csv')
    if job:
        charts = [
            {
                'title': 'Top Rated Job Titles',
                'image': chart_obj.topTitleRating('bar1.jpg')
            },
            {
                'title': 'Top Locations',
                'image': chart_obj.topLocations('bar2.jpg')
            },
            {
                'title': 'Job Title Experience',
                'image': chart_obj.expBar('bar3.jpg')
            },
            {
                'title': 'Job Title Salary',
                'image': chart_obj.salBar('bar4.jpg')
            },
            {
                'title': 'Job Companies',
                'image': chart_obj.topCompany('bar5.jpg')
            },
            {
                'title': 'Salary Distribution',
                'image': chart_obj.reveiwHist('hist1.jpg')
            },
            {
                'title': 'Company Post History',
                'image': chart_obj.postHistory('pie1.jpg')
            },
            {
                'title': 'Top Reviewed Companies',
                'image': chart_obj.topReviewed('bar6.jpg')
            },
            # {
            #     'title': 'Common words in Job Titles',
            #     'image': chart_obj.titleWordCloud('cloud1.jpg')
            # },
        ]
    return render_template('home.html', charts=charts, message=job)


@app.route('/searchjobs', methods=['POST'])
def handleInput():
    # print(request.method)
    if request.method == 'POST':
        job = request.form.get('jobname')
        print(job)
        scrapData(job)
        return redirect(url_for('Home', message=job))


def scrapData(jobname):
    data = []
    for i in range(1, 3):
        if i == 1:
            data = data+extract(job=jobname)
        else:
            data = data+extract(page=i, job=jobname)

    df = pd.DataFrame(data)
    df.to_csv("jobs.csv")
    print(data)

# def initCharts():
#     charts.append()


if __name__ == '__main__':
    app.run()
