# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')

#smtp_server = raw_input('SMTP server: ')
#smtp_port = raw_input('SMTP port: ')

msg = MIMEText('hello, send by Python... no ehlo', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

#server = smtplib.SMTP(smtp_server, 25)
#server = smtplib.SMTP('smtp.gmail.com:587')

#server.connect("smtp.gmail.com", "submission")
#server = smtplib.SMTP(smtp_server, smtp_port)


'''
gmail smtp;  port  and gmail --> Security -> Account permissions -> Access for less secure apps, enable this option.

About this option: https://support.google.com/accounts/answer/6010255
'''
#server = smtplib.SMTP('smtp.gmail.com', 587)


'''
hotmail smtp;  port
'''
server = smtplib.SMTP('smtp.live.com', 587)
#server.ehlo()

'''
 without server.starttls() : smtplib.SMTPException: SMTP AUTH extension not supported by server.
 '''
server.starttls() 
#server.startssl()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()