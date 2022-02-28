# This class represents the medical procedure being performed

class Procedure:

# __init__ to accept arguments for pro_name, date, practitioner,
# charge, patient_id

    def __init__(self, pro_name, date, practitioner, charge, patient_id):
        self.__pro_name = pro_name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        self. __patient_id = patient_id

#### set_methods ####

# set_pro_name
    def set_pro_name(self, pro_name):
        self.__pro_name = pro_name

#set_date
    def set_date(self, date):
        self.__date = date

#set_practitioner
    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

#set_charge
    def set_charge(self, charge):
        self.__charge = charge

#set_id 
    def set_id(self, patient_id):
        self.__patient_id = patient_id

#### get_methods ####
#get_pro_name
    def get_pro_name(self):
        return self.__pro_name

#get_date
    def get_date(self):
        return self.__date

#get_practitioner
    def get_practitioner(self):
        return self.__practitioner

#get_charge
    def get_charge(self):
        return self.__charge

#get_id
    def get_id(self):
        return self.__patient_id