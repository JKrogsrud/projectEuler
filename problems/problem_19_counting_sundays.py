# Problem Source: https://projecteuler.net/problem=19

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def weekly_cycle():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    i = 0
    while True:
        yield days_of_week[i % 7]
        i += 1

day_gen = weekly_cycle()
setup = next(day_gen)

def month_cycle():
    months_of_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    i = 0
    while True:
        yield months_of_year[i % 12]
        i += 1

month_gen = month_cycle()
setup = next(month_gen)

# The date will be setup as follows: (day_of_week, date, month, year)
# So in english Monday, 1st of January, 1900 would be ('Monday', 1, 'January', 1900)

def is_leap_year(date):
    if date['year'] % 4 == 0:
        if date['year'] % 100 == 0:
            if date['year'] % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Takes in a date of form (day_of_week, date, month, year) and outputs the next day in same form
def next_day(day):
    next_day = {}
    next_day['day_of_week'] = next(day_gen)
    if day['month'] == 'January':
        # January has 31 days
        next_day['year'] = day['year']

        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)

        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'February':
        # February has 28 days except on leap years in which it has 29
        next_day['year'] = day['year']
        if is_leap_year(day):
            # case where we have 29 days
            if day['date'] == 29:
                next_day['date'] = 1
                next_day['month'] = next(month_gen)
            else:
                next_day['date'] = day['date'] + 1
                next_day['month'] = day['month']
        else:
            if day['date'] == 28:
                next_day['date'] = 1
                next_day['month'] = next(month_gen)
            else:
                next_day['date'] = day['date'] + 1
                next_day['month'] = day['month']

    if day['month'] == 'March':
        # March has 31 days
        next_day['year'] = day['year']
        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'April':
        # April has 30 days
        next_day['year'] = day['year']
        if day['date'] == 30:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'May':
        # May has 31 days
        next_day['year'] = day['year']
        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'June':
        # June has 30 days
        next_day['year'] = day['year']
        if day['date'] == 30:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'July':
        # July has 31 days
        next_day['year'] = day['year']
        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'August':
        # August has 31 days
        next_day['year'] = day['year']
        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'September':
        # September has 30 days
        next_day['year'] = day['year']
        if day['date'] == 30:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'October':
        # October has 31 days
        next_day['year'] = day['year']
        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'November':
        # November has 30 days
        next_day['year'] = day['year']
        if day['date'] == 30:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']

    if day['month'] == 'December':
        # December has 31 days
        if day['date'] == 31:
            next_day['date'] = 1
            next_day['month'] = next(month_gen)
            next_day['year'] = day['year'] + 1
        else:
            next_day['date'] = day['date'] + 1
            next_day['month'] = day['month']
            next_day['year'] = day['year']

    return next_day


def calendar_gen(start_date):
    while True:
        start_date = next_day(start_date)
        yield start_date


day = {'day_of_week': 'Monday', 'date' : 1, 'month': 'January', 'year': 1900}
calendar = calendar_gen(day)

count = 0
while 1900 <= day['year'] < 2001:
    if day['date'] == 1 and day['day_of_week'] == 'Sunday' and day['year'] > 1900:
        count += 1
    day = next(calendar)

print(count)