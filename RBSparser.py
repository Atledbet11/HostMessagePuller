
###################################################
# Project: RBS Parser
# Description: Parse an RBS host message
#   to make it easy to read without manual work
# Built: Tate Ledbetter - 2020
###################################################

Standard_map_pre_Products = {
    "Protocol Dependent Header": 0,
    "Application Type": 2,
    "Processing Mode": 1,
    "Message Format Version": 1,
    "Terminal Identification": 24,
    "Device Identifier": 1,
    "Message Sequence Number": 4,
    "Transaction Code": 2,
    "Account Type": 1,
    "Entry Method": 1,
    "Request Type": 1,
    "Batch/Shift Number": 11,
    "Transaction Sequence Number": 4,
    "Local Transaction Date": 8,
    "Local Transaction Time": 6,
    "Total Amount": 8,
    "Track Data": 0,
    "Total Number of Products": 2
}

Product_Map = {
    "Product Code": 3,
    "Delimiter": 1,
    "Service Code": 1,
    "Delimiter": 1,
    "Unit Measurement": 1,
    "Delimiter": 1,
    "Number Of Units (Thousandths)": 6,
    "Delimiter": 1,
    "Unit Cost (Thousandths)": 7,
    "Delimiter": 1,
    "Total Price (Hundredths)": 8,
    "Delimiter": 1
}

Standard_map_post_Products = {
    "Retrieval Data": 0,
    "Authorization Code": 0,
    "Pin Data": 0,
    "Cash Back Amount": 0,
    "Customer Data": 0,
    "Miscellaneous Return Data": 0,
    "Terminal Features Data": 0,
    "Application PAN Seq": 6,
    "Track 2 Equivalent Data": 40,
    "Other Amount": 16,
    "Dedicated File Name": 34,
    "Application Version Number": 8,
    "Cardholder Verify Result": 10,
    "Interface Device Serial Number": 20,
    "Terminal Capabilities": 10,
    "Terminal Type": 6,
    "Transaction Sequence Counter": 12,
    "Application Cryptogram": 20,
    "Application Interchange Profile": 6,
    "Application Transaction Counter": 8,
    "Cryptogram Info Data": 6,
    "Issuer Application Data": 68,
    "Amount Authorized": 16,
    "Term Country Code": 8,
    "Term Verification Results": 12,
    "Trans Currency Code": 8,
    "Trans Date": 8,
    "Trans Reference Currency Code": 8,
    "Transaction Type": 4,
    "Unpredictable Number": 12,
    "Application Usage Control": 8,
    "Auth Response Code": 6,
    "Application Identifier": 36,
    "Issuer Script Result": 14,
    "Secondary Pin Block": 78,
    "Obsolete": 12,
    "Customer Exclusive Data": 24,
    "Transaction Category Code": 5,
    "Application Expiration Date": 10,
    "Third Party Data": 68,
    "eParams": 0,
    "Protocol Dependent Trailer": 3
}

def RBS_Parser(message):
    print('Moo')