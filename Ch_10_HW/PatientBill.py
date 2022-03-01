import PatientClass as Pat
import ProcedureClass as Pro

DISCOUNT = .6

def main():

# header
    print("*** Patient Bill ***")

# patient object
    patient_1 = Pat.Patient(1, "Matt Jones", "123 Mainst, Waco TX 76706", "254-555-7415", True)

    print("Name:", patient_1.get_name())
    print("Address:", patient_1.get_address())
    print("Phone:", patient_1.get_phone())

# procedure object
    procedure_1 = Pro.Procedure("Pysical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    procedure_2 = Pro.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    procedure_3 = Pro.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

#procedure 1
    print("\n")
    print("Procedure:", procedure_1.get_pro_name())
    print("Date:", procedure_1.get_date())
    print("Practitioner:", procedure_1.get_practitioner())
    print("Charge: $", format(procedure_1.get_charge(), ',.2f'), sep = '')

#procedure 2
    print("\n")
    print("Procedure:", procedure_2.get_pro_name())
    print("Date:", procedure_2.get_date())
    print("Practitioner:", procedure_2.get_practitioner())
    print("Charge: $", format(procedure_2.get_charge(), ',.2f'), sep = '')

#Total
    total = format((procedure_1.get_charge() + procedure_2.get_charge()) * DISCOUNT, ',.2f')
    print("Total Charges: $", total, sep = '')


main()