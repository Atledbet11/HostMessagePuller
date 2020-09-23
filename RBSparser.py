
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
    {"Field": "Track Data", "Len": 0, "Max Len": 98, "FS": 0},
    {"Field": "Product Information", "Len": 0, "Max Len": 643, "FS": 0, "Display": True},
]

Product_Map = [
    {"Field": "Product Code", "Len": 3},
    {"Field": "Delimiter - 1", "Len": 1, "Display": False},
    {"Field": "Service Code", "Len": 1},
    {"Field": "Delimiter - 2", "Len": 1, "Display": False},
    {"Field": "Unit Measurement", "Len": 1},
    {"Field": "Delimiter - 3", "Len": 1, "Display": False},
    {"Field": "Number Of Units (Thousandths)", "Len": 6},
    {"Field": "Delimiter - 4", "Len": 1, "Display": False},
    {"Field": "Unit Cost (Thousandths)", "Len": 7},
    {"Field": "Delimiter - 5", "Len": 1, "Display": False},
    {"Field": "Total Price (Hundredths)", "Len": 8},
    {"Field": "Delimiter - 6", "Len": 1, "Display": False}
]

Standard_map_post_Products = [
    {"Field": "Retrieval Data", "Len": 0, "Max Len": 50, 'FS': 0},
    {"Field": "Authorization Code", "Len": 0, "Max Len": 6, 'FS': 0},
    {"Field": "Pin Data", "Len": 0, "Max Len": 36, 'FS': 0},
    {"Field": "Cash Back Amount", "Len": 0, "Max Len": 8, 'FS': 0},
    {"Field": "Customer Data", "Len": 0, "Max Len": 639, 'FS': 0},
    {"Field": "Miscellaneous Return Data", "Len": 0, "Max Len": 100, 'FS': 0},
    {"Field": "Terminal Features Data", "Len": 0, "Max Len": 8, 'FS': 0},
]

Standard_map_post_EMV_Tags = [
    {"Field": "eParams", "Len": 0, "Max Len": 300, 'FS': 0},
    {"Field": "Protocol Dependent Trailer", "Len": 0}
]

EMV_Fields = [
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
]

