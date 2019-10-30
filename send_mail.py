import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = '注册功能.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自21世纪的邮件', '296931626@qq.com', '18801363979@sina.cn'
    text_content = '欢迎访问这个！'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.网站.com</a>地球很漂亮！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()