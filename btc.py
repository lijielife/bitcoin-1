import requests
import datetime
from bs4 import BeautifulSoup

#抓取
url = "https://www.okcoin.cn/"
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'html.parser')
mess = soup.find(id="dataTradePriceBtc")
price = mess.get_text()

#时间
time = datetime.datetime.now()
time.strftime('%Y-%m-%d %H:%M')
nowtime = time.strftime('%Y-%m-%d %H:%M')

#存储
f = open('index.html', 'a+')
f.truncate()
f.write('<p contenteditable="true"><code>时间：</code>' + nowtime + "</p>" + "\n" + '<p contenteditable="true"><code>价格：</code>' + price + "</p>\n")
f.close()
