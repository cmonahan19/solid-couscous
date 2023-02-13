
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

htmlFile = "/Users/carolinemonahan/Desktop/TopSongs"


url = 'https://acharts.co/us_singles_top_100'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')

pageNum = 1
print(soup.title.string)


with open(htmlFile,'w', encoding = 'utf8') as file:
    file.write(soup.prettify())

Names = []
Ranks = []
PrevRanks = []
Artists = []
Peaks = []




print(soup)




with open(htmlFile,'r', encoding= 'utf8') as file:
    html = file.read()
    soup = BeautifulSoup(html, 'html.parser')


songs = soup.find_all('tr', itemprop="itemListElement")




for song in songs:
    Rank=song.find('span', itemprop='position').text
    PrevRank=song.find('td', class_='cStats cMhidden').text
    Name=song.find('a', itemprop= 'url').text
    Artist=song.find('span',itemprop='byArtist').text.strip()
    Peak = song.find('td', class_='cStats cShidden').text
        
    if not Name:
        Name = 'NA'
    if not Rank:
        Rank = 'NA'
    if not PrevRank:
        PrevRank = 'NA'
    if not Artist:
        Artist = 'NA'
    if not Peak:
        Peak = 'NA'

        
    Names.append(Name)
    Ranks.append(Rank)
    PrevRanks.append(PrevRank)
    Artists.append(Artist)
    Peaks.append(Peak)




print(Artists)


print(Ranks)


print(PrevRanks)


print(Names)


print(Peaks)



data = {
    'Rank': Ranks,
    'Title': Names,
    'Artist':Artists,
    'Previous Rank':PrevRanks,
    'Peak Position':Peaks,
}


dataframe = pd.DataFrame(data)


dataframe = dataframe.replace(r'\n','', regex=True)
dataframe = dataframe.replace(r'\t','', regex=True)
dataframe = dataframe.replace(r'\s\s\s','', regex=True)
dataframe = dataframe.set_index(['Rank'])


print(dataframe)



fileName = dataframe.to_csv('/Users/carolinemonahan/Desktop/Top100Singles.csv', encoding='utf-8')



readFile = open(r'/Users/carolinemonahan/Desktop/Top100Singles.csv', 'r', encoding='utf8')
line = readFile.readline().replace(',',' ')
while line != '':
    line = readFile.readline().replace('\n', '')
    lineList=line.split(',')
readFile.close()


def aretheyatopartist():
    topartist = input('Please enter an artist:')
    if topartist in Artists:
        print(topartist+' has a song in the top 100 singles.')
    else:
        print(topartist+' does not have a song in the top 100 singles.')



aretheyatopartist()



ranking = int(input('Enter a current ranking:'))
try:
    if ranking >100:
        raise IndexError('The inputted ranking can\'t be greater than 100. The chart only shows the top 1-100 songs.')
    else:
        rankinginlist = Ranks[ranking]
        print(Names[ranking-1])
except IndexError as errorMessage:
    print(errorMessage)


whatranking = int(input('Enter a ranking, 1-100:'))
songrank =(Names[whatranking-1])
def songandranking(whatranking):
    songrank =(Names[whatranking-1])
    return songrank
print (songrank)




