"""
Created on Apr 9, 2012

@author: peng
"""
from subprocess import Popen
from subprocess import PIPE
from email.mime.text import MIMEText


def send_email(subject, body, fromaddrs, toaddrs):
    """send email"""
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg["From"] = fromaddrs
    msg["To"] = toaddrs
    p = Popen(["sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())


def send_mail_mailgun(subject, body, fromaddrs, toaddrs):
    """send mail with mailgan"""
    import requests
    resp = requests.post(
        "https://api.mailgun.net/v3/raa.mailgun.org/messages",
        auth=("api", "key-3zteyls08bmbfxk7hh7mhw2xs44wfa70"),
        data={"from": fromaddrs,
              "to": toaddrs,
              "subject": subject,
              "html": body})
    print resp.status_code
    if resp.status_code != 200:
        return False
    return True


print send_mail_mailgun('test', 'test', 'prong@abcft.com', ['prong@abcft.com'])
