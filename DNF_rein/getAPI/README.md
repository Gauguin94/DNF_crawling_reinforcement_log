# getlog.py  
```python
class getLog:
    def __init__(self):
        pass
```  
>   
> getLog 클래스는 getInfo, logSearch, saveLog, run 메소드로 구성되어 있다.  
>   
```python
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
                            if '불사조' not in log['data']['itemName']:
                                if log['data']['itemRarity'] == '유니크' or log['data']['itemRarity'] == '레전더리' or log['data']['itemRarity'] == '에픽' or log['data']['itemRarity'] == '신화':
                                    temp.append({'before':log['data']['before'], 'result':log['data']['result'], 'date':log['date']})
                                    if log['data']['result'] and (log['data']['before'] >= 12):
                                        print('Item: {}- {}강 {}'.format(log['data']['itemRarity'], log['data']['after'], log['data']['itemName']))
                    normal += 1
                except:
                    error_count += 1
                    error_char.append({'serverId':char['serverId'], 'characterName':char['characterName']})
                    if error_count == 1:
                        print('{}/{} API server down or Freak character: {}(in logSearch step)'.format(num + 1, length, char['serverId']+" "+char['characterName']))
            if normal:
                print(str(num+1)+"/{}".format(length), char['serverId'], char['characterName'])
        return temp, error_char
```  
> NEOPLE Open API 서버에 GET 방식으로 request를 보낸다.  
> 응답받은 로그 중 강화 기록만을 추출하도록 한다.  
> 다만, 불사조 무기나 커먼, 언커먼, 레어 아이템은 개인적으로 불필요한 데이터라고 생각하기 때문에  
> 이는 제외시키도록 한다.  
