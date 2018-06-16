# from urllib.request import urlopen
# import urllib.request    
# from bs4 import BeautifulSoup
# import pyexcel
# url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
# dict_cafef = []

# #1. Download web page
# html = urlopen(url).read().decode('utf-8')
# #2. Extract ROI (Regiom of interest)
# soup = BeautifulSoup(html, "html.parser")
# ul = soup.find("table", id="tableContent")
# li_list = ul.find_all("td", "b_r_c")
# for 
#     new_dict = {
#     "Title" : 
#     "Quy 4 - 2016": ,
#     "Quy 1 - 2017": ,
#     "Quy 2 - 2017": ,
#     "Quy 3 - 2017": 
#     }
#     dict_cafef.append(new_dict)
#     #Đoạn này đang k biết lấy string ra kiwwur gì vì nó nằm trong table
# pyexcel.save_as(records=dict_cafef, dest_file_name="cafef_vinamilk.xlsx")
