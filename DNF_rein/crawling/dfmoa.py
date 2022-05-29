import ssl
import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .consts import*
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
context = ssl._create_unverified_context()

class dunfaMoa:
    def __init__(self, search_url, num):
        self.search_url = search_url
        self.filename = num

    def loadAdv(self):
        adv_url = []
        href_info = []
        sourcecode = urlopen(self.search_url, context=context, timeout = 600).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        for href in soup.find("div", class_="Wrapper-sc-1noqpd4-1 gfctoN").find_all("a"):
            href_info.append(href)
        for url in href_info:
            if 'href' in url.attrs and 'class' in url.attrs:
                if url.attrs['class'] == ['Row-sc-jrfk9d-1', 'hiKazl']:
                    adv_url.append(RAW_URL + url.attrs['href'])
        return adv_url
    
    def loadChar(self, adv_url):
        adv_link = []
        char_info = []
        for url in adv_url:
            try:
                sourcecode = urlopen(url, context=context, timeout = 600).read()
                soup = BeautifulSoup(sourcecode, "html.parser")
                
                for href in soup.find("div", class_ = 'Outer-sc-1cu42wh-3 kCIUEG').find_all("a"):
                    adv_link.append(href)
                for data in adv_link:
                    if 'href' in data.attrs:
                        temp = data.attrs['href'].replace("/characters/", "")
                        temp = self.saveServer(temp)
                        char_info.append(temp)
            except:
                continue
        return char_info

    def saveServer(self, temp):
        temp_ = {}
        for serverName in ALLSERVER:
            if serverName in temp:
                temp = temp.replace(serverName, "")
                servername = serverName.replace('/', "")
                temp_= {'serverName':'{}'.format(servername), 'characterName':'{}'.format(temp)}
        return temp_

    def saveCharinfo(self, char_name):
        f = open('/home/kkn/DNF_rein/crawling/dfmoa_list/{}.txt'.format(self.filename),'w')
        for name in char_name:
            f.write(str(name['characterName'])+'\n')
        f.close()
        return 0

    def run(self):
        char_info = []
        adv_url = self.loadAdv()
        char_info.extend(self.loadChar(adv_url))
        self.saveCharinfo(char_info)
        return 0