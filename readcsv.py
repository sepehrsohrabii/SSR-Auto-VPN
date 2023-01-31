import csv
from sendemail import send_email


sender = "sepehr0sohrabi@gmail.com"
password = "dzayxovqbjpzfmss"

with open('users.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        csv_row_list = row
            
        try:
            if "ssr" in csv_row_list[17] and int(csv_row_list[4]) == 1:
                print(csv_row_list[0], csv_row_list[1], csv_row_list[2], 'Sent!')
                subject = f'VPN connection for {csv_row_list[1]} from server two'
                body = f'''وی پی ان برای {csv_row_list[1]}:

{csv_row_list[17]}

** اپلیکیشن اندروید: SSRAY
** اپلیکیشن آیفون: FairVPN
   '''
                recipients = [csv_row_list[2]]
                send_email(subject, body, sender, recipients, password)
        except:
            pass