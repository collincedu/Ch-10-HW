class Patient:

# __init__ method for accepting ID, name, address
# phone, veteran_status
# accessor methods only

    def __init__(self, patient_id, name, address, phone, veteran_status):
        self.__patient_id = patient_id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status

# get_id method to return the patient id

    def get_id(self):
        return self.__patient_id

#get_name method

    def get_name(self):
        return self.__name

#get_address method

    def get_address(self):
        return self.__address

#get_phone method

    def get_phone(self):
        return self.__phone

#get_veteran_status method

    def get_veteran_status(self):
        return self.__veteran_status

def __str__(self):
    return "Name: " + self.__name + "\n" + "Address: " + self.__address
    + "\n" + "Phone:" + self.__phone
    
    