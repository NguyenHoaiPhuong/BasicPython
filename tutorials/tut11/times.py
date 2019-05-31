import time
import calendar

def tick():
    print('Time intervals are floating-point numbers in units of seconds.\
         Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).')
    ticks = time.time()
    print('Number of ticks since 12:00am, January 1, 1970: ', ticks)

def time_tuple():
    print("Many of Python's time functions handle time as a tuple of 9 numbers:")
    print("4-digit year: 2018")
    print("Month: 1 to 12")
    print("Day: 1 to 31")
    print("Hour: 0 to 23")
    print("Minute: 0 to 59")
    print("Second: 0 to 61 (60 or 61 are leap-seconds)")
    print("Day of Week: 0 to 6 (0 is Monday)")
    print("Day of year: 1 to 366 (Julian day)")
    print("Daylight savings: -1, 0, 1, -1 means library determines DST")

    localtime = time.localtime(time.time())
    print("Local current time :", localtime)

def time_format():
    localtime = time.asctime(time.localtime(time.time()))
    res = 'Local current time : ' + localtime
    print(res)

def get_calandar():
    cal = calendar.month(2019, 6)
    print(cal)
