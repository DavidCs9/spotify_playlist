from spotify import sp, user_id
import requests
from bs4 import BeautifulSoup

date = input("Hola! Que fecha quieres para crear tu playlist? Ingresa la fecha en el siguiente formato: YYYY-MM-DD:")
billboard = "https://www.billboard.com/charts/hot-100/"
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)
billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")
songs_list = []
song_1 = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s "
                                                                "u-letter-spacing-0021 u-font-size-23@tablet "
                                                                "lrv-u-font-size-16 u-line-height-125 "
                                                                "u-line-height-normal@mobile-max a-truncate-ellipsis "
                                                                "u-max-width-245 u-max-width-230@tablet-only "
                                                                "u-letter-spacing-0028@tablet")

songs_titles_from_2_100 = soup.find_all(name="h3", id="title-of-a-story",
                                        class_="c-title a-no-trucate a-font-primary-bold-s "
                                               "u-letter-spacing-0021 lrv-u-font-size-18@tablet "
                                               "lrv-u-font-size-16 u-line-height-125 "
                                               "u-line-height-normal@mobile-max "
                                               "a-truncate-ellipsis u-max-width-330 "
                                               "u-max-width-230@tablet-only")

song_titles = song_1 + songs_titles_from_2_100

for song in song_titles:
    songs_list.append(song.text.strip())
songs_uri_list = []

for song in songs_list:
    result = sp.search(q=song, offset=0, limit=1, type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri_list.append(uri)
    except IndexError:
        print(f"{song} doesnt exist in Spotify. Skipped!")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Top 100", public=False, description=f"Top 100 Billboard de {date}.")
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri_list)