fieldTranslations = {
    "Transaction Code": {
        "01": {"Card Type": "Credit", "Trans Type": "Sale"},
        "02": {"Card Type": "Credit", "Trans Type": "Preauthorization"},
        "03": {"Card Type": "Credit", "Trans Type": "Completion"},
        "04": {"Card Type": "Credit", "Trans Type": "Return"},
        "05": {"Card Type": "Credit", "Trans Type": "Void Sale"},
        "06": {"Card Type": "Credit", "Trans Type": "Void Return"},
        "07": {"Card Type": "Credit", "Trans Type": "Card Activation"},
        "08": {"Card Type": "Credit", "Trans Type": "Card Deactivation"},
        "09": {"Card Type": "Credit", "Trans Type": "Card Balance Inquiry"},
        "10": {"Card Type": "Credit", "Trans Type": "Reload/Recharge"},
        "18": {"Card Type": "Credit", "Trans Type": "Issue Card"},
        "19": {"Card Type": "Credit", "Trans Type": "Information update"},
        "11": {"Card Type": "Debit", "Trans Type": "Sale"},
        "12": {"Card Type": "Debit", "Trans Type": "Sale with Cash Back"},
        "13": {"Card Type": "Debit", "Trans Type": "Preauthorization"},
        "14": {"Card Type": "Debit", "Trans Type": "Completion"},
        "15": {"Card Type": "Debit", "Trans Type": "Void Sale"},
        "16": {"Card Type": "Debit", "Trans Type": "Void Sale with Cash Back"},
        "17": {"Card Type": "Debit", "Trans Type": "Return"},
        "21": {"Card Type": "EBT", "Trans Type": "Sale"},
        "22": {"Card Type": "EBT", "Trans Type": "Sale with Cash Back"},
        "24": {"Card Type": "EBT", "Trans Type": "Completion"},
        "25": {"Card Type": "EBT", "Trans Type": "Post Auth Sale with Cash Back"},
        "26": {"Card Type": "EBT", "Trans Type": "Return"},
        "27": {"Card Type": "EBT", "Trans Type": "Balance Inquiry"},
        "41": {"Card Type": "EBT", "Trans Type": "Reversal Sale"},
        "42": {"Card Type": "EBT", "Trans Type": "Reversal Sale with Cash Back"},
        "44": {"Card Type": "EBT", "Trans Type": "Reversal Completion"},
        "45": {"Card Type": "EBT", "Trans Type": "Reversal Post Auth Sale with Cash Back"},
        "46": {"Card Type": "EBT", "Trans Type": "Reversal Return"},
        "31": {"Card Type": "Fleet", "Trans Type": "Sale"},
        "32": {"Card Type": "Fleet", "Trans Type": "Preauthorization"},
        "33": {"Card Type": "Fleet", "Trans Type": "Completion"},
        "34": {"Card Type": "Fleet", "Trans Type": "Return"},
        "35": {"Card Type": "Fleet", "Trans Type": "Void Sale"},
        "36": {"Card Type": "Fleet", "Trans Type": "Void Return"},
        "38": {"Card Type": "Fleet", "Trans Type": "Information Update"},
        "51": {"Card Type": "Loyalty", "Trans Type": "Sale Accumulation"},
        "52": {"Card Type": "Loyalty", "Trans Type": "Void Sale Accumulation"},
        "53": {"Card Type": "Loyalty", "Trans Type": "Return Accumulation"},
        "54": {"Card Type": "Loyalty", "Trans Type": "Void Return Accumulation"},
        "55": {"Card Type": "Loyalty", "Trans Type": "Balance Inquiry"},
    },
    "Account Type": [
        {"Card Type": "Credit", "1": "Visa", "2": "Mastercard", "3": "American Express", "4": "Discover", "8": "Gift Card", "B": "SVS", "E": "PayPal"},
        {"Card Type": "Debit", "0": "Not Specified", "1": "Checking", "2": "Savings"},
        {"Card Type": "EBT", "0": "Not Specified", "1": "Food Stamps", "2": "Cash Benefits"},
        {"Card Type": "Fleet", "1": "WEX", "2": "Voyager", "4": "Visa Fleet", "5": "Mastercard Fleet", "6": "FuelLynk", "8": "MFA Preferred", "9": "Loyalty", "B": "Fleet One", "C": "Fuelman/GasCard", "D": "Alon Fleet"},
        {"Card Type": "Loyalty"},
    ],
    "Entry Method": {
        "0": "Manual Entry",
        "1": "Swiped",
        "2": "Island Card Reader",
        "3": "RFID",
        "4": "Automated Vehicle ID",
        "5": "EMV Contact",
        "6": "EMV Fallback Magstripe",
        "7": "EMV Fallback Voice",
        "8": "EMV Contactless",
        "9": "e-commerce/MOTO"
    }
}






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

        # If the dictionary specifies a Display mode
        if 'Display' in dictArray[i]:

            # Use the dictionaries Display mode
            display = dictArray[i]['Display']

        # Otherwise
        else:

            # Display the field by default.
            display = True

        # If the length is not pre defined or variable
        if length == 0:

            # Check to see if there is a field separator specified
            if 'FS' in dictArray[i]:

                # Since this can return a valueError we have to put it in a try except clause
                try:

                    # Get the index of the next field separator
                    stopPos = message.index(fieldSeparators[dictArray[i]['FS']], startPos)

                # If Value Error is returned
                except ValueError:

                    # The stop position is the end of the message.
                    stopPos = len(message) - 1

                # If the field has a specified max len
                if 'Max Len' in dictArray[i]:

                    # Short hand for the max length
                    max = dictArray[i]['Max Len']

                    # Short hand for the difference between the start and stop position
                    dif = stopPos - startPos

                    # If the difference is greater than the max length
                    if dif > max:

                        # Adjust the stop position to fit within the desired length
                        stopPos -= (dif - max)

                # If this field is to be displayed
                if display:

                    # Grab the message up until the nearest field separator
                    outputDict[str(dictArray[i]['Field'])] = arrayToString(message[startPos:stopPos])

                # Set the start position to be right after the field separator.
                startPos = stopPos + 1

            # Otherwise pull the rest of the message - Primarily used for the protocol dependent trailer
            else:

                # If the end of the message has already been reached somehow
                if startPos == len(message):

                    # Decrement the startPos by one to include the last character.
                    startPos -= 1

                # If this field is to be displayed
                if display:

                    # Grab the rest of the message
                    outputDict[str(dictArray[i]['Field'])] = arrayToString(message[startPos:len(message)])

                # Adjust the startPos as to avoid returning redundant message characters
                startPos = len(message)

                # With the rest of the message grabbed, break the for loop encase the dictionary did not end.
                break

        else:

            # If this field is to be displayed
            if display:

                # Add this element to the output dictionary
                outputDict[str(dictArray[i]['Field'])] = arrayToString(message[startPos:(startPos + length)])

            # Increment the start position
            startPos += length

    return outputDict, message[startPos:len(message)]


