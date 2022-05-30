import os
from datetime import datetime
import urllib3
from json import loads
from urllib.request import urlopen
APIKEY = '당신의 API key를 입력하세요'

def whatTime():
    time = datetime.now()
    time = time.strftime("%y%m%d%H%M")
    date = time[:6]
    return date

class makeData:
    def __init__(self):
        pass

    def loadData(self):
        path = '/home/kkn/DNF_rein/data/'
        charlist = []
        filelist = []
        filelist_ = os.listdir(path)
        for file in filelist_:
            if 'txt' in file:
                filelist.append(file)
        for txt in filelist:
            f = open(path + txt, 'r', encoding = 'UTF8')
            try:
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    charlist.append(name)
                f.close()
            except:
                f.close()
                f = open(path + txt, 'r', encoding = 'cp949')
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    charlist.append(name)
                f.close()
        charlist = self.deldupl(charlist)
        return charlist

    def deldupl(self, list):
        update_list = []
        for i, name in enumerate(list):
            if name not in update_list:
                update_list.append(name)
        return update_list

    def onemoreFilter(self, list):
        char_list = []
        http = urllib3.PoolManager()
        for char in list:
            try:
                url = 'https://api.neople.co.kr/df/servers/{}/characters/{}/equip/equipment?apikey={}'\
                    .format(char.split(" ")[0], char.split(" ")[1], APIKEY)
                req = http.request('GET', url)
                search_info = loads(req.data.decode('utf-8'))
                if search_info['equipment'][0]['reinforce'] > 12:
                    char_list.append(char)
                    print("{} is what i want.".format(char.split(" ")[2]))
                else:
                    print("{} is useless data".format(char.split(" ")[2]))   
            except:
                print("{} is freak".format(char.split(" ")[2]))
        return char_list

    def saveData(self, charlist):
        filename = whatTime()
        f = open('/home/kkn/DNF_rein/output/character_list/name_list_{}.txt'.format(filename), 'w')
        for line in charlist:
            f.write(line+'\n')
        f.close()
        return 0

    def run(self):
        char_list = []
        char_list = self.loadData()
        char_list = self.onemoreFilter(char_list)
        self.saveData(char_list)
        return char_list
