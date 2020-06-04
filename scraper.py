from requests import get;
from bs4 import BeautifulSoup as bs;
from time import sleep, time;
from datetime import datetime as DateTime, timedelta as TimeDelta;
from threading import Thread;
from multiprocessing.pool import ThreadPool;
from db import fetch, insert;


def scrape(weeks):
    spec_date = DateTime(2002, 12, 8);
    delta = 7;
    date_list = [spec_date]
    chart = [];

    for x in range(1, weeks + 1):
        if x <= weeks:
            new = spec_date + TimeDelta(delta)
            date_list.append(new);
            spec_date = new
    for date in date_list:
        url = "https://top40-charts.com/chart.php?cid=25&date=" + date.strftime('%Y-%m-%d')



        website = bs(get(url).text, 'html.parser');
        chart_songs = website.find_all("tr", "latc_song")

        for i in range(40):
            try:
                song = chart_songs[i].find("div").find("a").get_text();
                artist = chart_songs[i].find("div").next_sibling.get_text();
                track = {
                    "song": song,
                    "artist": artist
                }
                chart.append(track)
            except Exception as error:
                print(error)

    return chart;


def fast_scrape(weeks):
    spec_date = DateTime(2002, 12, 8);
    delta = 7;
    date_list = []; date_list.append(spec_date);
    x = 1;
    #chart = [];

    while x <= weeks:
        if x <= weeks:
            new = spec_date + TimeDelta(delta)
            date_list.append(new);
            spec_date = new
        x += 1;

    with ThreadPool(processes=80) as first_thread:
        for date in date_list:
            url = "https://top40-charts.com/chart.php?cid=25&date=" + date.strftime('%Y-%m-%d')
    
        

            website = bs(get(url).text, 'html.parser');
            chart_songs = website.find_all("tr", "latc_song")

            def gen_track(index, bs_data):
                try:
                    song = bs_data[index].find("div").find("a").get_text();
                    artist = bs_data[index].find("div").next_sibling.get_text();
                    track = {
                        "song": song,
                        "artist": artist
                    }
                    return track;
                except Exception as error:
                    pass
                    
            for i in range(0, 40):
                
                track_song = gen_track(i, chart_songs)
                
                insert(track_song["song"], track_song["artist"])

            print("Done for ", date.strftime('%Y-%m-%d'))
        print("Done for ", date.strftime('%Y-%m-%d'))
            
    return "done";


if __name__ == "__main__":

    try:
        pool = ThreadPool(processes=1);
        start_time = time();
        result = pool.apply_async(fast_scrape, (450, ))
        data = result.get()
        print(len(data))
        print(time() - start_time, " seconds")
    except Exception as error:
        print(error)