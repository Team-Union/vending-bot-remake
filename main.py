import discord
from discord.ext import commands, tasks
import random
import os
from pymongo import MongoClient
from discord.utils import get

bot = commands.Bot(command_prefix="!자판기 ")
bot.remove_command('help')
g = "\""
c = 0
games = [
    "동방영이전",
    "동방봉마록",
    "동방몽시공",
    "동방환상향",
    "동방괴기담",
    "동방홍마향",
    "동방요요몽",
    "동방췌몽상",
    "동방영야초",
    "동방화영총",
    "동방문화첩",
    "동방풍신록",
    "동방비상천",
    "동방지령전",
    "동방성련선",
    "동방비상천칙",
    "더블 스포일러 ~ 동방문화첩",
    "요정대전쟁 ~ 동방삼월정",
    "동방신령묘",
    "동방심기루",
    "동방휘침성",
    "탄막 아마노자쿠",
    "동방심비록",
    "동방감주전",
    "동방빙의화",
    "동방천공장",
    "비봉 나이트메어 다이어리",
    "동방귀형수",
    "동방강욕이문 체험판",
    "포켓몬스터 금/은",
    "포켓몬스터 하트골드/소울실버",
    "포켓몬스터 블랙2/화이트2"
]


bot.run(os.environ["token"])
