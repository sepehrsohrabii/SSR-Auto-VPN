import paramiko

# Connection details
host = 'your_server_ip_or_hostname'
username = 'your_username'
password = 'your_password'

# Create an instance of the SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the VPS server
ssh.connect(host, username=username, password=password)

# Execute the desired bash command
stdin, stdout, stderr = ssh.exec_command('your_bash_command')

# Print the output of the command
print(stdout.read().decode())

# Close the connection
ssh.close()
