from datetime import datetime 

a = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
f= open("/Users/shashwataryal/Documents/GIT/Short/log.txt","a")
f.write((a + '\n'))