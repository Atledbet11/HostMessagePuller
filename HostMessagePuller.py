import paramiko

# list of strings to look for in lines indicating that the line may be ignored.
ccl_blacklist = ['SC Message Type']

def main():

    # Opens a new paramiko client that we then use to ssh with later.
    client = paramiko.SSHClient()

    # Tries to load any available system host keys.
    client.load_system_host_keys()

    # Overrides the host key if it is missing from the local system host keys.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connects to the host machine
    client.connect('192.168.101.133', 22, 'root', 'fiscal')

    # Executes commands across to the connected client.
    # The commands executed navigate to the ccl directory and less the CCLlog.
    stdin, stdout, stderr = client.exec_command('cd /home/ccl/ccl && less CCLlog.dat')

    # This stores the standard output into the variable lines so that we can close the connection and keep the output.
    lines = stdout.readlines()

    # Here we close the ssh connection to the machine.
    client.close()

    # Initialize the output variable used to hold important data.
    output = ""

    # For each line found in the standard output,
    for line in lines:

        # Check for blacklisted strings contained in the list ccl_blacklist.
        if not any(s in line for s in ccl_blacklist):

            # If none of the blacklisted strings are contained in the line, then add the line to the output variable.
            output=output+line

    # If the output is not empty
    if output != "":

        # Print the outputted lines.
        print(output)

    # IF the output is empty
    else:

        # Tell the user that we could not find any host messages in the log.
        print("Failed to find host messages in the log.")

if __name__ == "__main__":
    main()