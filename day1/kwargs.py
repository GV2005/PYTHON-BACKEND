def doctor_info(**data):
    print(data)
    print(data["name"])
    print(data["specialization"])

doctor_info(name="Ravi", specialization="Cardiology", exp=10)