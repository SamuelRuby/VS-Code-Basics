import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates import Template

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

class Emailer():
    subject = ''
    context = {}
    to_emails = []
    has_html = False
    test_send = False
    from_email = 'workwithruby <workwithrubyy@gmail.com>' #because this is the only email i'll be sending from
    template_html = None
    template_name = None

    def __init__ (self, subject='', template_name = None,context = {}, template_html=None, to_emails=None, test_send = False):
        if template_name == None and template_html==None:
            raise Exception('You must set a template')
        assert isinstance (to_emails, list)
        self.to_emails = to_emails
        self.subject = subject
        if template_html != None:
            self.has_html = True
            self.test_send = test_send
            self.template_html = template_html
        self.template_name = template_name
        self.context = context
        self.test_send = test_send

    def format_msg(self):
        msg = MIMEMultipart ('alternative')
        msg['From'] = self.from_email
        msg['To'] = ','.join(self.to_emails)
        msg['Subject'] = self.subject
        
        if self.template_name != None:
            tmpl_str = Template(template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(), 'plain')
            print(txt_part)
            msg.attach (txt_part)
        if self.template_html != None:
            tmpl_str = Template(template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(), 'html')
            msg.attach (html_part)
            print(html_part)
        msg_str =msg.as_string()
        return msg_str
    
        #txt_part = MIMEText(text, 'plain')
        #msg.attach (txt_part)
        #if html != None:
         #   html_part = MIMEText(html, 'html')
          #  msg.attach(html_part)
        
    def send(self): 
        msg = self.format_msg()
    #login to my smtp server
        did_send = False
        if not self.test_send:
            with smtplib.SMTP (host ='smtp.gmail.com', port = 587) as server:
                msg_str = ''
                server.ehlo()
                server.starttls()
                server.login(username, password)
                try: #this is a way to catch exceptions
                    server.sendmail(from_email, to_emails, msg_str)
                    did_send = True
                except:
                    did_send =False
        return did_send
#with smtplib-SMTP()as server:
#server.login()
#pass