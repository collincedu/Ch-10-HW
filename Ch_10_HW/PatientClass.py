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

#### set_methods ####
# set_id mehtod will accept the argument for the patients id

    def set_id(self, patient_id):
        self.__patient_id = patient_id

# set_name method
    
    def set_name(self, name):
        self.__name = name

# set_address method

    def set_address(self, address):
        self.__address = address

# set_phone method

    def set_phone(self, phone):
        self.__phone = phone 

#set_veteran_status method

    def set_veteran_status(self, veteran_status):
        self.__veteran_status = veteran_status

#### get_methods ####
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