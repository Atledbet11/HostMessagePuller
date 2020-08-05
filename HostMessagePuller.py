import paramiko
import datetime
from z01parser import *

# list of strings to look for in lines indicating that the line may be ignored.
ccl_blacklist = ['SC Message Type', 'ERR:', '(2)', 'CCLMain']

# This gets the timestamp of a provided date and time in epoch form
def getTimestamp(date, time):

    # Split the date at the -'s
    sDate = date.split('-')

    # If the date provided only contains a 2 digit year.
    if len(sDate[0]) == 2:

        # Append "20" to the front of the year
        sDate[0] = int("20" + sDate[0])

    # Else convert the date to an int
    else:
        sDate[0] = int(sDate[0])

    # Convert to Int, Removing leading zero's from the month and day
    sDate[1] = int(sDate[1])
    sDate[2] = int(sDate[2])

    # If a time is provided
    if not time == '':

        # Split the time at the (.)
        temp = time.split('.')

        # Add the hours Minutes and Seconds to the time variable
        sTime = temp[0].split(':')

        # Add the milliseconds to the time variable
        sTime.append(temp[1])

        # For each piece of the time variable.
        for i in range(len(sTime)):

            # Convert sTime to an integer, this also removes leading zeros.
            sTime[i] = int(sTime[i])

    # If a time was not provided
    else:
        sTime = [0, 0, 0, 0]

    # Use datetime to return the timestamp of the provided date
    return datetime.datetime(sDate[0], sDate[1], sDate[2], sTime[0], sTime[1], sTime[2], sTime[3]).timestamp()

# This tests to see if a connection can be made to the IP provided.
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
        client.connect(str(IP), 22, 'ccl', 'fiscal')

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

# This pulls all of the lines from the CCL log.
def pullMainCCLLog(IP):

    # Opens a new paramiko client that we then use to ssh with later.
    client = paramiko.SSHClient()

    # Tries to load any available system host keys.
    client.load_system_host_keys()

    # Overrides the host key if it is missing from the local system host keys.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connects to the host machine
    client.connect(str(IP), 22, 'ccl', 'fiscal')

    # Executes commands across to the connected client.
    # The commands executed navigate to the ccl directory and less the CCLlog.
    stdin, stdout, stderr = client.exec_command('cd /home/ccl/ccl && less CCLlog.dat')

    # This stores the standard output into the variable lines so that we can close the connection and keep the output.
    lines = stdout.readlines()

    # Here we close the ssh connection to the machine.
    client.close()

    # Return the gathered lines
    return lines

