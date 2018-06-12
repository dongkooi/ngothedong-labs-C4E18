from urllib.request import urlopen
import urllib.request    
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com.vn"
dict_dantri = []

#1. Download web page
# from urllib.request import urlopen
# html = urlopen("http://dantri.com.vn").read().decode('utf-8')
# print(html)
#1.1 Create a connection
conn = urlopen(url)
#1.2 Read
data = conn.read()
#1.3 Decode
html_content = data.decode('utf-8')
# print(html_content)

# Save html_Content to file 
#1. urllib.request.urlretrieve(url, "dantri.html")
#2.
#  f = open("dantri.html", "wb")
# f.write(data)
# f.close()
#2. Extract ROI (Regiom of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())
li_list = ul.find_all("li")
for li in li_list:
    # print(li.prettify())
    # print("* " * 20)
    # h4 = li.find("h4")
    # a = h4.find("a")
    a = li.h4.a
    # print(url + a['href'], a.string, sep="")
    new_dict = {
    "Link" : url + a['href'],
    "Nội dung":  a.string
    }
    dict_dantri.append(new_dict)
pyexcel.save_as(records=dict_dantri, dest_file_name="dantri.xlsx")


#3. Extract info
