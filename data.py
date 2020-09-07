import keys.db as dbm
import mysql.connector

mydb = mysql.connector.connect(
    host=dbm.host,
    user=dbm.user,
    passwd=dbm.password,
    database=dbm.db
)


def fetch_songs():
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    table_chart = []

    for line in mycursor.fetchall():
        table_chart.append(line[0])

    songs = {}
    for year in table_chart:
        song_select = f"SELECT title, artist FROM {year};"
        mycursor.execute(song_select)
        for line in mycursor.fetchall():
            songs[line[0].replace("\n", "")] = line[1].replace("\n", "")
    mycursor.close()
    mydb.close()
    return songs


if __name__ == "main":
    pass
