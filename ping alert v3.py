#!/usr/bin/env python

import openpyxl
import statistics as stats
import os
import smtplib
import time

def sendalert(msg):

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()

    smtpObj.starttls()
    smtpObj.login(FROM, PSWD)

    smtpObj.sendmail(FROM,TO,msg)
    smtpObj.quit()

# enter full path for site.xlsx file before site.xlsx
book = openpyxl.load_workbook('site.xlsx', data_only=True)

sheet = book.active

rows = sheet.rows

values = []

for row in rows:
    for cell in row:
        values.append(cell.value)

# add full path for userpass.txt file before userpass.txt (this email and password for smtp server)
with open('userpass.txt') as f:
    lines = [line.rstrip() for line in f]

FROM = lines[0]
PSWD = lines[1]
# Replace EMAIL with email will get message when site down
TO = 'EMAIL'
SUB = 'Subject: Alert webserver is Down \n'
header = 'To:' + TO + '\n' + 'From: ' + FROM + '\n' + SUB
body = """Your site is DOWN. \n"""

#print(values)
for ip in values:
      #command ping for linux and unix
      response = os.system('ping -c 1 ' + str(ip))
      #command ping for windows
      #response = os.system('ping -n 1 ' + str(ip))
      if response == 0:
        print (ip, ' is up')
      else:
        message = header + body + ip
        sendalert(message)
      #time.sleep(5)


#if __name__ == '__main__':
#    sendalert(message)
