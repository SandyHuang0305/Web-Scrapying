#大學排行
import requests
from bs4 import BeautifulSoup

def getHTMLText(url): #爬訊息
    try:
        r = requests.get(url, timeout =30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

import bs4
def fillUnivList(ulist, html):#將頁面放到列表
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])   

def printUnivList(ulist, num): #打出列表並設定要輸出幾所學校
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format('排名', '學校名稱', '總分',chr(12288)))
    for i in range(num): #要輸出的數量
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
main()