import mysql.connector as dbm
from keys.db import host, user, password, db, port

mydb = dbm.connect(
    host=host,
    user=user,
    passwd=password,
    database=db
)


def create_table():
    with mydb.cursor() as cursor:
        try:
            new_table = "songs"
            query = f"""
            CREATE TABLE IF NOT EXISTS {new_table}(
                id INT AUTO_INCREMENT NOT NULL,
                songname VARCHAR(255) NOT NULL,
                artistname VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            );
            """
            cursor.execute(query)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    create_table()
