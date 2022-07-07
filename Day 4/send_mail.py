from pickle import NONE
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#declaring varaiables
import configparser
config = configparser.ConfigParser()
config.read('/Users/ruby/Desktop/VS-Code-Basics/credentials.ini') #PATH TO MY config file on my local device

cred = config["GMAIL"]
username = cred["USERNAME"]
password = cred["PASSWORD"]

#print(username)
#print (password)


msg = MIMEMultipart ('alternative')
from_email = 'workwithruby <workwithrubyy@gmail.com>'
to_emails = 'youreajockey@gmail.com'
html = []

def send_mail(text= 'Email body', subject = 'Hello world', from_email = 'workwithruby <workwithrubyy@gmail.com>', to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart ('alternative')
    msg['From'] = from_email
    msg['To'] = ','.join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach (txt_part)
    
    if html != None:
        html_part = MIMEText (html, 'html'),
        msg.attach (html_part)

msg_str = ''
#login to my smtp server
server = smtplib.SMTP (host ='smtp.gmail.com', port = 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(from_email, to_emails, msg_str)
server.quit()

#with smtplib-SMTP()as server:
#server.login()
#pass