import paramiko

ccl_blacklist = ['SC Message Type']

def main():

    client = paramiko.SSHClient()
    client.load_system_host_keys()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect('192.168.101.133', 22, 'root', 'fiscal')

    stdin, stdout, stderr = client.exec_command('cd /home/ccl/ccl && less CCLlog.dat')

    output = ""

    for line in stdout:
        if not any(s in line for s in ccl_blacklist):
            output=output+line

    if output != "":
        print(output)
    else:
        print("Failed to read from CCLlog.")

    client.close()

if __name__ == "__main__":
    main()