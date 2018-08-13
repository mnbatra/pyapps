from email.mime.text import MIMEText
import smtplib


def send_email(email,height,average_height,count):
    from_email="seedhibaatnobakwasclearhai@gmail.com"
    from_password="Atcbtra1!"
    to_email=email

    subject="Height Data"
    message="Hey there, Average height of <strong>%s</strong> people surveyed so far is <strong>%s</strong>." % (count, average_height)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
