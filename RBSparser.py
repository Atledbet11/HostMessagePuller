
###################################################
# Project: RBS Parser
# Description: Parse an RBS host message
#   to make it easy to read without manual work
# Built: Tate Ledbetter - 2020
###################################################

fieldSeparators = ['1C']

Standard_map_pre_Products = [
    {"Field": "Protocol Dependent Header", "Len": 1},
    {"Field": "Application Type", "Len": 2},
    {"Field": "Processing Mode", "Len": 1},
    {"Field": "Message Format Version", "Len": 1},
    {"Field": "Terminal Identification", "Len": 24},
    {"Field": "Device Identifier", "Len": 1},
    {"Field": "Message Sequence Number", "Len": 4},
    {"Field": "Transaction Code", "Len": 2},
    {"Field": "Account Type", "Len": 1},
    {"Field": "Entry Method", "Len": 1},
    {"Field": "Request Type", "Len": 1},
    {"Field": "Batch/Shift Number", "Len": 11},
    {"Field": "Transaction Sequence Number", "Len": 4},
    {"Field": "Local Transaction Date", "Len": 8},
    {"Field": "Local Transaction Time", "Len": 6},
    {"Field": "Total Amount", "Len": 8},
    {"Field": "Track Data", "Len": 0, "FS": fieldSeparators[0]},
    {"Field": "Total Number of Products", "Len": 2},
    {"Field": "Delimiter - 0", "Len": 1}
]

Product_Map = [
    {"Field": "Product Code", "Len": 3},
    {"Field": "Delimiter - 1", "Len": 1},
    {"Field": "Service Code", "Len": 1},
    {"Field": "Delimiter - 2", "Len": 1},
    {"Field": "Unit Measurement", "Len": 1},
    {"Field": "Delimiter - 3", "Len": 1},
    {"Field": "Number Of Units (Thousandths)", "Len": 6},
    {"Field": "Delimiter - 4", "Len": 1},
    {"Field": "Unit Cost (Thousandths)", "Len": 7},
    {"Field": "Delimiter - 5", "Len": 1},
    {"Field": "Total Price (Hundredths)", "Len": 8},
    {"Field": "Delimiter - 6", "Len": 1}
]

