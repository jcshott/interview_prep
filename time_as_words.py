"""
phone screen question that Antonia got from Airbnb.

given time string (i.e. 1:12) - print it out in words to nearest tenth. i.e. "one ten"

"""
time_words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
15: "quarter", 20: "twenty", 25: "twenty-five", 30: "half", 0: "o'clock", 24:"midnight"}

def time_as_words(time_string):
    time_lst = time_string.split(":")
    hour = int(time_lst[0])
    am_pm = None
    midnight = False
    # if given am/pm at end, not military time
    if time_lst[-1][-2:] == "AM":
        am_pm = "AM"
    if time_lst[-1][-2:] == "PM":
        am_pm = "PM"
    if am_pm:
        minute = int(time_lst[1][:-2])
        if hour == 12 and am_pm == "AM":
            midnight = True
    # military time. convert
    else:
        minute = int(time_lst[1])
        if hour > 11:
            am_pm = "PM"
        else:
            am_pm = "AM"
        if hour == 00:
            midnight = True
        hour = hour % 12

    if minute % 5 != 0:
        # round minute up to nearest 5
        minute += (5-(minute % 5))

    # if minute is greater than 35, round hour up
    if minute >= 35:
        hour += 1
        if hour == 12 and am_pm == "PM":
            midnight = True

        minute = 60-minute

        if midnight:
            return time_words[minute] + " to midnight"
        else:
            if minute == 0:
                return time_words[hour] + " o'clock " + am_pm
            else:
                return time_words[minute] + " to " + time_words[hour] + " " + am_pm

    elif minute <= 25:
        if midnight:
            return time_words[minute] + " past midnight"
        else:
            if minute == 0:
                return time_words[hour] + " o'clock " + am_pm
            else:
                return time_words[minute] + " past " + time_words[hour] + " " + am_pm
    else:
        if midnight:
            return "half past midnight"
        else:
            return "half" + " past " + time_words[hour] + " o'clock " + am_pm


print time_as_words("11:52PM")
print time_as_words("10:57AM")
print time_as_words("3:13PM")

print time_as_words("12:13PM")
print time_as_words("3:45")
print time_as_words("12:22AM")
print time_as_words("3:00PM")
print time_as_words("14:27")
print time_as_words("00:22")
