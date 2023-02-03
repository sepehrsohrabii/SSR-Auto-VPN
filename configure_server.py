import time
from server_creator import server_creator
import paramiko
import re
from SECRETS import SHADOWSOCKSR_PASSWORD, SSH_PRIVATE_KEY_PASS, EMAIL_SENDER
from sendemail import get_email_info


# 3.Configure servers
def configure_server(list, server_name):
    # 3.2.Login to server
    server_access_info = server_creator(server_name)

    # Connection details
    host = server_access_info['server_ip']
    username = 'root'

    # The path to the private key file
    private_key_file = "./file.key"

    # The password to unlock the private key
    private_key_password = SSH_PRIVATE_KEY_PASS

    # Load the private key
    private_key = paramiko.RSAKey.from_private_key_file(private_key_file, password=private_key_password)

    # Create an instance of the SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        time.sleep(20)
        ssh.connect(host, username=username, pkey=private_key)
        # Successful connection message
        print("Connected to {} as {}".format(host, username))

    except Exception as e:
        print("Error: {}".format(e), "Sleep time was 20 seconds. Now going to try 30 seconds.")
        time.sleep(30)
        ssh.connect(host, username=username, pkey=private_key)
        # Successful connection message
        print("Connected to {} as {}".format(host, username))

    except Exception as e:
        print("Error: {}".format(e), "Sleep time was 30 seconds. Now going to try 40 seconds.")
        time.sleep(40)
        ssh.connect(host, username=username, pkey=private_key)
        # Successful connection message
        print("Connected to {} as {}".format(host, username))


    # Run a command on the VPS
    ssh.exec_command("yes" + "\n")
    ssh.exec_command("\n")
    ssh.exec_command("\n")
    ssh.exec_command("\n")

    # wget ShadowsocksR
    try:
        stdin, stdout, stderr = ssh.exec_command('wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssrmu.sh && chmod +x ssrmu.sh')
        exit_status = stdout.channel.recv_exit_status()  # Blocking call
        if exit_status == 0:
            print("ssrmu.sh downloaded")
        else:
            print("Error", exit_status)
        print("ssrmu.sh download is ok.")
    except Exception as e:
        print("Error: {}".format(e))
        exit()

    # Install ShadowsocksR
    port = 2333
    try:
        stdin, stdout, stderr = ssh.exec_command(f"./ssrmu.sh <<< $'1\n\nAdmin\n{port}\n{SHADOWSOCKSR_PASSWORD}\n10\n5\n2\nn\n\n\n\n\n\n'")
        exit_status = stdout.channel.recv_exit_status()  # Blocking call
        if exit_status == 0:
            print("ShadowsocksR installed.")
        else:
            print("Error", exit_status)
        output = stdout.read().decode()
        print(output)
        print("ShadowsocksR installation is ok.")
    except Exception as e:
        print("Error: {}".format(e))
        exit()

    # Get the user link that starts from ssr://
    pattern = r"ssr:\/\/.*"
    match = re.search(pattern, output)
    if match:
        user_link = match.group()
        print('This is Admin\'s user link: ')
        print(user_link)
        print('Going to send it.')
        get_email_info("admin", EMAIL_SENDER, user_link)


    # Create users
    for user in list:
        name = user["name"]
        email = user["email"]
        port += 1
        stdin, stdout, stderr = ssh.exec_command(f"./ssrmu.sh <<< $'7\n1\n{name}\n{port}\n{SHADOWSOCKSR_PASSWORD}\n10\n5\n2\nn\n1\n\n\n\n\nn'")
        exit_status = stdout.channel.recv_exit_status()  # Blocking call
        if exit_status == 0:
            print(f"user {name} created successfully.")
        else:
            print("Error", exit_status)
        # Print the output of the command
        output = stdout.read().decode()

        # Get the user link that starts from ssr://
        pattern = r"ssr:\/\/.*"
        match = re.search(pattern, output)
        if match:
            user_link = match.group()
            print(f'This is {name}\'s user link: ')
            print(user_link)
            print('Going to send it.')
            get_email_info(name, email, user_link)

    # Close the connection
    ssh.close()
