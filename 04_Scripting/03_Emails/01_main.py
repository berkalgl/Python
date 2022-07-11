#Comes with built in
import imp
import smtplib
from email.message import EmailMessage

#stmp stands for simple mail transfer protocol

# basic email sender
email = EmailMessage()
email['from'] = 'Berk Algul'
email['to'] = 'dummyberkalgul@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(' To access it click here ')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        print('Hello')
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummyberkalgul@gmail.com', '123')
        smtp.send_message(email)
        print('All good !')

except Exception as ex:
    print(ex)

#with html template
from string import Template
#docs.python.org/3/library/string.html
from pathlib import Path

html = Template(Path('email_template.html').read_text())

email = EmailMessage()
email['from'] = 'Berk Algul'
email['to'] = 'dummyberkalgul@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

d = {'name': 'Berk'}
email.set_content(html.substitute(d), 'html')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        print('Hello')
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummyberkalgul@gmail.com', '123')
        smtp.send_message(email)
        print('All good !')

except Exception as ex:
    print(ex)

