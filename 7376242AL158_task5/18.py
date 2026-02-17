class Patient:
    def __init__(self, patient_id, name, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis
    def calculate_cost(self):
        pass
    def display_details(self):
        print("Name:", self.name)
        print("Total Treatment Cost: ₹", self.calculate_cost())
class InPatient(Patient):
    def __init__(self, patient_id, name, diagnosis, days_admitted):
        super().__init__(patient_id, name, diagnosis)
        self.days_admitted = days_admitted

    def calculate_cost(self):
        daily_charge = 2000
        treatment_charge = 5000
        return (self.days_admitted * daily_charge) + treatment_charge
class OutPatient(Patient):
    def calculate_cost(self):
        consultation_fee = 500
        return consultation_fee
class EmergencyPatient(Patient):
    def calculate_cost(self):
        emergency_charge = 3000
        treatment_charge = 7000
        return emergency_charge + treatment_charge
p1 = InPatient(101, "Rahul", "Surgery", 3)
p2 = OutPatient(102, "Anita", "Fever")
p3 = EmergencyPatient(103, "Vikram", "Accident")
p1.display_details()
p2.display_details()
p3.display_details()
