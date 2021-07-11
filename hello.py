import requests
import datetime
import Time

def upcoming(a):
    s = ''
    for i in a:
        start = i['start']
        event = i['event']
        resource = i['resource']
        resource = resource[0:len(resource)-4].upper()
        start = Time.local(start)
        s += f'{resource}: {event} Starts at {start} \n'
    return s


def reminder(a):
    s = ''
    for i in a:
        x = i['relativeTimeSeconds']
        x = -x
        y = i['name']
        if 9 * 60 <= x < 10 * 60:
            s = f'{y}: starts in 10 minutes \n' + s
    if s == '':
        return -1
    return s


def hello(a):
    s = ''
    for i in a:
        x = i['relativeTimeSeconds']
        x = -x
        y = i['name']
        if datetime.datetime.now() < x <= datetime.datetime.now()+ datetime.timedelta(12):
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


def hi():
    r = requests.get(
        'https://clist.by:443/api/v2/contest/?username=Ksathwik03&api_key=ed6d08ae4f389746f053fb34351419e52d087227')
    q = r.json()
    print(q)


# hi()


# a = [0, 1, 2]
#print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=a[0], hours=a[1], minutes=a[2]))
