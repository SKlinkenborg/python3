from datetime import datetime
# https://docs.python.org/3/library/datetime.html#module-datetime
# assign a datetime object (year, month, day, hour 0-23, minute, second) to the variable birthday
birthday = datetime(1988, 6, 19, 0, 45, 36)

# birthday values
print(birthday.year)
print(birthday.month)
# etc etc

# built-in functions
print(birthday.weekday())
# 6 (Sunday. Monday = 0)

datetime.now()
# datetime.datetime(2025, 3, 26, 8, 35, 0, 768351)

# determine delta between 2 dates. Only works with subtraction. No other arithmetic.
datetime(2018, 1, 1) - datetime(2017, 1, 1)
# datetime.timedelta(days=365)
datetime.now() - birthday
datetime.timedelta(days=13429, seconds=28296, microseconds=316616)

# strptime parse datetime from string
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
parsed_date = datetime.strptime('Jan 6, 2021', '%b  %d, %Y' )
parsed_date.month
# 1
parsed_date - birthday
# datetime.timedelta(days=11888, seconds=83664)

# strftime extract value from datetime object as string in specified format
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
# March 26, 2025
