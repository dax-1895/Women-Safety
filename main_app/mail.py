from os import link
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
from twilio.rest import Client

# Before using your email,  please ensure that you have set you gmail account to enable "less secure apps"
# Recheck this step that you have enabled the less secure app

def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()

    # Enter your Email and Password
    server.login("tests.daksh@gmail.com", "hello1895")
    email_html = open('main_app/templates/main_app/email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = 'Danger!'
    msg.attach(MIMEText(email_body, 'html'))
    
    # Again enter your Email ID
    msg['From'] = formataddr(("HELP", "tests.daksh@gmail.com"))

    # One last time add your email
    server.sendmail("tests.daksh@gmail.com", dest, msg.as_string())
    server.quit()

def send_message(name,number,link):
    account_sid ='ACd74ae6566e9b3a12e19ecac0baa2fb98'
    auth_token = '28256b6e402e9cbc836dc180e70d2d76000'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=name+' is in danger. Click link below to find her: '+link,
            from_='+12183043415',
            to='+'+str(number)
        )

    # print(message.sid)