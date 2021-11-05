# print(d.hour)
# print(d.ctiome()) #current time
# print(d)

import calendar #캘린더 모듈 사용
import datetime #date / time에 대한 모듈
d=datetime.datetime.now()
print(calendar.month(d.year, d.month))
