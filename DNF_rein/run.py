import os
import sys
from analyze import*
from crawling import*
from data import*
from getAPI import*

SEARCH_URL = 'https://dunfamoa.com/characters/adventure?search='

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

if __name__ == "__main__":
    for num, letter in enumerate(LETTER):
        dunfaMoa(SEARCH_URL + letter, num + 137).run()
    do = filtering()
    do.run()
    char_list = preprocessData().run()
    getLog().run()
    rein = reinForce().run()