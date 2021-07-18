# 第一题
# from datetime import datetime,timedelta
# import os
# import time
#
# now = datetime.now()
# before_5day = now - timedelta(days=5)
#
# now_format = now.strftime('%Y-%m-%d_%H-%M-%S')
# # str_now = str(now_format).replace(' ', '_').split('.')[0].replace(':', '-')
# file_name = 'save_fivedayago_time_' + now_format + '.txt'
# file = open(file_name, 'w')
# file.write(str(before_5day))
# file.close()

# 第二题
import paramiko


def ssh_cli(ip, username, password, port=22, cmd='show run'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'usage:python Simple_SSH_Client -i ipaddr -u username -p password -c command'
    parser = ArgumentParser(usage=usage)
    parser.add_argument('-i', '--ipaddress', dest='ipaddress', help='SSH Server', default='1.1.1.1', type=str)
    parser.add_argument('-u', '--username', dest='username', help='SSH Username', default='root', type=str)
    parser.add_argument('-p', '--password', dest='password', help='SSH Password', default='123456', type=str)
    parser.add_argument('-c', '--command', dest='command', help='Shell Command', default='ls', type=str)

    #
    args = parser.parse_args()
    ssh_rev = ssh_cli(args.ipaddress, args.username, args.password, cmd=args.command)
    print(ssh_rev)
