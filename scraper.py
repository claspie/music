from requests import get
from bs4 import BeautifulSoup as bs
from time import time
from datetime import datetime as DateTime, timedelta as TimeDelta
from db import fetch, insert


def scrape(weeks):
    """
    Creating a list of dates for the charts
    """
    spec_date = DateTime(2002, 12, 8)
    delta = 7
    date_list = [spec_date]
    x = 1
    # chart = [];

    while x <= weeks:
        if x <= weeks:
            new = spec_date + TimeDelta(delta)
            date_list.append(new)
            spec_date = new
        x += 1
    """
    Use the dates in the list of dates generated to scrape the webpages
    """
    for date in date_list:
        url = "https://top40-charts.com/chart.php?cid=25&date=" + date.strftime('%Y-%m-%d')

        website = bs(get(url).text, 'html.parser')
        chart_songs = website.find_all("tr", "latc_song")

        def gen_track(index, bs_data):
            try:
                song = bs_data[index].find("div").find("a").get_text()
                artist = bs_data[index].find("div").next_sibling.get_text()
                return {
                    "song": song,
                    "artist": artist
                }
            except Exception as e:
                print(e)

        for i in range(0, 40):
            track_song = gen_track(i, chart_songs)

            insert(track_song["song"], track_song["artist"])

    return "done"


if __name__ == "__main__":
    try:
        """
        Enter number of weeks, in this case 100
        """
        start_time = time()
        result = scrape(100)
        print(time() - start_time, " seconds")
    except Exception as error:
        print(error)
