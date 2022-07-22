import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService():
    def __init__(self):
        self.client=os.getenv('EMAIL_CLIENT', 'netrava1000@gmail.com')
        self.user_email=os.getenv('EMAIL_ID', 'netravati1000@gmail.com')
        self.user_password=os.getenv('EMAIL_PASSWORD', 'electrical')
        self.connect(self.client,self.user_email,self.user_password)

    def connect(self,client,user_email,user_password):
        con='smtp.{}.com:587'.format(client)
        self.server=smtplib.SMTP(con)
        self.server.starttls()
        return self.server.login(user_email,user_password)

    def send_message(self,msg_dict):
        msg= MIMEMultipart()
        msg['From']=self.user_email
        msg['To']=msg_dict['user_email']
        msg['Subject']=msg_dict['subject']
        msg.attach(MIMEText(msg_dict['message'],'plain'))
        self.server.sendmail(msg['From'],msg['To'],msg.as_string())
        self.server.quit()

email=dict(user_email='harikrishna.srds@gmail.com', subject='My wishes',message='Good Morning!..')
EmailService().send_message(msg_dict=email)


