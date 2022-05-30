# reinforce.py
```python
class reinForce:
    def __init__(self):
        self.time = whatTime()
```  
>   
> reinForce 클래스는 loadData, selectValue, arrangeBytime,  
> makeDict, timeResult, minuteResult, run 메소드로 구성되어 있다.  
>   
```python
    def run(self):
        rein_log = self.loadData()
        print("12->13강")
        reinforce_val = 12
        win, lose = self.selectValue(rein_log, reinforce_val)
        win_time, lose_time = self.arrangeBytime(win, lose)
        win_dict = self.makeDict(win_time)
        lose_dict = self.makeDict(lose_time)
        self.timeResult(win_dict, lose_dict, reinforce_val)
        win_minute, lose_minute = self.minuteResult(win_dict, lose_dict, reinforce_val)
```  
>   
> run 메소드에서 나머지 메소드들을 호출하도록 구성하였다.  
>   
```python
    def selectValue(self, rein_log, val):
        win = []
        lose = []
        trash = []
        for log in rein_log:
            if log['result'] == 'True' and int(log['before']) == val:
                win.append(log)
            elif log['result'] == 'False' and int(log['before']) == val:
                lose.append(log)
            else:
                trash.append(log)
        return win, lose
```
>   
> selectValue 메소드에서는 성공과 실패 로그 및 횟수를 나눠서 저장한다.  
>   
```python
    def arrangeBytime(self, win, lose):
        temp = []
        win_time = {}
        lose_time = {}
        for time in win:
            if time['date'][:2] not in win_time:
                win_time.setdefault(time['date'][:2], [])
            win_time[time['date'][:2]].append(int(time['date'][:2]+time['date'][-2:]))
        [win_time[hour].sort() for hour in win_time]
        win_time = sorted(win_time.items())

        for time in lose:
            if time['date'][:2] not in lose_time:
                lose_time.setdefault(time['date'][:2], [])
            lose_time[time['date'][:2]].append(int(time['date'][:2]+time['date'][-2:]))
        [lose_time[hour].sort() for hour in lose_time]
        lose_time = sorted(lose_time.items())
        return win_time, lose_time
```
>   
> arrangeBytime 메소드에서는 selectValue에서 초기화한 성공과 실패 리스트를 사용하여  
> 성공한 시간대, 실패한 시간대를 나눠 기록하는 작업을 수행한다.  
> 또한 시간대를 오름차순으로 정렬한다.  
