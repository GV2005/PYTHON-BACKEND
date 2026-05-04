class Appointment:

    def __init__(self,appointment_id,patient,doctor,date):
        self.appointment_id=appointment_id
        self.patient=patient
        self.doctor=doctor
        self.date=date

    def show_details(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient: {self.patient.name}")
        print(f"Doctor: {self.doctor.name}")
        print(f"Specialization: {self.doctor.specialization}")
        print(f"Date: {self.date}")