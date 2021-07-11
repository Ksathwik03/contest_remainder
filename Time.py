import datetime
from time import strftime, gmtime,localtime
import pytz


def time_url():
    time = strftime('%Y-%m-%d %H:%M:%S', gmtime())
    # time = str(datetime.datetime.now())
    # time = time[0:19]
    time = time.replace(' ', 'T')
    time = time.replace(':', '%3A')
    return time


# def Local():
#     start = '2021-07-06T18%3A32%3A45'
#     start = start.replace('T', ' ')
#     timestamp = start.replace(tzinfo=timezone.utc).timestamp()
#     print(timestamp)


# a = [{'id': 213, 'name': 'as', 'con': ['z', 'a']}, {'id': 223, 'name': 'as', 'con': ['we', 'bcd']}]
# a = sorted(a, key=lambda k: k['con'])
# #print(a)
# a = list(filter(lambda x: x['id'] == 213, a))
# a = a.find({id: 213})
# print(a)
# now = datetime.datetime.now()
# local_now = now.astimezone()
# # local_tz = local_now.tznfo
# # local_tzname = local_tz.tzname(locail_now)
# local_now = datetime.datetime.now() - datetime.timedelta(hours=5, minutes=30)
# local_now.__format__('s')
# print(local_now)
# mongoose.connect('mongodb+srv://Ksathwik03:Ksathwik03@cluster0.xtzux.mongodb.net/Happy?retryWrites=true&w=majority', { useNewUrlParser: true, useUnifiedTopology: true }, () => { console.log('database loaded') });
# db = pymongo.MongoClient('mongodb+srv://Ksathwik03:Ksathwik03@cluster0.xtzux.mongodb.net/Happy?retryWrites=true&w=majority')
# db = db["Happy"]
# db = db["happies"]
# for i in db:
#     print(i)


#
# client = pymongo.MongoClient("mongodb+srv://Ksathwik03:Ksathwik03@cluster0.xtzux.mongodb.net/Python?retryWrites=true&w=majority")
# db = client['Python']
# db = db['Ksathwik03']
# a = db.find({})
# for i in a:
#     print(i)
# print(Local())

# tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
# print(tz)
# local_time = datetime.datetime(2010, 4, 27, 12, 0, 0, 0, tzinfo=pytz.timezone(str(tz)))
# print(local_time)

from datetime import timedelta

s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'
timedelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