def RBS_REQ_Parser(message):

    # Initialize an array to store all of the dictionary results for later printing.
    parsedData = []

    # To begin we need to parse the message using the standard map pre products
    dict, msg = dictionarySplit(Standard_map_pre_Products, message)

    # Append the dictionary to the parsed data array
    parsedData.append(dict)

    # If product Data was provided
    if len(parsedData[0]['Product Information']) > 0:

        # From this we get the total number of products listed off in the message
        products = int(parsedData[0]['Product Information'][0:2])

        # Define the range to iterate over
        msgb = parsedData[0]['Product Information'][3:]

        # We need to parse each of the products out of the list.
        for i in range(products):

            # Parse out the product
            dict, msgb = dictionarySplit(Product_Map, msgb)

            # Append the product to the parsed data array
            parsedData.append(dict)

    # We need to build the rest of the dictionary entries to either include or exclude the EMV Fields
    dict = Standard_map_post_Products

    # If the entry method is an EMV type method
    if int(parsedData[0]['Entry Method']) in range(5, 9):

        # Add the EMV fields into the message
        dict.extend(EMV_Fields)

    # Add the post EMV fields
    dict.extend(Standard_map_post_EMV_Tags)

    # Now that the products have been pulled out of the message we need to grab the rest of the data
    dict, msg = dictionarySplit(dict, msg)

    # We need to append this data to the parsed data array
    parsedData.append(dict)

    return parsedData, msg

