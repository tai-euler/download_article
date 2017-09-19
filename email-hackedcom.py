
import os
import time
import smtplib
import time
import random

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "sender_email@gmail.com"
toaddr =   [
        'recipient1@gmail.com',
        'recipient2@gmail.com',
]


msg = MIMEMultipart()

msg['From'] = fromaddr
#localtime = time.asctime( time.localtime(time.time()) )
localtime = time.strftime('%x')
msg['Subject'] = localtime
#msg['Subject'] = localtime + "your fresh articles"
body = "\nWith kind regards \n\n your_bot:)\n\n"
msg.attach(MIMEText(body, 'plain'))

#--------------------------------------------------
# save names in a array --> nameList[]
# we count the numbers --> count
count = 0
nameList = []
path = '/Users/tai-euler/Desktop/article-scraper/articles'
skip = False
for filenamee in os.listdir(path):
    if filenamee:
        # it ignores the .DS_Store file on MAC
              if ".DS_Store" not in filenamee:
                    nameList.append(filenamee) #you save their names in a array
                    count = len(nameList) #you save the number 

#--------------------------------------------------

# converting to base64 before sending
for names in nameList:

    filename = names
    attachment = open("/Users/tai-euler/Desktop/article-scraper/articles" + filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

#--------------------------------------------------
#iterate through toaddr array and send everybody the email and between sleep for random time
number = 0
for addres in toaddr :

        msg['To'] = addres
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "YOUR_PASSWORD_FOR_sender_email@gmail.com")
        text = msg.as_string()
        server.sendmail(fromaddr, addres, text)
        server.quit()
        del msg['To']
        number = random.randint(1,10)
        time.sleep( number )
