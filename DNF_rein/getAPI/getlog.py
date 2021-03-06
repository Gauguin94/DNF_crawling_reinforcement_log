import urllib3
from json import loads
from datetime import datetime, timedelta
from .consts import*

def whatTime():
    time = datetime.now()
    time = time.strftime("%y%m%d%H%M")
    date = time[:6]
    return date

def transform(time):
    time_temp = time.strftime("%y%m%d%H%M")
    time_first = time_temp[:6]
    time_last = time_temp[-4:-2]
    time = '20{}T{}00'.format(time_first, time_last)
    return time

class getLog:
    def __init__(self):
        pass

    def getInfo(self):
        info_dict = []
        f = open('/home/kkn/DNF_rein/output/character_list/name_list_{}.txt'.format(whatTime()), 'r')
        for character in f:
            info = character.split(" ")
            info_dict.append({'serverId':info[0], 'characterId':info[1], 'characterName':info[2].replace('\n', '').strip()})
        f.close()
        return info_dict

    def logSearch(self, char_info):
        temp = []
        error_char = []
        length = len(char_info)
        for num, char in enumerate(char_info):
            error_count = 0
            normal = 0
            start = datetime(2018, 8, 9, 6, 0)
            deadline = datetime.now()
            day = (deadline-start).days + 1
            for i in range(1, day):
                if i == 1:
                    origin = start
                start_time = transform(start)
                end = origin + timedelta(days = i)
                end_time = transform(end)
                try:
                    http = urllib3.PoolManager()
                    url = 'https://api.neople.co.kr/df/servers/{}/characters/{}/timeline?limit={}&code={}&startDate={}&endDate={}&apikey={}'\
                        .format(char['serverId'], char['characterId'], LIMIT, REINFORCE, start_time, end_time, APIKEY)
                    req = http.request('GET', url)
                    info = loads(req.data.decode('utf-8'))
                    start = end
                    if len(info['timeline']['rows']):
                        for log in info['timeline']['rows']:
                            if '?????????' not in log['data']['itemName']:
                                if log['data']['itemRarity'] == '?????????' or log['data']['itemRarity'] == '????????????' or log['data']['itemRarity'] == '??????' or log['data']['itemRarity'] == '??????':
                                    temp.append({'before':log['data']['before'], 'result':log['data']['result'], 'date':log['date']})
                                    if log['data']['result'] and (log['data']['before'] >= 12):
                                        print('Item: {}- {}??? {}'.format(log['data']['itemRarity'], log['data']['after'], log['data']['itemName']))
                    normal += 1
                except:
                    error_count += 1
                    error_char.append({'serverId':char['serverId'], 'characterName':char['characterName']})
                    if error_count == 1:
                        print('{}/{} API server down or Freak character: {}(in logSearch step)'.format(num + 1, length, char['serverId']+" "+char['characterName']))
            if normal:
                print(str(num+1)+"/{}".format(length), char['serverId'], char['characterName'])
        return temp, error_char

    def saveLog(self, log_list, error_list):
        filename = whatTime()
        f = open('/home/kkn/DNF_rein/output/rein_{}_log.txt'.format(filename),'w')
        for line in log_list:
            f.write(str(line['before'])+" "+str(line['result'])+" "+line['date']+'\n')
        f.close()
        f = open('/home/kkn/DNF_rein/output/character_list/error_log.txt','w')
        try:
            for line in error_list:
                f.write(line['serverId']+" "+line['characterName'])
            f.close()
        except:
            f.close()
        print('Finish!')
        return 0

    def run(self):
        char_info = self.getInfo()
        log_list, error_list = self.logSearch(char_info)
        self.saveLog(log_list, error_list)
        return 0