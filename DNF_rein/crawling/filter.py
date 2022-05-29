import os
import sys
from .consts import*
from .dfmoa import*
from json import loads
from datetime import datetime, timedelta
import urllib3

path = '/home/kkn/DNF_rein/crawling/dfmoa_list/'

def whatTime():
    time = datetime.now()
    time = time.strftime("%y%m%d%H%M")
    date = time[:6]
    return date

class filtering:
    def __init__(self):
        pass

    def deldupl(self, list):
        update_list = []
        for i, name in enumerate(list):
            if name not in update_list:
                update_list.append(name)
        return update_list

    def dataLoad(self):
        filelist = []
        rawlist = []
        filelist_ = os.listdir(path)
        for file in filelist_:
            if 'txt' in file:
                filelist.append(file)
        for txt in filelist:
            f = open(path + txt, 'r', encoding = 'UTF8')
            try:
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    rawlist.append(name)
                f.close()
            except:
                f.close()
                f = open(path + txt, 'r', encoding = 'cp949')
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    rawlist.append(name)
                f.close()
        charlist = self.deldupl(rawlist)
        return charlist

    def getInfo(self):
        char_list = []
        error_count = 0
        decoded_list = self.dataLoad()
        http = urllib3.PoolManager()
        for time, hash in enumerate(decoded_list):
            try:
                url = 'https://api.neople.co.kr/df/servers/{}/characters?characterName={}&limit={}&wordType={}&apikey={}'\
                        .format('all', hash, '200', 'match', APIKEY)
                req = http.request('GET', url)
                search_info = loads(req.data.decode('utf-8'))
                if len(search_info['rows']) >= 1:
                    for individual_info in search_info['rows']:
                        if individual_info['level'] > FWLV:
                            char_list.append({"serverId":individual_info['serverId'], "characterId":individual_info['characterId'], "characterName":individual_info['characterName']})
                            print(time, individual_info['characterName'])
            except:
                error_count += 1
                print("API server down or Freak character. [Error Count : {}]".format(error_count))
        char_list = self.deldupl(char_list)
        filename = whatTime()
        f = open("/home/kkn/DNF_rein/data/{}_4.txt".format(filename),'w')
        for line in char_list:
            f.write(line['serverId']+" "+line['characterId']+" "+line['characterName']+'\n')
        f.close()
        print('Success! and Error count: {}'.format(error_count))
        return 0

    def run(self):
        self.getInfo()
        return 0