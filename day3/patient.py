class Patient:
    hospital_name="KMS Hospital"

    def __init__(self,patient_id,name,age):
        self.patient_id=patient_id
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.patient_id} admitted in {self.hospital_name}"
    
    def introduce(self):
        return f"Patient name {self.name} of age {self.age}"