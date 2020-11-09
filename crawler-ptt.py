#抓取ptt八卦版標題，頁數自訂
import urllib.request as req
import bs4
def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", 
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
#抓取三頁
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1