import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('SERVER_IPADDR', username='USERNAME', password='PASSWORD')
except paramiko.SSHException:
        print "Connection Failed"
        quit()

stdin,stdout,stderr = ssh.exec_command("pwd")

for line in stdout.readlines():
        print line.strip()
ssh.close()
