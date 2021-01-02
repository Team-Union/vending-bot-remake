import discord
from discord.ext import commands, tasks
import random
import os
import sqlite3
from discord.utils import get

bot = commands.Bot(command_prefix="!자판기 ")
bot.remove_command('help')
conn = sqlite3.connect("self-introduce.db")
cur = conn.cursor()
g = "\""
c = 0
games = [
    "동방홍마향",
    "동방요요몽",
    "동방췌몽상",
    "동방영야초",
    "동방화영총",
    "동방풍신록",
    "동방비상천",
    "동방지령전",
    "동방성련선",
    "동방비상천칙",
    "동방신령묘",
    "동방심기루",
    "동방휘침성",
    "동방감주전",
    "동방천공장",
    "동방귀형수",
    "포켓몬스터 골드/실버",
    "포켓몬스터 하트골드/소울실버",
    "포켓몬스터 블랙/화이트2"
]


def is_table_created(table_name):
    if cur.execute(f'SELECT COUNT(*) FROM sqlite_master WHERE type="table" AND name={table_name}').fetchall() != [(0,)]:
        return True
    else:
        return False


@tasks.loop(seconds=15)
async def change_presence():
    await bot.change_presence(activity=discord.activity.Game(name=games[random.randint(0, len(games) - 1)]))


@bot.event
async def on_ready():
    print(f"Name={bot.user.name}, ID={bot.user.id}")
    for i in bot.guilds:
        try:
            for j in await i.invites():
                print(f"{i.name} - {j}")
        except:
            pass
    change_presence.start()


@bot.command()
async def 상품보기(ctx):
    if True:
        if is_table_created(ctx.guild.id):
            if cur.execute(f'SELECT COUNT(*) FROM {ctx.guild.id}').fetchall() != [(0,)]:
                v = cur.execute(f'SELECT * FROM {ctx.guild.id}').fetchall()
                e = discord.Embed(
                    title=f"상품보기 - 성공",
                    description="",
                    color=65535
                )
                ids = []
                names = []
                stocks = []
                prices = []
                for i in v:
                    ids.append(i[0])
                    prices.append(i[2])
                    stocks.append(i[3])
                    names.append(i[1])
                e.add_field(name="번호", value="\n".join(ids))
                e.add_field(name="이름", value="\n".join(names))
                e.add_field(name="가격", value="\n".join(prices))
                e.add_field(name="재고", value="\n".join(stocks))
                await ctx.send(embed=e)
            else:
                e = discord.Embed(
                    title=f"상품보기 - 성공",
                    description="물건이 아무것도 없습니다.",
                    color=65535
                )
                await ctx.send(embed=e)
        else:
            cur.execute(f'CREATE TABLE {ctx.guild.id} (id integer, name text, price integer, stock integer)')
            e = discord.Embed(
                title=f"상품보기 - 성공",
                description="물건이 아무것도 없습니다.",
                color=65535
            )
            await ctx.send(embed=e)


@bot.command()
@commands.has_permissions(administrator=True)
async def 상품생성(ctx, name, price, stock):
    if not isinstance(int, price):
        e = discord.Embed(
            title=f"상품생성 - 실패",
            description="가격이 올바르지 않습니다. (숫자만 있어야 합니다.)",
            color=16711680
        )
        await ctx.send(embed=e)
    elif not isinstance(int, stock):
        e = discord.Embed(
            title=f"상품생성 - 실패",
            description="재고가 올바르지 않습니다. (숫자만 있어야 합니다.)",
            color=16711680
        )
        await ctx.send(embed=e)
    else:
        cur.execute(f'INSERT INTO {ctx.guild.id} VALUES ({random.randint(0,99999)}, {name}, {price}, {stock})')
        e = discord.Embed(
            title=f"상품생성 - 성공",
            description="새로운 상품이 추가되었습니다.",
            color=65535
        )
        await ctx.send(embed=e)


@bot.command(aliases=["help", "명령어", "도움말"])
async def 도움(ctx):
    e = discord.Embed(
        title=f"도움말",
        description="""
        상품보기 - 서버에 있는 모든 상품을 봅니다
        상품생성 - 상품을 등록합니다
        
        원래 있던 다른 명령어들은 SQL 상에서
        구현의 난해함으로 현재 지원하지 않으며
        구현체를 DM으로 보내주시면 적용됩니다
        """,
        color=65535
    )
    e.set_footer(text="Vending Bot/Refine v1.0.0a")
    await ctx.send(embed=e)


@bot.after_invoke
async def invoked(ctx):
    conn.commit()


bot.run(os.environ["token"])
