import time

time.sleep(10)

rfile = open("date.txt", "r")
line = rfile.readlines()

if len(line[0]) > 0:
    date = line[0].split("/")
    #print(date)
    month = int(date[0])
    day = int(date[1])
    sign = ""
    if month == 1:
        if day < 20:
            sign = "capricorn"
        else:
            sign = "aquarius"
    elif month == 2:
        if day < 19:
            sign = "aquarius"
        else:
            sign = "pisces"
    elif month == 3:
        if day < 21:
            sign = "pisces"
        else:
            sign = "aries"
    elif month == 4:
        if day < 20:
            sign = "aries"
        else:
            sign = "taurus"
    elif month == 5:
        if day < 22:
            sign = "taurus"
        else:
            sign = "gemini"
    elif month == 6:
        if day < 21:
            sign = "gemini"
        else:
            sign = "cancer"
    elif month == 7:
        if day < 23:
            sign = "cancer"
        else:
            sign = "leo"
    elif month == 8:
        if day < 23:
            sign = "leo"
        else:
            sign = "virgo"
    elif month == 9:
        if day < 23:
            sign = "virgo"
        else:
            sign = "libra"
    elif month == 10:
        if day < 23:
            sign = "libra"
        else:
            sign = "scorpio"
    elif month == 11:
        if day < 22:
            sign = "scorpio"
        else:
            sign = "sagittarius"
    elif month == 12:
        if day < 22:
            sign = "sagittarius"
        else:
            sign = "capricorn"
    print(sign)

else:
    print("nothing in file")

rfile.close()

wfile = open("sign.txt", "w")
wfile.write(sign)
wfile.close()
