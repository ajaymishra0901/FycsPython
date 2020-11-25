#!/usr/bin/python3

import smtplib
import getpass

content='hello,sending mail from python code'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()

passwd=getpass.getpass()

mail.login('nivethakutty32@gmail.com',passwd)
mail.sendmail('nivethakutty32@gmail.com','snehashanagoni05potti@gmail.com', content)

mail.close()
