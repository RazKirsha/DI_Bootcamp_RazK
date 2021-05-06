import datetime
import time
now = datetime.datetime.now()
print(now)
# print(dir(now))
print(f'current hour: {now.hour}, current minutes: {now.minute}')

# adds 40 minutes to current time
print(now + datetime.timedelta(minutes=40))
print(now + datetime.timedelta(days=40))

# setting a timer in seconds (5 seconds)
# time.sleep(5)
# nowafter5 = datetime.datetime.now()
# print(nowafter5 - now)
# print(type(nowafter5 - now))
# if nowafter5 > now:
#     print('im time after 5')
#
# today = datetime.datetime.today()
# print(today)

users_birthday = input('DD/MM/YYY: ')
birthday = datetime.datetime.strptime(users_birthday, "%-d/%-m/%Y")
delta = datetime.datetime.now() - birthday
print(delta.days/365)

