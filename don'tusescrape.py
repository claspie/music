from requests import get;
from bs4 import BeautifulSoup as bs;
from time import sleep, time;
from datetime import datetime as DateTime, timedelta as TimeDelta;
from json import dump, dumps, load, loads;

spec_date = DateTime(2002, 12, 8)
delta = 7;
weeks = 524;
x = 1;
date_list = []; date_list.append(spec_date);

while x <= weeks:
    if x <= weeks:
        new = spec_date + TimeDelta(delta)
        date_list.append(new);
        spec_date = new
    x += 1;

for date in date_list:
    url = "https://top40-charts.com/chart.php?cid=25&date=" + date.strftime('%Y-%m-%d')
    
    chart = [];

    website = bs(get(url).text, 'html.parser');
    chart_songs = website.find_all("tr", "latc_song")

    ''' with open ('tracks.json', 'a') as file:
        for i in range(0, 40):
            song = {
                "song": chart_songs[i].find("div").find("a").get_text(),
                "artist": chart_songs[i].find("div").next_sibling.get_text()
            }
            file.write(dumps(song))
            file.write('/n')
        pass; '''

    for i in range(0, 40):
        song = chart_songs[i].find("div").find("a").get_text();
        artist = chart_songs[i].find("div").next_sibling.get_text();

    print(f"Scraped for chart of ", date.strftime('%Y-%m-%d'))
    sleep(1);