#Playlist Creator
This project collects chart data from a specific website and stores it in a database.
With the database data, it creates a playlist on Spotify.

<ul>The scraping was synchronously in order to respect the website and not flood them with requests</ul>
<ul>The weekly charts went up to 500 weeks so it was a great idea to not make it asynchronous</ul>
<ul>The same applies to the playlist creation process. It was not made asynchronously in order to keep within Spotify's rate limits when using a developer account registered for personal purposes.</ul>
<ul>Moving this to a production environment, all of this including the server framework would be async</ul>

####Setup
<ul>Add database variables in the db.py file inside the keys directory</ul>
<ul>Add your Spotify Client ID and Secret using the Keyring "set_password" method</ul>

####Running Project
<ul>Edit scraper.py to change the first chart you want to collect and the number of charts you want, the charts are weekly</ul>

