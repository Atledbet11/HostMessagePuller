import paramiko

# list of strings to look for in lines indicating that the line may be ignored.
ccl_blacklist = ['SC Message Type', 'ERR:']

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

    # Initialize the output variable(filteredCCLlog) used to hold important data.
    filteredCCLlog = []

    # For each line found in the standard output,
    for line in lines:

        # Check for blacklisted strings contained in the list ccl_blacklist.
        if not any(s in line for s in ccl_blacklist):

            # If none of the blacklisted strings are contained in the line, then add the line to the output variable.
            filteredCCLlog.append(line)

    # For each element in the output list
    for i in range(len(filteredCCLlog)):

        # Holds the current lines value so we can make changes as necessary without affecting the line.
        currentString = filteredCCLlog[i]

        # Make sure the relevantInfo list is initialized and also empty.
        relevantInfo = []

        # Make sure the host variable is initialized empty.
        host = ''

        # If the element contains the start of a Response
        if ' Response (' in currentString:

            # Split the currentString to obtain the date of the transaction
            currentString = currentString.split(' ', 1)

            # Append the date to the relevantInfo Array
            relevantInfo.append(currentString[0])

            # Split the currentString's second half at ' - INF: ' to obtain the timestamp.
            currentString = currentString[1].split(' - INF: ')

            # Append the timestamp to the relevant info array.
            relevantInfo.append(currentString[0])

            # Split the currentString's second half at ' Response (' to obtain the host and message length.
            currentString = currentString[1].split(' Response (')

            # Append the host to the relevant info array.
            relevantInfo.append(currentString[0])

            # Append the message length to the relevant info array.
            relevantInfo.append(''.join(filter(lambda x: x.isdigit(), currentString[1])))

            # Print the relevant information.
            print('Index: ' + str(i) + ' - ' + str(relevantInfo))


if __name__ == "__main__":
    main()