import paramiko

# list of strings to look for in lines indicating that the line may be ignored.
ccl_blacklist = ['SC Message Type', 'ERR:', '(2)']

def testIP(IP):

    # Opens a new paramiko client that we then use to ssh with later.
    client = paramiko.SSHClient()

    # Tries to load any available system host keys.
    client.load_system_host_keys()

    # Overrides the host key if it is missing from the local system host keys.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Try to connect to the requested machine
    try:

        # Connects to the host machine
        client.connect(str(IP), 22, 'root', 'fiscal')

        # Closes the client
        client.close()

        # Return true because we were able to connect to the host machine
        return True

    # Failed to connect to the requested machine
    except:

        # Close the client
        client.close()

        # Return false because we were unable to connect to the host machine
        return False


def pullMainCCLLog(IP):

    # Opens a new paramiko client that we then use to ssh with later.
    client = paramiko.SSHClient()

    # Tries to load any available system host keys.
    client.load_system_host_keys()

    # Overrides the host key if it is missing from the local system host keys.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connects to the host machine
    client.connect(str(IP), 22, 'root', 'fiscal')

    # Executes commands across to the connected client.
    # The commands executed navigate to the ccl directory and less the CCLlog.
    stdin, stdout, stderr = client.exec_command('cd /home/ccl/ccl && less CCLlog.dat')

    # This stores the standard output into the variable lines so that we can close the connection and keep the output.
    lines = stdout.readlines()

    # Here we close the ssh connection to the machine.
    client.close()

    # Return the gathered lines
    return lines

def pullCCLlogDate(IP, date):
    print("moo")

def logFilter(lines):

    # Initialize the output variable(filteredCCLlog) used to hold important data.
    filteredCCLlog = []

    # Build a dictionary for holding all the messages produced by this tool.
    outputDict = {}

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

        # Looks for these to be in the current string.
        ccl_whitelist = [' Response (', ' Request (']

        # If the element contains the start of a Response
        if any(s in currentString for s in ccl_whitelist):

            # Split the currentString to obtain the date of the transaction
            currentString = currentString.split(' ', 1)

            # Append the date to the relevantInfo Array
            relevantInfo.append(currentString[0])

            # Split the currentString's second half at ' - INF: ' to obtain the timestamp.
            currentString = currentString[1].split(' - INF: ')

            # Append the timestamp to the relevant info array.
            relevantInfo.append(currentString[0])

            # If its a response message.
            if ccl_whitelist[0] in currentString[1]:

                # Split the string at ' Response ('
                currentString = currentString[1].split(ccl_whitelist[0])

                # Append 'Response' into the relevant information array.
                relevantInfo.append('Response')

            # If its a request message.
            elif ccl_whitelist[1] in currentString[1]:

                # Split the string at ' Request ('
                currentString = currentString[1].split(ccl_whitelist[1])

                # Append 'Request' to the relevant information array.
                relevantInfo.append('Request')

            # Append the host to the relevant info array.
            relevantInfo.append(currentString[0])

            # Append the message length to the relevant info array.
            relevantInfo.append(''.join(filter(lambda x: x.isdigit(), currentString[1])))

            # Initialize msgArray and make sure it is empty.
            msgArray = []

            # Initialize count for the for loop at 1
            count = 1

            # While message list length is less than the specified message length
            while (len(msgArray) < int(relevantInfo[4])):

                # Split the next index at 'INF: ' on the line starting at the index(i) plus the loop count
                message = filteredCCLlog[i + count].split('INF: ')

                # Split the message at the space characters and add them to the array.
                message = message[1].split()

                # Add all of the message bytes using '.extend'
                msgArray.extend(message)

                # Increment the counter - this is used to choose the line in the CCL log being operated on.
                count += 1

            # Get the length of the outputDict for use as the key/index
            outputLen = len(outputDict)

            # Create an entry in the dictionary for the new entry
            outputDict[outputLen] = [relevantInfo, msgArray]

    # Return the output dictionary
    return outputDict

def main():

    IP = "192.168.101.133"

    if testIP(IP):

        lines = pullMainCCLLog(IP)

        test = logFilter(lines)

        print(str(len(test)))

        for key, value in test.items():
            print(str(key) + ' - ' + str(value))
            print(str(key) + ' - ' + str(value[0][0]) + ' ' + str(value[0][1]))
    else:
        print("Failed to connect to the IP: " + str(IP))

if __name__ == "__main__":
    main()