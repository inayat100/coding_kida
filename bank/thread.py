import random
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from io import BytesIO
import threading
from .models import otp_save

class class_email_otp(threading.Thread):
    def __init__(self,email,o):
        self.mail = email
        self.otp = o
        threading.Thread.__init__(self)
    def run(self):
        send_mail(
            'otp for verifactions',
            str(self.otp),
            settings.EMAIL_HOST_USER,
            [self.mail],
            fail_silently=False
        )
        print("this done email...")

class class_money_otp(threading.Thread):
    def __init__(self, email, o):
        self.mail = email
        self.o = o
        threading.Thread.__init__(self)
    def run(self):

        html_content = render_to_string("tem_email.html", {'otp': self.o})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "otp for verifactions",
            text_content,
            settings.EMAIL_HOST_USER,
            [self.mail]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

class class_forget_password(threading.Thread):
        def __init__(self, s_email,token,username):
            self.mail = s_email
            self.token = token
            self.username = username
            threading.Thread.__init__(self)

        def run(self):
            html_content = render_to_string("tem_email.html", {'token': self.token, 'name': self.username, 'reset': True})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "otp for verifactions",
                text_content,
                settings.EMAIL_HOST_USER,
                [self.mail]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

class class_send_money_sender(threading.Thread):
    def __init__(self,email,fname,lname,money,account,time,status):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.money = money
        self.account = account
        self.time = time
        self.status = status
        threading.Thread.__init__(self)

    def run(self):
        send = {'fname': self.fname, 'lname': self.lname, 'money': self.money, 'account': self.account, 'time': self.time, 'status': self.status,
                'sender': True}
        html_content = render_to_string("tem_email.html", send)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            f'Sent Rs. {self.money} To {self.fname} {self.lname}',
            text_content,
            settings.EMAIL_HOST_USER,
            [self.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        print("this is send money classs if done now")


class class_send_money_resever(threading.Thread):
    def __init__(self,email,fname,lname,money,account,time,status):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.money = money
        self.account = account
        self.time = time
        self.status = status
        threading.Thread.__init__(self)

    def run(self):
        send = {'fname': self.fname, 'lname': self.lname, 'money': self.money, 'account': self.account, 'time': self.time, 'status': self.status,
                'resever': True}
        html_content = render_to_string("tem_email.html", send)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            f'Resever Rs. {self.money} From {self.fname} {self.lname}',
            text_content,
            settings.EMAIL_HOST_USER,
            [self.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        print("this is send money classs if done now")
