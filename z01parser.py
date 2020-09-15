import sys

Standard_Map_Dict = {
    # 1001
    "Company_Identifier": 4,
    "Terminal_Class_ID": 1,
    "Terminal_Format_Level": 2,
    "Multiple_Inquiry_Flag": 1,
    "Response_Format_Code": 2,
    "Request_Format_Code": 2,
    "Transaction_Type": 2,
    "Sequence_Number": 6,
    "Date": 6,
    "Time": 4,
    "Terminal_Location_ID": 15,  # Named Terminal_ID in spec's map info
    "Company_ID": 4,
    "Unique_Device_ID": 4,  # This is not always present
    "Account_Number": 0,  # Variable Length
    "Field_Sep_Track2": 1,
    "Exp_Date_Track2:": 4,
    "Disc_Data_Track2": 0,  # Variable_Length
    "Card_Use_Type": 1,  # Adding these to standard map to reduce replication
    "Total_Amount": 7,  # Adding these to standard map to reduce replication
}

Standard_Map_No_Unique_Dict = {
    # 1000
    "Company_Identifier": 4,
    "Terminal_Class_ID": 1,
    "Terminal_Format_Level": 2,
    "Multiple_Inquiry_Flag": 1,
    "Response_Format_Code": 2,
    "Request_Format_Code": 2,
    "Transaction_Type": 2,
    "Sequence_Number": 6,
    "Date": 6,
    "Time": 4,
    "Terminal_Location_ID": 15,  # Named Terminal_ID in spec's map info
    "Company_ID": 4,
    "Account_Number": 0,  # Variable Length
    "Field_Sep_Track2": 1,
    "Exp_Date_Track2:": 4,
    "Disc_Data_Track2": 0,  # Variable_Length
    "Card_Use_Type": 1,  # Adding these to standard map to reduce replication
    "Total_Amount": 7,  # Adding these to standard map to reduce replication
}

Terminal_Diagnostics_Dict = {
    # 999
    "Number_Dial_Attempts": 1,
    "Terminal_Reason_Code": 2,
    "Host_Dialed": 1,
}

Terminal_Diagnostics_Plus_Dict = {
    # 998
    "Number_Dial_Attempts": 1,
    "Terminal_Reason_Code": 2,
    "Host_Dialed": 1,
    "Folio_Area_Tag": 2,
    "Purchase_ID_Format_Code": 1,
    "Reserved_2": 39,
    "Field_Separator_2": 1,
    "AVS_Area_Tag": 2,
    "AVS_Information": 0,
    "Field_Separator_3": 1,
    "Variable_Data_Area_Tag": 2,
}

Discretionary_Data_Dict = {
    # 997
    "Client_Discretionary_Data": 0,
    "Field_Separator": 1,
    "Field_Separator_Holder": 1,
}

Addendum_Tag_Data_Dict = {
    # 996
    "Field_Separator_2": 1,
    "Addendum_Data_Length": 4,
    "Number_Tag_IDs": 2,
    "Tag_ID": 3,
    "Tag_Data_Length": 4,
    "Tag_Data": 0,
    "Field_Separator_Holder_2": 1,
}

