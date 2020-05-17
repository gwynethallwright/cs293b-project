# This script is designed to run at the edge-device
# Based on classifier output, alert user via email of human activity

# version 1: Uses gmail's smtp server, requires enabling less secure apps
# https://myaccount.google.com/lesssecureapps

# todo: implement Oauth, https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html

import smtplib

myEmail = input("Enter your email: ")
myEmailPass = input("Enter your email password: ") 
destEmail = input ("Enter the email you would like to send message to: ")

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()

#log in to the server using user provided credentials
server.login(myEmail, myEmailPass)

#Send the mail
subject = "Human detected"
body = "The device has detected human activity."
message = ("From: %s\r\n" % myEmail
             + "To: %s\r\n" % destEmail
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)
server.sendmail(myEmail, destEmail, message)

server.close()