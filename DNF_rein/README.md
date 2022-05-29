# run.py

> 우리는 최대한 많은 모험단을 찾아 로그를 수집해야 한다.  
```python
LETTER = [
    'SaeronHolic', '%ec%a0%84%eb%87%8c%ec%86%8c%eb%85%80%eb%8b%a8', 'loveintheice', '%eb%8f%84%ec%9c%a0TV', '%ea%b0%a4%eb%9f%ad%ec%8b%9cNote',\
    'NOHOLD', '%ea%b3%b5%ea%b0%90%ec%98%81%ec%96%b4', '%eb%aa%a8%eb%8b%88%ec%b9%b4%ed%95%9c%ec%83%81%ec%9e%90', '%ec%ac%b4',\
    '%eb%9d%b5%eb%b0%9c%ec%82%ac%ec%83%9d%ed%8c%ac6%ed%98%b8', '%eb%8b%b9%ea%b7%bc%eb%8b%b9%ea%b7%bc', '%ed%8f%ac%eb%8f%84%ec%a6%99%eb%86%8d%ec%9e%a5',\
    '%ec%9e%90%eb%b0%a9%ec%9d%b4%eb%84%a4', '%ec%b9%b8%ec%a1%b0%ec%bf%a0', '%eb%aa%a8%ec%82%b4%eb%8c%80', '%ec%a7%80%ed%99%98%ec%a7%b1',\
    '%eb%aa%85%ec%98%88%ed%9b%88%ec%9e%a5%ec%9e%84%eb%8b%a4', '%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8%ec%82%bc%ec%8b%9d', 'collet',\
    '%ec%a7%b1%ec%9d%b5%ec%a0%84%ec%9a%a9%ea%b2%8c%ec%9e%84', '%ec%9a%94%ea%b8%b0%eb%b2%a0%eb%9d%bc', '%ea%b7%b8%ec%9d%b8%ed%8c%8c'
]
# saeronholic, 전뇌소녀단, loveintheice, 도유TV, 갤럭시Note
# 공감영어, 모니카한상자, 쬴
# 띵발사생팬6호, 당근당근, 포도즙농장
# 자방이네, 칸조쿠, 모살대, 지환짱
# 명예훈장임다, 에이전트삼식, collet
# 짱익전용게임, 요기베라, 그인파
```  
> 던파모아에서 캐릭터 강화 부분에서 상위권에 위치해 있는 캐릭터들의  
> 모험단 계정을 LETTER라는 리스트로 선언하였다.   
> 각 모험단 이름들은 URL 인코딩을 사용하여 변환하였다.  
> [URL 인코딩 변환 사이트](https://www.convertstring.com/ko/EncodeDecode/UrlEncode) <- click  
> 또한 최대한 많은 자료를 수집하고자 본 Github에서 고유 에픽 확률을 확인해보기 위해  
> 저장했던 모험단들 또한 활용하였다. [WARP](https://github.com/Gauguin94/DNF_crawling_epic_log) <- click  
# 대략적인 흐름  
> **세부적인 것은 글 마지막에 존재하는 링크들로 들어가면 확인 가능.**  
```python
SEARCH_URL = 'https://dunfamoa.com/characters/adventure?search='

if __name__ == "__main__":
    for num, letter in enumerate(LETTER):
        dunfaMoa(SEARCH_URL + letter, num + 137).run()
```  
>  
> 먼저, 앞서 만들었던 리스트 내 단어들로 dunfamoa 홈페이지에서 검색을 실시한다.  
> 모험단 검색을 통해, 모험단 내 계정 캐릭터의 이름들을 전부 가져온다.    
>  
```python
    do = filtering()
    do.run()
```  
>   
> 목표는 13강 이상을 성공한 사람들의 로그를 얻는 것이기 때문에 13강을 성공해보지 못하신 분들,  
> 그리고 레어 등급 이하의 아이템이나 불사조 유니크 무기와 같은,  
> 재미삼아 강화해본 무기 혹은 실질적으로 사용하지 않는 무기의 성공은 제외시켰다.     
>   
```python
    char_list = preprocessData().run()
```  
>   
> 혹시나 겹치는 캐릭터가 있을 수 있기 때문에 한 번 걸러준다.  
> (preprocess는 아니지만, 작성 당시 떠오르는 이름이 없어서...)  
>   
```python
    getLog(char_list).run()
```  
>   
> 저장한 캐릭터들의 로그를 NEOPLE Open API 서버에 요청한다.  
>   
```python
    extract_func = extractEpic()
    epic = extract_func.run()
```  
>   
> 반환받은 로그들 중 강화 로그만을 가져온다.  
> 또한 다루기 쉽도록 내가 원하는 형태의 데이터로 가공한다.  
>    
```python
    rein = reinForce().run()
```  
>   
> 시간대별 13강화 이상 성공 비율을 확인하는 작업.  
> 통계적인 방법을 사용하지 않아 의미없을 수 있는 기록이지만  
> 13강 도전을 33번 실패한 친구에게는 유용할 수도 있을 것 같다...    
>   
# 결과
![성공비율](https://user-images.githubusercontent.com/98927470/170871890-f0d877fa-4947-4e76-9a1e-29c5083f4862.jpg) 
>   
> 위 그림은 결과의 일부를 캡쳐한 것이다.  
>   
# Go to directory  
  
> **1. Dunfamoa 크롤링**  
> 크롤링 과정은 고유 에픽 크롤링 과정과 동일하게 이루어진다.  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/crawling) <- click  
>   
> **2. 데이터 관련 사전 작업**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/data) <- click  
>   
> **3. NEOPLE 오픈 API 호출**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/getAPI) <- click  
>   
> **4. 재미로 해본 근본없는 분석?**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/analyze) <- click  
