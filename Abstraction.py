# Task1:
# Define Abstract base Class
from abc import ABC, abstractmethod

class BillingRecord(ABC):
    @abstractmethod
    def get_bill(self):
        """
        Abstract method to get the billing details.
        Subclasses must implement this method.
        """
        pass

    @abstractmethod
    def update_bill(self, amount):
        """
        Abstract method to update the billing details.
        Subclasses must implement this method.
        """
        pass

# Task2:
# Define Concrete Classes
class PatientBilling(BillingRecord):
    def __init__(self, patient_id, patient_name, billing_amount=0):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.billing_amount = billing_amount

    def get_bill(self):
        return{
            'Patient ID': self.patient_id,
            'Patient Name': self.patient_name,
            'Billing Amount':f"₹{self.billing_amount:.2f}"
        }
    def update_bill(self, amount):
        if amount > 0:
            self.update_amount += amount
            print(f"Billing amount updated by ₹{amount:.2f}. New amount is ₹{self.billing_amount:.2f}.")
        else:
            print("Amount to update must be positive.")

# Task3:
# Use to concrete class
if __name__ =="__main__":
    # create a billing record for a patient
    patient_bill = PatientBilling(
        patient_id= "p001",
        patient_name= "Ramar Bose",
        billing_amount= "150.00"
    )
    # print initial bill details
    print("Initial Bill Details:")
    print(patient_bill.get_bill())

    # Update billing amount
    patient_bill.update_bill(50.00)

    # print updated bill details
    print("\nUpdate Bill Details:")
    print(patient_bill.get_bill())
