import paramiko
from scp import SCPClient





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host = '34.86.254.119'
    username = 'alexanderfournier'
    password = 'Reddit123!'

    key = paramiko.RSAKey.from_private_key_file('/Users/alexanderfournier/Desktop/key',password=password)

    ssh  = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,password=password,pkey=key)















