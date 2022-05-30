# preprocess.py
```python
class preprocessData:
    def __init__(self):
        pass
```  
>   
> preprocessData 클래스는 loadData, deldupl, onemoreFilter, saveData, run 메소드로 구성되어 있다.  
>   
```python
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
```  
>   
> 13강 이상의 장비를 갖고 있는 캐릭터들을 추려 데이터로 저장하는 작업을 수행한다.  
> 13강의 성공 비율을 보는 것인데 12강을 갖고 있지만 13강에 성공한적이 없는 사람들은 어떻게 할거냐?  
> **성공한 사람들은 어느 시간대에 주로 성공하는가?** <- 목표.  
> 목표를 위해서는 13강 장비를 갖고 있지 않은 분들은 제외하도록 하겠다.  
> 클래스내 다른 메소드들은 DNF_crawling_epic_log repository의  
> data 디렉토리 내 README.md를 참고하면 되겠다.  
> [DNF_crawling_epic_log/data](https://github.com/Gauguin94/DNF_crawling_epic_log/tree/main/DNF_epic/data) <- click  