z01_Request_Field = {
    "C201": {
        "Standard_Map_No_Unique": Standard_Map_No_Unique_Dict,
        "Currency_Code": 3,
        # Specific Information
        "Terminal_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Term_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "D301": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "D401": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Terminal_Type": 1,
        "PoS_Data_Codes": 12,
        "Authorization_Response_Code": 2,
        "Reserved": 20,
        "Addendum_Presence_Ind": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "C103": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Currency_Code": 3,
        "Terminal_Type": 1,
        "Authorization_Number": 6,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "C203": {
        "Standard_Map_No_Unique": Standard_Map_No_Unique_Dict,
        "Currency_Code": 3,
        # Specific Information
        "Authorization_Number": 6,
        "Terminal_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Retrieval_Ref_Num": 12,
        "Term_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "D003": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Reserved": 8,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "B205": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "CVV2_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Authorisation_Response_Code": 2,
        "Reserved": 4,
        "Goods_Sold": 1,
        "Reserved_2": 33,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # End of Term Diagnostics
        "Reserved_3": 19,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field Separator": 1,
        "Variable_Data_Area_Tag": 2,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "F005": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        "Good_Sold": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # End of Terminal Diagnostics
        "Folio_Area_Tag": 2,
        "Purch_ID_Format_Code": 1,
        "Reserved": 26,
        "Field_Separator": 1,
        "Reserved_2": 18,
        "Field_Separator_2": 1,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field Separator": 1,
        "Variable_Data_Area_Tag": 2,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "F205": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "CVV2_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Filler": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # End of Terminal Diagnostics
        "Folio_Area_Tag": 2,
        "Purch_ID_Format_Code": 1,
        "Reserved": 26,
        "Field_Separator": 1,
        "Reserved_2": 18,
        "Field_Separator_2": 1,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,  # Variable Length
        "Field Separator": 1,
        "Variable_Data_Area_Tag": 2,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "G205": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Authorisation_Response_Code": 2,
        "Reserved": 4,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Reserved_2": 32,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "NT05": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Settlement_Indicator": 1,
        "Reserved": 2,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "NO05": {
        "Standard_Map_Dict": Standard_Map_Dict,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "N205": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Credit_Plan": 5,
        "Offered_Down_Payment": 7,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "N905": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Card_Type": 4,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P005": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P505": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P605": {
        "Standard_Map_Dict": Standard_Map_Dict,
        # This map appears identical to the P5...?
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P705": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "PO_Number": 15,
        "Business_Date": 6,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P805": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_Set": 2,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        "Authorisation_Response_Code": 2,
        "Settlement_Indicator": 1,
        "Reserved": 17,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "W705": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Vehicle_Card_Number": 5,
        "Addendum_Presence_Indicator": 1,
        "Available Products": 1,
        "Reserved": 1,
        "Unit_Measure": 1,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "B211": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobil_Device_Indicator": 1,
        "Reserved": 66,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "E311": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Currency_Code": 3,
        "EBT_Type": 2,
        "Terminal_Type": 1,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Voucher_Number": 15,
        "Reserved": 10,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "G211": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Tax_Code": 6,
        "Customer_Code": 25,
        "Surcharge_Amount": 6,
        "PoS_Data_Code": 12,
        "Mobile_Device_Indicator": 1,
        "Terminal_Type": 1,
        "Reserved": 65,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "N811": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P011": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P511": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P611": {
        "Standard_Map_Dict": Standard_Map_Dict,
        # Again its the same as P5..?
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P711": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "PO_Number": 15,
        "Date": 6,
        "Invoice_Total": 12,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P811": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_Set": 2,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Reserved": 1,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        "Reserved_2": 20,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "W711": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Authorisation_Number": 6,
        "Authorization_Type": 1,
        "Terminal_Type": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Authorization_Amount": 7,
        "Purchase_Device_Seq_Number": 5,
        "Addendum_Presence_Indicator": 1,
        "Reserved": 2,
        "Unit_Measure": 1,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "B213": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "CVV2_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Purchase_Type": 1,
        "Terminal_Type": 1,
        "Cash_Over_Amount": 6,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Goods_Sold": 1,
        "Reserved": 3,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        "AVS_Area_Tag": 2,
        "AVS_Information": 0,
        "Field_Separator": 1,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "C213": {
        "Standard_Map_No_Unique": Standard_Map_No_Unique_Dict,
        "Currency_Code": 3,
        # Specific Information
        "Terminal_Type": 1,
        "Sale_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Usage_Code": 1,
        "Terminal_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "D313": {
        "Standard_Map_Dict": Standard_Map_Dict,
        # Same as 01 version..?
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "D413": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Terminal_Type": 1,
        "PoS_Data_Codes": 12,
        "Reserved": 21,
        "Addendum_Presence_Ind": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "E313": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Currency_Code": 3,
        "EBT_Type": 2,
        "Terminal_Type": 1,
        "Purchase_Type": 1,
        "KSN": 16,
        "Pin_Block": 16,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Reserved": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "F013": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Mail_Indicator": 1,
        "Terminal_Type": 1,
        "Reserved": 2,
        # Term Diagnostics Plus
        "Terminal_Diagnostics_Plus": 0,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "F213": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "CVV2_Presence_Indicator": 1,
        "CVV2": 4,
        "Moto_Indicator": 1,
        "Purchase_Type": 1,
        "Terminal_Type": 1,
        "Filler": 1,
        # Term Diagnostics Plus
        "Terminal_Diagnostics_Plus": 0,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "G213": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Tax_Amount": 6,
        "Customer_Code": 25,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Reserved": 65,
        "Addendum_Presence_indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "N013": {
        "Standard_Map_Dict": Standard_Map_Dict,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "N213": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Credit_Plan": 5,
        "Offered_Down_Payment": 7,
        "Product_Code_1": 4,
        "Product_Code_2": 4,
        "Product_Code_3": 4,
        "Product_Code_4": 4,
        "Product_Code_5": 4,
        "Unused": 11,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P013": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Tax_Code": 6,
        "Customer_Code": 25,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P513": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P613": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P713": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Odometer": 6,
        "Driver": 6,
        "PO_Number": 15,
        "Business_Date": 6,
        "Invoice_Total": 12,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "P813": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Odometer": 6,
        "Driver": 6,
        "Control_Number": 4,
        "Vehicle_Number": 6,
        "Fuel_Measure": 1,
        "Fuel_Service_Type": 2,
        "Product_Code_Set": 2,
        "Surcharge_Amount": 6,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Chip_Condition_Code": 1,
        "Product_Code_1": 2,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Product_Code_2": 2,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Product_Code_3": 2,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Product_Code_4": 2,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Product_Code_5": 2,
        "Quantity_5": 7,
        "Amount_5": 7,
        "Product_Code_6": 2,
        "Quantity_6": 7,
        "Amount_6": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        "Reserved": 20,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "W713": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Terminal_Type": 1,
        "Fuel_Service_Type": 2,
        "Prompt_Data": 43,
        "Purchase_Device_Seq_Number": 5,
        "Addendum_Presence_Indicator": 1,
        "Reserved": 2,
        "Unit_Measure": 1,
        "Product_Code_1": 3,
        "Quantity_1": 7,
        "Amount_1": 7,
        "Unit_Measure_2": 1,
        "Product_Code_2": 3,
        "Quantity_2": 7,
        "Amount_2": 7,
        "Unit_Measure_3": 1,
        "Product_Code_3": 3,
        "Quantity_3": 7,
        "Amount_3": 7,
        "Unit_Measure_4": 1,
        "Product_Code_4": 3,
        "Quantity_4": 7,
        "Amount_4": 7,
        "Sales_Tax": 5,
        "Discount": 5,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "B230": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "PoS_Data_Codes": 12,
        "Mobile_Device_Indicator": 1,
        "Reserved": 1,
        "Reversal_Reason": 1,
        "Reserved_2": 40,
        "Addendum_Presence_Indicator": 1,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
        # Addendum_Tag_Data
        "Addendum_Tag_Data": Addendum_Tag_Data_Dict,
    },
    "C230": {
        "Standard_Map_No_Unique": Standard_Map_No_Unique_Dict,
        "Currency_Code": 3,
        # Specific Information
        "Terminal_Type": 1,
        "Card_Type": 4,
        "Employee_ID": 8,
        "Shift_Number": 3,
        "Control_Number": 6,
        "Access_Code": 4,
        "Term_Reference_Number": 12,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
    "??30": {
        "Standard_Map_Dict": Standard_Map_Dict,
        "Currency_Code": 3,
        "EBT_Type": 2,
        "Cash_Back_Amount": 6,
        "Convenience_Fee_Amount": 6,
        "Reserved": 10,
        # Term Diagnostics
        "Terminal_Diagnostics": Terminal_Diagnostics_Dict,
        # Client Disc Data
        "Discretionary_Data": Discretionary_Data_Dict,
    },
}

#####################

def user_input_formatting(user_Input_List):
    # Entry point, takes multi-line input that needs formatting
    print("Enter string, press 'ctrl+d' when done to input")
    user_Input = str(sys.stdin.readlines())  # Reads multi-line string input and assigns to variable

    # Turns input into list of strings
    user_Input = user_Input.split(",")
    for string in user_Input:
        string = string.partition("INF:")[2]
        string = string.partition("\\n")[0]
        string = string.replace("  ", " ")
        string = string.replace("   ", "")
        string = string.replace("']", "")
        temp_list = string.split(" ")
        for i in temp_list:
            user_Input_List.append(i)

    print(user_Input_List)

    return user_Input_List


######################


def map_selection_func(user_input):
    # Pulls the map type needed from the fully formatted list of single byte strings
    print(user_input)
    request_format_code = "".join(user_input[10:12])
    transaction_type = "".join(user_input[12:14])
    map_selection = request_format_code + transaction_type
    print(map_selection)
    return map_selection


########################
# Loops through the map bases on request type and expands the data using template maps to form a new 'fully expanded' map
def dict_maker(z01_request_type):
    created_dictionary = {}
    template_dicts = [Standard_Map_Dict, Standard_Map_No_Unique_Dict, Terminal_Diagnostics_Dict,
                      Terminal_Diagnostics_Plus_Dict, Discretionary_Data_Dict, Addendum_Tag_Data_Dict]
    for key, value in z01_Request_Field[z01_request_type].items():
        if value in template_dicts:
            for key_2, value_2 in value.items():
                created_dictionary.update({key_2: value_2})
            continue
        created_dictionary.update({key: value})
    # pprint.pprint(created_dictionary, sort_dicts=False)
    return created_dictionary


# returns a map that can be iterated over to actually parse out the map data


########################

# Pass map_selection to auto determine which map type to parse
# Sorts data by Key:Value in specified sub-dictionary from the use_map and cuts out string values by Value in dict
def request_parser(created_dict, user_Input_List):
    #pprint.pprint(created_dict, sort_dicts=False)
    print("".join(user_Input_List))

    for x, y in created_dict.items():
        has_field_separator = ["Account_Number", "AVS_Information", ]
        field_separators = ["1C", "1E", "="]
        card_use_type_values = ["C", "B", "F"]
        try:
            if x in has_field_separator:  # This catches the special dict entries that end in a field sep
                for char in user_Input_List:  # Will find any value of 0 that isn't in the above loop
                    if char in field_separators:
                        end_index = (user_Input_List.index(char))
                        print(x + ": " + "".join(user_Input_List[:end_index]))
                        user_Input_List = user_Input_List[end_index:]
                        break  # do not continue to loop through index looking for characters
            elif x == "Tag_Data":
                end_index = user_Input_List.index("1E")
                emv_tags = ("".join(user_Input_List[:end_index]))
                print(x + ": " + emv_tags)
                user_Input_List = user_Input_List[end_index:]
            elif x == "Client_Discretionary_Data":
                end_index = user_Input_List.index("=")
                discretionary_data = ("".join(user_Input_List[:end_index]))
                print(x + ": " + discretionary_data)
                user_Input_List = user_Input_List[end_index:]

            else:
                if y == 0:  # This is a bit sloppy. The only thing this should find is Disc_Data_Track2 but,
                    for char in user_Input_List:  # Will find any value of 0 that isn't in the above loop
                        if char in card_use_type_values:
                            end_index = (user_Input_List.index(char))
                            print(x + ": " + "".join(user_Input_List[:end_index]))
                            user_Input_List = user_Input_List[end_index:]
                            break  # do not continue to loop through index looking for characters
                else:  # if not a special dict value
                    end_index = 0
                    end_index += y
                    print(x + ": " + "".join(user_Input_List[:end_index]))
                    user_Input_List = user_Input_List[end_index:]
        except ValueError:
            pass

def exampleOutputBuilder(messageDict):

    # Initialize the output Dict.
    outputDict = {
        'KeyInfo': {
            'SequenceNumber': '',
            'MessageType': '',
            'ApprovalNumber': '',
            'CardPan': '',
            'Date': '',
            'Time': '',
            'TagData': '',
        }
        , 'FullMessage': messageDict
    }

    # An example as to how to set values in the KeyInfo section.
    outputDict['KeyInfo']['Date'] = messageDict['Date']

    # An example of for looping this information if it is phrased the same in the message Dict.
    for key in outputDict['KeyInfo']:

        # If the tag exists in the messageDict
        if key in messageDict.items():

            # Set the tag in the outputDict
            outputDict['KeyInfo'][key] = messageDict[key]

    # Make any other necessary changes to the dict and return the outputDict.

    return outputDict


####################
# MAIN
#user_input_formatting()
#request_parser(dict_maker(map_selection_func(user_input_formatting())))
