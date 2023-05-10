import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'Email'
email['subject'] = 'Subject'

email.set_content(html.substitute({'name': 'Name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Email', 'Password')
    smtp.send_message(email)
    print('all set')



