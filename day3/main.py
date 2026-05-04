import appointment
import doctor
import patient

patient1=patient.Patient("0a7","hari",34)
doctor1=doctor.Doctor("001","kelvin","othology")

appointment1=appointment.Appointment("071",patient1,doctor1,"10/12/2026")


appointment1.show_details()
