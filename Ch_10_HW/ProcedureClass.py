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

def __str__(self):
    return "Procedure: " + self.__pro_name + '\n' + "Date: " + self.__date +'\n' + "Practitioner: " + self.__practitioner + '\n' + "Charge:  $" + format(self.__charge, ',.2f')