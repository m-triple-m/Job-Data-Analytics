import pandas as pd
import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDSip[;'\/p[;'8520/]996+]


class GenChart:
    def __init__(self, path="jobs.csv"):
        self.loadData(path)

        # self.df['Job_Post_History'] = self.df['Job_Post_History'].apply(
        #     lambda r: r.split()[0])

    def loadData(self, path):
        self.df = pd.read_csv(path)
        self.df.drop(columns=['Unnamed: 0'], inplace=True)

        # cleaning
        self.df['Reviews'] = self.df['Reviews'].apply(

            lambda r: r.strip('()').split()[0])
        self.df['Reviews'] = self.df['Reviews'].astype('int')

        self.df['Location'] = self.df['Location'].apply(
            lambda r: r.split('(')[0].strip())

        self.df['Experience'] = self.df['Experience'].apply(
            lambda r: r.split('(')[0].strip())

        self.df['Salary'] = self.df['Salary'].apply(
            lambda r: r.split('(')[0].strip())

    def topTitleRating(self, path):
        self.df.sort_values('Ratings', ascending=False).set_index(
            'Title')['Ratings'].head(10).plot(kind='barh', width=0.8, figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def topLocations(self, path):
        self.df.groupby('Location').count()['Title'].plot(
            kind='barh', figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def expBar(self, path):
        self.df.groupby('Experience').count()[
            'Title'].plot(kind='bar', figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def salBar(self, path):
        self.df.groupby('Salary').count()['Title'].plot(
            kind='bar', figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def topCompany(self, path):
        self.df.set_index('Company').groupby('Company').max().sort_values(
            'Reviews', ascending=False)['Reviews'].head().plot(kind="bar", figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def reveiwHist(self, path):
        self.df['Reviews'].plot(kind="hist", figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def postHistory(self, path):
        data = self.df.groupby('Job_Post_History').count()

        data[
            'Title'].plot(kind='pie', autopct="%1.1f%%", pctdistance=1.2, labels=None, figsize=(20, 10))
        plt.legend(data.index, loc="upper left")
        plt.axis('equal')
        plt.savefig('static/'+path)
        plt.close()
        return path

    def topReviewed(self, path):
        self.df.sort_values('Reviews', ascending=False).set_index(
            'Company')['Reviews'].head(10).plot(kind='barh', width=0.8, figsize=(20, 10))
        plt.xticks(rotation=30)
        plt.savefig('static/'+path)
        plt.close()
        return path

    def avgRating(self, path):
        pass
