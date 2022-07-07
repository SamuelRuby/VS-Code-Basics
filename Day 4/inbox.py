import imaplib
import email

import configparser
config = configparser.ConfigParser()
config.read('/Users/ruby/Desktop/VS-Code-Basics/credentials.ini') #PATH TO MY config file on my local device

cred = config["GMAIL"]
username = cred["USERNAME"]
password = cred["PASSWORD"]

#print(username)
#print (password)


#declaring varaiables
host = 'imap.gmail.com' 

def get_inbox ():
    mail = imaplib.IMAP4_SSL(host)
    mail.login (username, password)
    mail.select ('inbox')
    _, search_data = mail.search (None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split ():
        email_data = {}
        _, data = mail.fetch (num, '(RFC822)')
    #print(data)
        _,b = data[0]
        email_message = email. message_from_bytes(b)
    
        for header in ['subject', 'to', 'from', 'date']:
            print ('{}: {}'. format(header, email_message[header]))
            email_data[header] = email_message [header]
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload (decode = True)
                email_data ['body'] = body.decode ()
            elif part.get_content_type() == 'text/html':
                html_body = part.get_payload (decode = True)
                email_data['html_body'] = html_body.decode()
        my_message.append (email_data)
    return my_message

if __name__ == "__main__":
    my_inbox = get_inbox()
    print (my_inbox)
#print (search_data[0].split())
#https://accounts.google.com/b/0/DisplayUnlockCaptcha
#allow less secure app access in google account permissions under security settings