def main():
    message = ['02', 'L', 'P', '0', '6', '5', '4', '2', '9', '0', '0', '0', '0', '0', '0', '0', '0', '2', '5', '2', '0', '0', '9', '9', '9', '0', '0', '1', '0', 'A', '0', '7', '5', '9', '1', '3', '0', '5', '0', '2', '0', '2', '0', '0', '4', '0', '8', '0', '0', '1', '0', '4', '4', '0', '2', '0', '2', '0', '0', '9', '2', '1', '1', '1', '3', '3', '1', '3', '0', '0', '2', '4', '0', '0', '0', '0', '6', '2', '1', '0', '9', '4', '8', '0', '0', '0', '0', '0', '0', '2', '6', '8', '=', '3', '0', '1', '0', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1C', '1C', '1C', '1C', '1', '0', '0', '0', '2', '0', '0', '0', '0', '9', '0', '0', '0', '0', '8', '0', '0', '0', '1', 'F', '6', '1', '2', '4', 'A', '9', '0', '6', '2', '7', '2', '8', '6', '8', '2', '1', '1C', '1C', '1C', '1C', '1', '1', '1', 'C', '20', '20', '20', '20', '1C', '5', 'F', '3', '4', '0', '1', '5', '7', '6', '2', '1', '0', '9', '4', '8', '0', '0', '0', '0', '0', '0', '2', '6', '8', 'D', '3', '0', '1', '0', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'F', '9', 'F', '0', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '4', 'A', '0', '0', '0', '0', '0', '0', '3', '3', '3', '0', '1', '0', '1', '0', '8', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '9', 'F', '0', '9', '0', '0', '8', 'C', '9', 'F', '3', '4', '4', '2', '0', '3', '0', '0', '9', 'F', '1', 'E', '3', '0', '3', '0', '3', '0', '3', '0', '3', '1', '3', '5', '3', '5', '3', '1', '9', 'F', '3', '3', '6', '0', '4', '8', '0', '0', '9', 'F', '3', '5', '2', '4', '9', 'F', '4', '1', '0', '0', '0', '0', '0', '0', '1', '6', '9', 'F', '2', '6', '5', 'B', 'D', '8', '7', 'C', '8', 'D', 'B', 'F', '8', '4', 'F', 'A', 'D', 'B', '8', '2', '7', 'D', '0', '0', '9', 'F', '3', '6', '0', '0', 'C', 'B', '9', 'F', '2', '7', '8', '0', '9', 'F', '1', '0', '0', '7', '0', '1', '0', '1', '0', '3', 'A', '0', '0', '0', '0', '0', '0', '1', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '9', 'F', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '7', '5', '0', '0', '9', 'F', '1', 'A', '0', '8', '4', '0', '9', '5', '8', '0', '8', '8', '0', '4', 'C', '0', '0', '0', '5', 'F', '2', 'A', '0', '8', '4', '0', '9', 'A', '2', '0', '0', '9', '2', '1', '9', 'F', '3', 'C', '0', '0', '0', '0', '9', 'C', '0', '0', '9', 'F', '3', '7', '1', 'B', '1', '7', '7', '6', 'F', '1', '9', 'F', '0', '7', 'F', 'F', '0', '0', '8', 'A', '20', '20', '20', '20', '9', 'F', '0', '6', 'A', '0', '0', '0', '0', '0', '0', '3', '3', '3', '0', '1', '0', '1', '0', '8', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '9', 'F', '5', 'B', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', 'S', 'C', 'P', 'B', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '9', 'F', '7', 'C', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '9', 'F', '5', '3', '5', '5', 'F', '2', '4', '3', '0', '1', '0', '3', '1', '9', 'F', '6', 'E', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '03', ';']
    message2 = ['02', 'L', 'P', '0', '6', '5', '4', '2', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '9', '9', '9', '0', '0', '1', '6', '1', '0', '7', '7', '2', '1', '1', '0', '1', '0', '2', '0', '2', '0', '0', '4', '0', '8', '0', '0', '1', '0', '0', '4', '0', '2', '0', '2', '0', '0', '9', '1', '8', '1', '3', '3', '0', '0', '2', '0', '0', '0', '0', '0', '1', '0', '0', '6', '0', '1', '1', '7', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '=', '2', '5', '1', '2', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1C', '0', '1', '-', '4', '5', '0', ':', 'O', ':', 'U', ':', '0', '0', '1', '0', '0', '0', ':', '0', '0', '0', '1', '0', '0', '0', ':', '0', '0', '0', '0', '0', '1', '0', '0', '\\', '1C', '1C', '1C', '1', '0', '0', '0', '2', '0', '0', '0', '0', '9', '0', '0', '2', '1', '2', '0', '0', '1', '0', '1', '4', '4', '2', '9', '5', '3', '8', 'F', '8', '9', 'B', '4', 'E', 'D', '3', 'D', '1C', '1C', '1C', '1C', '1', '1', '1', 'C', '20', '20', '20', '20', '03', '~']

    array, msg = RBS_REQ_Parser(message2)

    for i in range(len(array)):
        for key,value in array[i].items():
            print(str(key) + ': ' + str(value))

    print(str(msg))

if __name__ == "__main__":
    main()