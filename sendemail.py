import smtplib
from email.mime.text import MIMEText
from SECRETS import EMAIL_PASSWORD

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


def get_email_info(user_name, user_mail, user_link):
    sender = "sepehr0sohrabi@gmail.com"
    password = EMAIL_PASSWORD
    subject = f'VPN connection for {user_name} from server two'
    body = f'''وی پی ان برای {user_name}:
    
    {user_link}
    
    ** اپلیکیشن اندروید: SSRAY
    ** اپلیکیشن آیفون: FairVPN
       '''
    recipients = [user_mail]
    send_email(subject, body, sender, recipients, password)
    print(user_name, user_mail, 'Sent!')