# This will pull all of the lines for a specified day from the CCL log and its backups.
def pullCCLlogDate(IP, date):

    # Convert the date to a timestamp
    tDate = getTimestamp(date, '')

    # Initialize the Output list
    outputLines = []

    # Opens a new paramiko client that we then use to ssh with later.
    client = paramiko.SSHClient()

    # Tries to load any available system host keys.
    client.load_system_host_keys()

    # Overrides the host key if it is missing from the local system host keys.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connects to the host machine
    client.connect(str(IP), 22, 'ccl', 'fiscal')

    # Executes commands across to the connected client.
    # The commands executed navigate to the ccl directory and less the CCLlog.
    stdin, stdout, stderr = client.exec_command('cd /home/ccl/ccl && less CCLlog.dat')

    # This stores the standard output into the variable lines so that we can close the connection and keep the output.
    lines = stdout.readlines()

    # Get the timestamp for the date of the first line in the CCL.
    cclOldestDate = getTimestamp(lines[0].split(' ')[0], '')

    # If the date in the first line of the CCLlog is older than the requested date.
    # We know that the date we are looking for is in the CCL log.
    if cclOldestDate <= tDate:

        # If the first line in the CCLlog contains the date
        if cclOldestDate == tDate:

            # Navigate to the logs directory and less the most recent CCLlog backup.
            stdin, stdout, stderr = client.exec_command(
                'cd /home/ccl/ccl/logs && less $(ls -Art *CCLlog.dat.* | tail -n 1)'
            )

            # Store the lines collected from the backup file in the front of the variable lines.
            lines = stdout.readlines() + lines

    # Otherwise the date we are looking for will be in the logs folder
    else:

        # Get the date, time, and filename of all the backup logs in the logs directory.
        stdin, stdout, stderr = client.exec_command(
            'cd /home/ccl/ccl/logs && find . -type f -print0 | xargs -0 stat -c "%y %n" | grep "CCL"'
        )

        # lines contains the date, time, and filename of all the backup logs.
        lines = stdout.readlines()

        # Declare list to hold all timestamps and filenames.
        relevantList = []

        # For each backup file
        for line in lines:

            # Strip out the date and time to obtain a timestamp for the file
            tempList = line.split()

            # Build the relevant list containing the file timestamp and name.
            relevantList.append({'Timestamp': getTimestamp(tempList[0], ''), 'Filename': tempList[3]})

        # Sort the relevant list based off of the timestamp.
        relevantList.sort(key=lambda x: x['Timestamp'])

        # Clear the lines variable
        lines = []

        # For each item in the relevant list
        for log in relevantList:

            tStamp = log['Timestamp']

            # If the timestamp for the log is less than the date we are looking for
            if tStamp < tDate:

                # Continue to the next log
                continue

            # Else if the timestamp for the log is equal to the date we are looking for
            else:

                # Pull the log
                stdin, stdout, stderr = client.exec_command(
                    'cd /home/ccl/ccl/logs && less ' + log['Filename']
                )

                # Extend the log to the lines variable
                lines.extend(stdout.readlines())

                # If the timestamp for the log is equal to the date we are looking for
                if tStamp == tDate:

                    # Continue to the next log - because the next log probably contains more of this date
                    continue

                # Elif the timestamp is greater to the date we are looking for
                elif tStamp > tDate:

                    # Break out of the loop, this should be all the data we need
                    break

    # For all the lines returned from the CCLlog.
    for line in lines:

        # If the line contains the date being searched for.
        if date in line:

            # Add it to the output list.
            outputLines.append(line)

    # Here we close the ssh connection to the machine.
    client.close()

    # Return the gathered lines
    return outputLines

# This filters the provided lines (From the CCL) and provides a dictionary containing any host message.
def logFilter(lines):

    # Initialize the output variable(filteredCCLlog) used to hold important data.
    filteredCCLlog = []

    # Build a dictionary for holding all the messages produced by this tool.
    outputList = []

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

        # Make sure the relevantInfo dictionary is initialized and also empty.
        relevantInfo = {}

        # Make sure the host variable is initialized empty.
        host = ''

        # Looks for these to be in the current string.
        ccl_whitelist = [ ' Request (', ' request (', ' Response (', ' response (']

        # For each item in the ccl whitelist
        for item in ccl_whitelist:

            # If the current item is in the string
            if item in currentString:

                # Split the currentString to obtain the date of the transaction
                currentString = currentString.split(' ', 1)

                # Append the date to the relevantInfo Array
                relevantInfo['Date'] = currentString[0]

                # Split the currentString's second half at ' - INF: ' to obtain the timestamp.
                currentString = currentString[1].split(' - INF: ')

                # Append the timestamp to the relevant info array.
                relevantInfo['Time'] = currentString[0]

                # Split the string at the whitelist item
                currentString = currentString[1].split(item)

                # If the index of the item is less than two, then this is a Request.
                if ccl_whitelist.index(item) < 2:

                    # Append 'Response' into the relevant information array.
                    relevantInfo['MessageType'] = 'Request'

                # Otherwise the item is a response
                else:

                    # Append 'Request' to the relevant information array.
                    relevantInfo['MessageType'] = 'Response'

                # Append the host to the relevant info dictionary.
                relevantInfo['Host'] = currentString[0]

                # Append the message length to the relevant info dictionary.
                relevantInfo['Length'] = ''.join(filter(lambda x: x.isdigit(), currentString[1]))

                # Initialize msgArray and make sure it is empty.
                msgArray = []

                # Initialize count for the for loop at 1
                count = 1

                # While message list length is less than the specified message length
                while (len(msgArray) < int(relevantInfo['Length'])):

                    # Split the next index at 'INF: ' on the line starting at the index(i) plus the loop count
                    message = filteredCCLlog[i + count].split('INF: ')

                    # Split the message at the space characters and add them to the array.
                    message = message[1].split()

                    # Add all of the message bytes using '.extend'
                    msgArray.extend(message)

                    # Increment the counter - this is used to choose the line in the CCL log being operated on.
                    count += 1

                # Create an entry in the dictionary for the new entry
                relevantInfo['Message'] = msgArray

                # Append the information to the output list
                outputList.append(relevantInfo)

    # Return the output list
    return outputList

