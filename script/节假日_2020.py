import calendar
import datetime,time
import chinese_holiday

date_input1 = '2019-01-01'
date_input2 = '2020-12-31'
timelist1 = date_input1.split("-")
timelist1 = [int(x) for x in timelist1]
year1 = timelist1[0]
month1 = timelist1[1]
day1 = timelist1[2]
begin = datetime.date(year1, month1, day1)
#print(begin)
timelist2 = date_input2.split("-")
timelist2 = [int(x) for x in timelist2]
year2 = timelist2[0]
month2 = timelist2[1]
day2 = timelist2[2]
end = datetime.date(year2, month2, day2)
#print(end)

for i in range((end - begin).days + 1):
    day = begin + datetime.timedelta(days=i)
    dt = str(day)
    if chinese_holiday.is_holiday(dt):
        print(dt)
#    a = int(dt[5:7])
#    b = int(dt[8:10])
#    calen1 = calendar.weekday(2020, a, b)
#    if calen1 == 5 or calen1 == 6:
#        print(dt)