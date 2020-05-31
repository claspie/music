from flask import Flask, jsonify, redirect, request
from auth import app_auth, user_auth
import mysql.connector, keys.dbm as dbm

mydb = mysql.connector.connect(
    host = dbm.host,
    user = dbm.user,
    passwd = dbm.password,
    database = dbm.db
)

def Fetch_Songs():
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    table_chart = []

    for line in mycursor.fetchall():
        table_chart.append(line[0])

    song_table = {}
    songs = {}
    for year in table_chart:
        song_select = f"SELECT title, artist FROM {year};"
        mycursor.execute(song_select)
        for line in mycursor.fetchall():
            songs[line[0].replace("\n", "")] = line[1].replace("\n", "")
    mycursor.close()
    mydb.close()
    return songs