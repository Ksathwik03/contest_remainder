import asyncio
import discord
import requests
from discord.ext import commands
import Time
import hello
import pymongo
import Data_base

client = commands.Bot(command_prefix='!')

text_channel_list = []
upcoming_data = []
supported_data = ['codeforces.com',
                  'codechef.com',
                  'atcoder.jp',
                  'hackerearth.com',
                  'codingcompetitions.withgoogle.com']
db = Data_base.data_base()
Remainder_data = list(db.find({}))


async def check(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            global text_channel_list
            text_channel_list.append(channel)
            return channel


def print_website(temp):
    s = ''
    for website in temp:
        s += f'{website}\n'
    embed = discord.Embed(
        title=' Your Subscribed websites',
        description=s,
        color=discord.Colour.red()
    )
    return embed


async def print_statement(s):
    embed = discord.Embed(
        title='Remainder',
        description=s,
        color=discord.Colour.red()
    )
    for i in text_channel_list:
        await i.send(embed=embed)


async def channel_list():
    global db
    for guild in client.guilds:
        global Remainder_data, supported_data
        if len(list(db.find({'id': guild.id}))) == 0:
            channel = await check(guild)
            Remainder_data.append(
                {'id': guild.id, 'websites': supported_data, 'remainder': 600, 'channel': channel.id})
            db.insert_one({'id': guild.id, 'websites': supported_data, 'remainder': 600, 'channel': channel.id})


async def contest_reminder():
    while True:
        r = requests.get(f'https://codeforces.com/api/contest.list')
        p = r.json()
        s = hello.reminder(p['result'])
        if s != -1:
            await print_statement(s)
        await asyncio.sleep(60)


async def fetch():
    while True:
        data = requests.get(f'https://clist.by:443/api/v2/contest/?limit=20&start__gte={Time.time_url()}&order_by=start&username=Ksathwik03&api_key=ed6d08ae4f389746f053fb34351419e52d087227')
        global upcoming_data
        upcoming_data = data.json()
        await asyncio.sleep(180)


@client.event
async def on_ready():
    print("Bot is ready")
    await channel_list()
    await fetch()
    await contest_reminder()


@client.command()
async def upcoming(ctx):
    global upcoming_data, Remainder_data
    temp = list(filter(lambda x: x['id'] == ctx.guild.id, Remainder_data))
    temp = list(filter(lambda x: temp[0]['websites'].count(x['resource']) >= 1, upcoming_data['objects']))
    s = hello.upcoming(temp)
    embed = discord.Embed(
        title=' Upcoming contests',
        description=s,
        color=discord.Colour.red()
    )
    await ctx.send(embed=embed)


@client.command()
async def cur_website(ctx):
    temp = list(filter(lambda x: x['id'] == ctx.guild.id, Remainder_data))
    await ctx.send(embed=print_website(temp[0]['websites']))


@client.command()
async def add_website(ctx, arg):
    temp = list(filter(lambda x: x['id'] == ctx.guild.id, Remainder_data))
    if temp[0]['websites'].count(arg):
        await ctx.send(embed=print_website(temp[0]['websites']))
        return
    temp[0]['websites'].append(arg)
    global db
    db.update_one({'id': ctx.guild.id}, {'$set': {'websites': temp[0]['websites']}})
    await ctx.send(embed=print_website(temp[0]['websites']))


@client.command()
async def delete_website(ctx, arg):
    temp = list(filter(lambda x: x['id'] == ctx.guild.id, Remainder_data))
    if temp[0]['websites'].count(arg):
        temp[0]['websites'].remove(arg)
    await ctx.send(embed=print_website(temp[0]['websites']))


client.run("ODYwNzc5NjY5Mjg4Nzc5Nzc2.YOANiQ.Y9wBmDSdnvOJW3FFyANMAr5X-eg")
