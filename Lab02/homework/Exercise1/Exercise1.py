from youtube_dl import YoutubeDL
from urllib.request import urlopen
import urllib.request    
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs"

#1. Download web page
html = urlopen(url).read().decode('utf-8')

#2. Extract ROI (Regiom of interest)
soup = BeautifulSoup(html, "html.parser")
ul = soup.find("section", "section chart-grid")
li_list = ul.find_all("li")

dict_topsong = []
for li in li_list:
    h3 = li.h3
    h4 = li.h4

    new_dict = {
    "Names" : h3.string,
    "Artists":  h4.string
    }
    dict_topsong.append(new_dict)
    
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    song_name = h3.string + " " + h4.string
    dl.download([song_name])
pyexcel.save_as(records = dict_topsong, dest_file_name = "topsong.xlsx")

