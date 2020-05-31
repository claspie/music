import sqlite3;
from sqlite3 import Error;

def insert_song(song, artist):
    conn = sqlite3.connect('charts.db');
    insert = f"""INSERT INTO uksongs(songname, artistname)
    VALUES('{song}', '{artist}')"""
    try:
        conn.execute(insert)
        conn.commit()
        return "success"
    except Error as e:
        conn.rollback()
        print(e)

def fetch_songs():
    conn = sqlite3.connect('charts.db');
    songlist = [];
    fetch = f"SELECT * FROM uksongs"
    cursor = conn.execute(fetch);
    conn.commit()
    row = cursor.fetchone();
    if row != None:
        print("There are no rows");
    else:
        print("There are ", row[0], " rows.")
        return(row[0])
    conn.close();


# row = cursor.fetchone();
# if row != None:
#     print("There are no rows");
# else:
#     print("there are ", row, " rows.")
# conn.close();


if __name__ == "__main__":
    pass;