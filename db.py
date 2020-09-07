import mysql.connector as dbm
from keys.db import host, user, password, db, port

mydb = dbm.connect(
    host=host,
    user=user,
    passwd=password,
    database=db
)


def fetch(*args):
    if len(args) == 0:
        try:
            query = f"SELECT DISTINCT songname, artistname FROM charts.uksongs;"
            cursor = mydb.cursor()

            cursor.execute(query)
            result = cursor.fetchall()

            table = []
            for row in result:
                results = {
                    "name": row[0],
                    "artist": row[1]
                }
                table.append(results)
            mydb.close()
            return table

        except Exception as error:
            print(error)

    elif len(args) == 1:
        try:
            query = f"SELECT DISTINCT songname, artistname FROM charts.uksongs LIMIT {int(args[0])};"
            cursor = mydb.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            table = []
            for row in result:
                results = {
                    "name": row[0],
                    "artist": row[1]
                }
                table.append(results)
            mydb.close()
            return table

        except Exception as error:
            print(error)


def insert(song, artist):
    try:
        songname = str(song)
        artistname = str(artist)
        query = f'''INSERT INTO charts.uksongs (songname, artistname)
            VALUES ("{songname}", "{artistname}");'''
        cursor = mydb.cursor()
        cursor.execute(query)

        mydb.commit()
        mydb.close()

        print("row added")
    except Exception as error:
        print(error)
        mydb.rollback()


if __name__ == "__main__":
    songs = fetch()
    print(len(songs))
