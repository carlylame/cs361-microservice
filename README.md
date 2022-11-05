# cs361-microservice
microservice for Nina's project!

- How to REQUEST data: To request data, a date is written to a text file in the main program (date.txt). A sample call would be: 
rfile = open("date.txt", "r")
line = rfile.readlines()

- How to RECEIVE data: To recieve data, the microservice writes to a text file (sign.txt). A sample call would be:
wfile = open("sign.txt", "w")
wfile.write(sign)

- UML sequence diagram:
<img width="425" alt="Screen Shot 2022-11-04 at 11 04 42 PM" src="https://user-images.githubusercontent.com/91341249/200105121-cf9aedc0-8d2d-4454-9d2e-e69fb934aaf7.png">
