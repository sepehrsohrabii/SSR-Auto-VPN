import smtplib
from email.mime.text import MIMEText
from SECRETS import EMAIL_PASSWORD, EMAIL_SENDER


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


def get_email_info(user_name, user_mail, user_link):
    sender = EMAIL_SENDER
    password = EMAIL_PASSWORD
    subject = f'User for {user_name}.'
    with open("email_template.html", "r") as f:
        template = f.read()

    body = template.format(user_name=user_name, user_link=user_link)
    recipients = [user_mail]
    send_email(subject, body, sender, recipients, password)
    print(user_name, user_mail, 'Sent!' + '\n')
