def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def no_of_days(month,year):
    if month in [9,4,11,6]:
        return 30
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else:
        if isLeap(year):
            return 29
        else:
            return 28

def first_day_of_next_month(year,month,first_day):
    week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    pos = 0
    for i in range(len(week_days)):
        #print(i)
        if first_day == week_days[i]:
            pos = i
            break
    week_days = week_days[pos:] + week_days[:pos]
    #print(week_days)
    days_ = {1: week_days[0], 2:week_days[1], 3:week_days[2], 4:week_days[3], 5:week_days[4], 6:week_days[5], 7:week_days[6]}
    #print(days_)
    days = no_of_days(month,year)
    first = 1 + days % 7
    return days_[first]

count = 0
first = 'Tuesday'
for i in range(1901,2001):
    for j in range(1,13):
        first = first_day_of_next_month(i,j,first)
        if first == 'Sunday':
            count += 1

print(count)


