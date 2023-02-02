from server_creator import server_creator
import paramiko
import re
from SECRETS import SHADOWSOCKSR_PASSWORD
from sendemail import get_email_info


# 3.Configure servers
def configure_server(list, server_name):

    # 3.1.Create Hetzner Server with basic plans
    server_creator(server_name)

    # 3.2.Login to server
    server_access_info = server_creator.login_info

    # Connection details
    host = server_access_info['server_ip']
    username = 'root'
    password = server_access_info['root_password']

    # Create an instance of the SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the VPS server
    ssh.connect(host, username=username, password=password)

    # wget ShadowsocksR
    stdin, stdout, stderr = ssh.exec_command('wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssrmu.sh && chmod +x ssrmu.sh')
    output = stdout.read().decode()
    print(output)

    port = 2333
    # Install ShadowsocksR
    stdin, stdout, stderr = ssh.exec_command(f'./ssrmu.sh "1" "" "Admin" {str(port)} {SHADOWSOCKSR_PASSWORD} "10" "5" "2" "n" "" "" "" "" ""')
    output = stdout.read().decode()
    print(output)

    # Get the user link that starts from ssr://
    pattern = r"ssr:\/\/.*"
    match = re.search(pattern, output)
    if match:
        user_link = match.group()
        print('This is Admin\'s user link: ')
        print(user_link)
        print('Goint to send it.')
        get_email_info("admin", "sepehr0sohrabi@gmail.com", user_link)


    # Create users
    for user in list:
        name = user["name"]
        email = user["email"]
        port += 1
        stdin, stdout, stderr = ssh.exec_command(f'./ssrmu.sh "7" "1" {name} {str(port)} {SHADOWSOCKSR_PASSWORD} "10" "5" "2" "n" "1" "" "" "" "" "n"')

        # Print the output of the command
        output = stdout.read().decode()

        # Get the user link that starts from ssr://
        pattern = r"ssr:\/\/.*"
        match = re.search(pattern, output)
        if match:
            user_link = match.group()
            print(f'This is {name}\'s user link: ')
            print(user_link)
            print('Goint to send it.')
            get_email_info(name, email, user_link)

    # Close the connection
    ssh.close()

