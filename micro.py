import time

while True:
    time.sleep(1.0)

    rfile = open("date.txt", "r")
    line = rfile.readlines()

    if len(line) > 0:
        date = line[0].split("/")
        #print(date)
        month = int(date[0])
        day = int(date[1])
        sign = ""
        if month == 1:
            if day < 20:
                sign = "Capricorn"
            else:
                sign = "Aquarius"
        elif month == 2:
            if day < 19:
                sign = "Aquarius"
            else:
                sign = "Pisces"
        elif month == 3:
            if day < 21:
                sign = "Pisces"
            else:
                sign = "Aries"
        elif month == 4:
            if day < 20:
                sign = "Aries"
            else:
                sign = "Taurus"
        elif month == 5:
            if day < 22:
                sign = "Taurus"
            else:
                sign = "Gemini"
        elif month == 6:
            if day < 21:
                sign = "Gemini"
            else:
                sign = "Cancer"
        elif month == 7:
            if day < 23:
                sign = "Cancer"
            else:
                sign = "Leo"
        elif month == 8:
            if day < 23:
                sign = "Leo"
            else:
                sign = "Virgo"
        elif month == 9:
            if day < 23:
                sign = "Virgo"
            else:
                sign = "Libra"
        elif month == 10:
            if day < 23:
                sign = "Libra"
            else:
                sign = "Scorpio"
        elif month == 11:
            if day < 22:
                sign = "Scorpio"
            else:
                sign = "Sagittarius"
        elif month == 12:
            if day < 22:
                sign = "Sagittarius"
            else:
                sign = "Capricorn"
        print(sign)

        wfile = open("sign.txt", "w")
        wfile.write(sign)
        wfile.close()

    else:
        print("nothing in file")

    rfile.close()
