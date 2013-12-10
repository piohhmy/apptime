import os
import sendgrid

EMAIL_HOST_USER = os.getenv('SENDGRID_USERNAME', 'app20099764@heroku.com')
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD', 'tyibjs5x')

s = sendgrid.Sendgrid(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, secure=True)

fromEmail = "sandbox.apptime@gmail.com"

def send_msg(toEmail, message_string):
    msg = sendgrid.Message(fromEmail, "Apptime Sandbox Message", message_string)
    msg.add_to(toEmail)
    
    s.web.send(msg)