# This pulls the nearest transaction to the date and time provided.
def getTransactionTime(IP, date, time):

    tTime = getTimestamp(date, time)

    # Grab the transactions for the specified Date.
    lines = pullCCLlogDate(IP, date)

    # Filter out the lines into a usable list.
    lines = logFilter(lines)

    # If there were no transactions found for that day
    if len(lines) == 0:

        # Tell the user that we could not find any results for that day.
        print("Could not find a transaction for the day requested")

    # Temp list of lines to be sifted through
    tempLines = []

    # Define outputLines variable
    outputLines = []

    # For each line returned for the date requested
    for line in lines:

        # Fetch the timestamp for the line, and calculate the time difference from the desired transaction.
        timeDiff = getTimestamp(line['Date'], line['Time']) - tTime

        # Build an array containing the time Difference and the line for the transaction
        tempLines.append({'TimeDifference': timeDiff, 'Line': line})

    # Finds the closest line to the provided date, by locating the lowest value for timeDifference in the list.
    closestLine = min(tempLines, key=lambda x: abs(x['TimeDifference']))

    # If the closest line in the list is a request, grab the next line (Should be a response) too
    if closestLine['Line']['MessageType'] == 'Request':

        # Get the next index of the array.
        nextIndex = tempLines.index(closestLine) + 1

        # If the next index is in the array.
        if nextIndex < len(tempLines):

            # Get the next line after the closest Line.
            nextLine = tempLines[nextIndex]['Line']

            # If the next line contains a response
            if nextLine['MessageType'] == 'Response':

                # Add the request and response to the output list.
                outputLines = [closestLine['Line'], nextLine]

            # Else the response could not be found
            else:

                # Set the output list equal to the request that was found
                outputLines = [closestLine['Line']]

        else:

            # Set the output list equal to the Line that was found
            outputLines = [closestLine['Line']]

    # Else if the closest line was a response
    elif closestLine['Line']['MessageType'] == 'Response':

        # Get the index of the previous line
        previousIndex = tempLines.index(closestLine) - 1

        if not previousIndex < 0:

            # Get the previous line.
            previousLine = tempLines[previousIndex]['Line']

            # If the previous line was a request, Which should usually be the case.
            if previousLine['MessageType'] == "Request":

                # The outputlines should contain the request and the response.
                outputLines = [previousLine, closestLine['Line']]

            # Else the matching request could not be found, so just return the response message.
            else:

                # Set the Output list equal to the response that was found.
                outputLines = [closestLine['Line']]

        else:

            # Set the Output list equal to the response that was found.
            outputLines = [closestLine['Line']]

    # Return the best fitting lines we located for this transaction.
    return outputLines


def main():
    # This is the IP that the script will pull transactions from
    IP = "192.168.1.43"

    # This is the date that the script will pull
    date = "20-07-16"

    # This is the time the script hopes to find a related transaction to.
    # It simply pulls the closest transaction to this time
    time = "14:34:15.250"

    # If
    if testIP(IP):

        lines = getTransactionTime(IP, date, time)

        for line in lines:
            #print(str(line))

            if line['Host'] == "Z01":
                if line['MessageType'] == "Request":
                    normalized_dict(request_parser(dict_maker(map_selection_func(line['Message'])), line['Message']))

    else:
        print("Failed to connect to the IP: " + str(IP))

if __name__ == "__main__":
    main()