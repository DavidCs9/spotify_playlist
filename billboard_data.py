import requests
from bs4 import BeautifulSoup

# date = input("Hello! Wich year you wanto to travel to? Type the data in this format YYYY-MM-DD:")
# billboard = "https://www.billboard.com/charts/hot-100/"
URL = f"https://www.billboard.com/charts/hot-100/1999-06-08"

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
# print(songs_list)