Standard_map_post_Products = [
    {"Field": "Retrieval Data", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Authorization Code", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Pin Data", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Cash Back Amount", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Customer Data", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Miscellaneous Return Data", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Terminal Features Data", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Application PAN Seq", "Len": 6},
    {"Field": "Track 2 Equivalent Data", "Len": 40},
    {"Field": "Other Amount", "Len": 16},
    {"Field": "Dedicated File Name", "Len": 34},
    {"Field": "Application Version Number", "Len": 8},
    {"Field": "Cardholder Verify Result", "Len": 10},
    {"Field": "Interface Device Serial Number", "Len": 20},
    {"Field": "Terminal Capabilities", "Len": 10},
    {"Field": "Terminal Type", "Len": 6},
    {"Field": "Transaction Sequence Counter", "Len": 12},
    {"Field": "Application Cryptogram", "Len": 20},
    {"Field": "Application Interchange Profile", "Len": 6},
    {"Field": "Application Transaction Counter", "Len": 8},
    {"Field": "Cryptogram Info Data", "Len": 6},
    {"Field": "Issuer Application Data", "Len": 68},
    {"Field": "Amount Authorized", "Len": 16},
    {"Field": "Term Country Code", "Len": 8},
    {"Field": "Term Verification Results", "Len": 12},
    {"Field": "Trans Currency Code", "Len": 8},
    {"Field": "Trans Date", "Len": 8},
    {"Field": "Trans Reference Currency Code", "Len": 8},
    {"Field": "Transaction Type", "Len": 4},
    {"Field": "Unpredictable Number", "Len": 12},
    {"Field": "Application Usage Control", "Len": 8},
    {"Field": "Auth Response Code", "Len": 6},
    {"Field": "Application Identifier", "Len": 36},
    {"Field": "Issuer Script Result", "Len": 14},
    {"Field": "Secondary Pin Block", "Len": 78},
    {"Field": "Obsolete", "Len": 12},
    {"Field": "Customer Exclusive Data", "Len": 24},
    {"Field": "Transaction Category Code", "Len": 5},
    {"Field": "Application Expiration Date", "Len": 10},
    {"Field": "Third Party Data", "Len": 68},
    {"Field": "eParams", "Len": 0, 'FS': fieldSeparators[0]},
    {"Field": "Protocol Dependent Trailer", "Len": 3}
]

def arrayToString(array):

    # Initialize the output string
    output = ''

    # For each value in the array
    for i in range(len(array)):

        # Add array[i] to the output string.
        output = output + array[i]

    # Return the string result of the array
    return output

# Returns a dictionary that can be printed, and the remaining message.
def dictionarySplit(dictArray, message):

    # Initialize the output dictionary
    outputDict = {}

    # Initialize the starting position
    startPos = 0

    # for each element in the array of dictionaries
    for i in range(len(dictArray)):

        # Get the length of the current element
        length = dictArray[i]['Len']

        # If the length is not pre defined or variable
        if length == 0:

            # Since this can return a valueError we have to put it in a try except clause
            try:

                # Get the index of the next field separator
                stopPos = message.index(dictArray[i]['FS'], startPos)

            # If Value Error is returned
            except ValueError:

                # The stop position is the end of the message.
                stopPos = len(message) - 1

            # Grab the message up until the nearest field separator
            outputDict[str(dictArray[i]['Field'])] = arrayToString(message[startPos:stopPos])

            # Set the start position to be right after the field separator.
            startPos = stopPos + 1

        else:

            # Add this element to the output dictionary
            outputDict[str(dictArray[i]['Field'])] = arrayToString(message[startPos:(startPos + length)])

            # Increment the start position
            startPos += length

    return outputDict, message[startPos:len(message)]


def RBS_Parser(message):

    # Initialize an array to store all of the dictionary results for later printing.
    parsedData = []

    # To begin we need to parse the message using the standard map pre products
    dict, msg = dictionarySplit(Standard_map_pre_Products, message)

    # Append the dictionary to the parsed data array
    parsedData.append(dict)

    # From this we get the total number of products listed off in the message
    products = int(dict['Total Number of Products'])

    # We need to parse each of the products out of the list.
    for i in range(products):

        # Parse out the product
        dict, msg = dictionarySplit(Product_Map, msg)

        # Append the product to the parsed data array
        parsedData.append(dict)

    # Now that the products have been pulled out of the message we need to grab the rest of the data
    dict, msg = dictionarySplit(Standard_map_post_Products, msg)

    # We need to append this data to the parsed data array
    parsedData.append(dict)

    return parsedData, msg


def main():
    message = ['02', 'L', 'P', '0', '6', '5', '4', '2', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '9', '9', '9', '0', '0', '1', '6', '1', '0', '7', '7', '2', '1', '1', '0', '1', '0', '2', '0', '2', '0', '0', '4', '0', '8', '0', '0', '1', '0', '0', '4', '0', '2', '0', '2', '0', '0', '9', '1', '8', '1', '3', '3', '0', '0', '2', '0', '0', '0', '0', '0', '1', '0', '0', '6', '0', '1', '1', '7', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '=', '2', '5', '1', '2', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1C', '0', '1', '-', '4', '5', '0', ':', 'O', ':', 'U', ':', '0', '0', '1', '0', '0', '0', ':', '0', '0', '0', '1', '0', '0', '0', ':', '0', '0', '0', '0', '0', '1', '0', '0', '\\', '1C', '1C', '1C', '1', '0', '0', '0', '2', '0', '0', '0', '0', '9', '0', '0', '2', '1', '2', '0', '0', '1', '0', '1', '4', '4', '2', '9', '5', '3', '8', 'F', '8', '9', 'B', '4', 'E', 'D', '3', 'D', '1C', '1C', '1C', '1C', '1', '1', '1', 'C', '20', '20', '20', '20', '03', '~']

    array, msg = RBS_Parser(message)

    for i in range(len(array)):
        for key,value in array[i].items():
            print(str(key) + ': ' + str(value))

    print(str(msg))

if __name__ == "__main__":
    main()