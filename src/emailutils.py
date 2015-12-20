'''
Created on Apr 9, 2012

@author: peng
'''
from subprocess import Popen
from subprocess import PIPE
from email.mime.text import MIMEText


def send_email(subject, body, fromaddrs, toaddrs):
    '''send email'''
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg["From"] = fromaddrs
    msg["To"] = toaddrs
    p = Popen(["sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())


def send_mail_mailgun(subject, body, fromaddrs, toaddrs):
    '''send mail with mailgan'''
    import requests
    resp = requests.post(
        "https://api.mailgun.net/v2/xxxx.mailgun.org/messages",
        auth=("api", "key-xxxxxxxxxxxxxxxxxxxxxxxxxxx"),
        data={"from": fromaddrs,
              "to": toaddrs,
              "subject": subject,
              "html": body})
    if resp.status_code != 200:
        return False
    return True

