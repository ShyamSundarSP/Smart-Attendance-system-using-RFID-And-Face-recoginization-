import pywhatkit
import datetime
import time


phonenumber = ["+919943267833","+919943267833","+919943267833","+919943267833","+919943267833"]
for i in phonenumber:
    e = datetime.datetime.now()
    h= e.hour
    m = e.minute
    if m == 59:
        h = h+1
        n = 0
    else:
        n = m+1
    pywhatkit.sendwhatmsg(i,"hi",h,n)
    time.sleep(40)
    
