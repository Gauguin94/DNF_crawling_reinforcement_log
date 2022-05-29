import os
from datetime import datetime

from sympy import maximum

path = '/home/kkn/DNF_rein/output/'

def whatTime():
    time = datetime.now()
    time = time.strftime("%y%m%d%H%M")
    date = time[:6]
    return date

class reinForce:
    def __init__(self):
        self.time = whatTime()

    def loadData(self):
        rein_log = []
        f = open(path+"rein_{}_log.txt".format('220423'), 'r')#.format(self.time), 'r')
        for line in f:
            rein_log.append({'before':line.split(" ")[0], 'result':line.split(" ")[1], 'date':line.split(" ")[3].replace('\n', "")})
        f.close()
        return rein_log

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

    def makeDict(self, data):
        time = []
        for i in range(24):
            if i < 10:
                time.append({'hour':'0{}'.format(i), 'time':[]})
            else:
                time.append({'hour':'{}'.format(i), 'time':[]})
        
        for i in data:
            for list in time:
                if list['hour'] == i[0]:
                    list['time'] = i[1]
        return time

    def timeResult(self, win_dict, lose_dict, val):
        error = 0
        for num, hour in enumerate(win_dict):
            error = 0
            try:
                percentage = (len(hour['time']) / (len(hour['time']) + len(lose_dict[num]['time'])))*100
            except:
                error += 1
            if error:
                print("{}시에서 {}->{} 성공은 {}번 vs 실패는 {}번.".format(hour['hour'], val, val+1,\
                    len(hour['time']), len(lose_dict[num]['time'])))
            else:
                print("{}시에서 {}->{} 성공은 {}번 vs 실패는 {}번. 성공 비율은 {:.3f}% ".format(hour['hour'], val, val+1,\
                    len(hour['time']), len(lose_dict[num]['time']), percentage))
        pass

    def minuteResult(self, win_dict, lose_dict, val):
        win_minute = []
        lose_minute = []
        for time in win_dict:
            count = {}
            for minute in time['time']:
                try:
                    count[minute] += 1
                except:
                    count[minute] = 1
            try:   
                max_val = max(count.values())
            except:
                max_val = 0
            for key, value in count.items():
                if value == max_val:
                    win_minute.append({key:value})
                    if value > 1:
                        if key < 10:
                            print("00시 0{}분 {}회의 가장 많은 {}->{}강화 성공을 거둔 시간".format(key, value, val, val+1))
                        elif key < 100:
                            print("00시 {}분 {}회의 가장 많은 {}->{}강화 성공을 거둔 시간".format(key, value, val, val+1))
                        elif key < 1000:
                            print("0{}시 {}분 {}회의 가장 많은 {}->{}강화 성공을 거둔 시간".format(str(key)[1], str(key)[-2:], value, val, val+1))
                        else:
                            print("{}시 {}분 {}회의 가장 많은 {}->{}강화 성공을 거둔 시간".format(str(key)[:2], str(key)[-2:], value, val, val+1))

        for time in lose_dict:
            count = {}
            for minute in time['time']:
                try:
                    count[minute] += 1
                except:
                    count[minute] = 1
            try:
                max_val = max(count.values())
            except:
                max_val = 0
            for key, value in count.items():
                if value == max_val:
                    lose_minute.append({key:value})
                    if value > 1:
                        if key < 10:
                            print("00시 0{}분 {}회의 가장 많은 {}->{}강화 실패를 겪은 시간".format(key, value, val, val+1))
                        elif key < 100:
                            print("00시 {}분 {}회의 가장 많은 {}->{}강화 실패를 겪은 시간".format(key, val, val+1, value))
                        elif key < 1000:
                            print("0{}시 {}분 {}회의 가장 많은 {}->{}강화 실패를 겪은 시간".format(str(key)[1], str(key)[-2:], value, val, val+1))
                        else:
                            print("{}시 {}분 {}회의 가장 많은 {}->{}강화 실패를 겪은 시간".format(str(key)[:2], str(key)[-2:], value, val, val+1))

        return win_minute, lose_minute

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

        print("13->14강")
        reinforce_val = 13
        win, lose = self.selectValue(rein_log, reinforce_val)
        win_time, lose_time = self.arrangeBytime(win, lose)
        win_dict = self.makeDict(win_time)
        lose_dict = self.makeDict(lose_time)
        self.timeResult(win_dict, lose_dict, reinforce_val)
        win_minute, lose_minute = self.minuteResult(win_dict, lose_dict, reinforce_val)

        print("14->15강")
        reinforce_val = 14
        win, lose = self.selectValue(rein_log, reinforce_val)
        win_time, lose_time = self.arrangeBytime(win, lose)
        win_dict = self.makeDict(win_time)
        lose_dict = self.makeDict(lose_time)
        self.timeResult(win_dict, lose_dict, reinforce_val)
        win_minute, lose_minute = self.minuteResult(win_dict, lose_dict, reinforce_val)

        print("15->16강")
        reinforce_val = 15
        win, lose = self.selectValue(rein_log, reinforce_val)
        win_time, lose_time = self.arrangeBytime(win, lose)
        win_dict = self.makeDict(win_time)
        lose_dict = self.makeDict(lose_time)
        self.timeResult(win_dict, lose_dict, reinforce_val)
        win_minute, lose_minute = self.minuteResult(win_dict, lose_dict, reinforce_val)

        print("16->17강")
        reinforce_val = 16
        win, lose = self.selectValue(rein_log, reinforce_val)
        win_time, lose_time = self.arrangeBytime(win, lose)
        win_dict = self.makeDict(win_time)
        lose_dict = self.makeDict(lose_time)
        self.timeResult(win_dict, lose_dict, reinforce_val)
        win_minute, lose_minute = self.minuteResult(win_dict, lose_dict, reinforce_val)

        print("17->18강")
        reinforce_val = 17
        win, lose = self.selectValue(rein_log, reinforce_val)
        win_time, lose_time = self.arrangeBytime(win, lose)
        win_dict = self.makeDict(win_time)
        lose_dict = self.makeDict(lose_time)
        self.timeResult(win_dict, lose_dict, reinforce_val)
        win_minute, lose_minute = self.minuteResult(win_dict, lose_dict, reinforce_val)

        return 0