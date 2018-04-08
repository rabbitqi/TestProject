#coding=utf-8
import sys,os
import smtplib
import importlib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send(results):
    _user = "18813684097@163.com"
    _pwd  = "aiqi0203"
    html = """\
    <html>
      <head></head>
      <body>
        <p>%s</p><br>        
      </body>
    </html>
    """ %(results)

    msg = MIMEMultipart('alternative')
    part = MIMEText(html, "html", "utf-8")
    msg.attach(part)

    importlib.reload(sys)
    # sys.setdefaultencoding('utf8')
    msg["Subject"] = u"用户端接口异常"
    msg["From"]    = _user

    _to = '18813684097@163.com,bu3g_yuqi@163.com'
    _cc = ''
    toaddrs = ['18813684097@163.com','bu3g_yuqi@163.com']

    msg["To"]      = _to
    msg["CC"]      = _cc
    msg.as_string().encode('ascii')
    s = smtplib.SMTP("smtp.163.com", timeout=30)
    s.login('18813684097@163.com', 'aiqi0203')
    s.sendmail(_user, toaddrs, msg.as_string())
    s.close()