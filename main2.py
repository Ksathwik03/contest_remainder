import datetime
import discord
from pytz import timezone


def upcoming(data, zone):
    pages = []
    j = 0
    description = ""
    for i in data:
        start_time = i['start']
        start_time = start_time.replace('T', ' ')
        FMT = '%Y-%m-%d %H:%M:%S'
        time = datetime.datetime.strptime(start_time, FMT)
        t = time.replace(tzinfo=datetime.timezone.utc).astimezone(timezone(zone))
        event = i['event']
        resource = i['resource']
        url = i['href']
        resource = resource[0:len(resource) - 4].upper()
        description += f'{resource}: {event}\n Starts at {t} \n Url: {url} \n'
        j = j + 1
        if j % 4 == 0:
            description += f'Page no. {j / 4}'
            embed = discord.Embed(
                title="UPCOMING CONTEST",
                description=description,
                color=discord.Colour.red()
            )
            pages.append(embed)
            description = ""
    if j % 4 != 0:
        description += f'Page no. {j / 4}'
        embed = discord.Embed(
            title="UPCOMING CONTEST",
            description=description,
            color=discord.Colour.red()
        )
        pages.append(embed)
    return pages


def help_description():
    description = 'This bot bot reminds you 30 minutes before the contest \n' \
                  'LIST OF COMMANDS \n ' \
                  '1)%upcoming  shows all the upcoming contests of the subscribed websites \n' \
                  '2)%cur_website shows all your subscribed websites \n' \
                  'Note - there are some default websites already subscribed for you check them out \n' \
                  '3)%add_website <url of website> - subscribes to this website \n' \
                  'Example - %add_website codeforces.com \n adds codeforces to your subscribed websites\n' \
                  '4)%del_website <url of website> - Deletes subscription of this website \n' \
                  'Example - %del_website codeforces.com \n deletes codeforces from your subscribed websites \n' \
                  '5)%supported_website - Shows all the supported websites \n' \
                  '6)%set_timezone <Your time zone> recieve updates in your time zone \n' \
                  'Example %set_timezone Europe/Berlin sets your time zone to Berlin \n'
    return description


def hello(a):
    s = ''
    for i in a:
        x = i['relativeTimeSeconds']
        x = -x
        y = i['name']
        if datetime.datetime.now() < x <= datetime.datetime.now() + datetime.timedelta(12):
            s = f'{y}: starts in {x // (3600 * 24)} days {(x % (3600 * 24) // 3600)} hrs \n' + s
    if s == '':
        s = 'No contest in the upcoming 3 days'
    return s


time_store = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}


def validate(time):
    if len(time) < 2:
        return -1
    time_num = time[0:len(time) - 1]
    time_str = time[len(time) - 1]
    check = list(filter(lambda i: i == time_str, time_store))
    if len(check) and time_num.isnumeric():
        return int(time_num) * time_store[check[0]]
    print(check)
    return -1
