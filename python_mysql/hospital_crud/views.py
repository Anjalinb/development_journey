from mysql import connector

class PatientListCreateRetreiveUpdateDelete:

    def __init__(self,user=None,password=None):
        if user==None or password==None:
            raise Exception("username and password required")

        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database='hospital_db'
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):
        db_cols=("patient_name","phone_number","assigned_doctor","department","appointment_date","status","consultation_fee")
        difference=set(db_cols).difference(kwargs.keys())
        if difference:
            raise Exception(f"{difference} required")

        col_str=",".join(db_cols)
        query=f"insert into patients ({col_str}) values (%s,%s,%s,%s,%s,%s,%s)"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been inserted")

    def get(self):
        query="select * from patients"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for r in records:
            print(r)

    def retrieve(self,patient_name=None,phone_number=None):
        
        query=f"select * from patients where patient_name=%s or phone_number=%s"
        values=(patient_name,phone_number)

        self.cursor.execute(query,values)
        records=self.cursor.fetchone()
        print(records)

    def put(self,patient_id=None,**kwargs):
        placeholder=""
        for k in kwargs.keys():
            placeholder+= k+"=%s,"
        placeholder=placeholder.rstrip(",")
        query=f"update patients set {placeholder} where patient_id=%s"
        values=list(kwargs.values())
        values.append(patient_id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated")

    def delete(self,patient_id = None):

        query = "delete from patients where patient_id = %s "

        values = (patient_id,)

        self.cursor.execute(query,values)

        self.connection.commit()

        print(".........patient record has been deleted.........")

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder += k + "=%s and "

        place_holder=place_holder.rstrip("and ")

        query = f"select * from patients where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        patient_list = self.cursor.fetchall()

        if patient_list:

            for p in patient_list:

                print(p)

        else:

            print("...NO PATIENT RECORDS.....")

    def summary(self):

        fee_query = " select  sum(consultation_fee) as total_fee from patients  "

        self.cursor.execute(fee_query)

        fee = self.cursor.fetchall()

        print("total consultation fee = ",fee)

        count_query = "select assigned_doctor,count(patient_name) as total_appoinment from patients group by assigned_doctor"

        self.cursor.execute(count_query)

        count = self.cursor.fetchall()

        print(count)
            


patient=PatientListCreateRetreiveUpdateDelete(user="root",password="root")
# print(patient.connection)
# patient.post(
#     patient_name="Arun Kumar",
#     phone_number="9876543210",
#     assigned_doctor="Dr. Rahul Menon",
#     department="Cardiology",
#     appointment_date="2026-09-08",
#     status="Pending",
#     consultation_fee=800.00
# )

# patient.post(
#     patient_name="Anjali Suresh",
#     phone_number="9123456780",
#     assigned_doctor="Dr. Priya Nair",
#     department="Dermatology",
#     appointment_date="2026-09-08",
#     status="Completed",
#     consultation_fee=600.00
# )

# patient.post(
#     patient_name="Vishnu Raj",
#     phone_number="9847123456",
#     assigned_doctor="Dr. Sandeep Kumar",
#     department="Orthopedics",
#     appointment_date="2026-09-09",
#     status="Pending",
#     consultation_fee=750.00
# )

# patient.post(
#     patient_name="Meera Joseph",
#     phone_number="9654321789",
#     assigned_doctor="Dr. Anitha Thomas",
#     department="Pediatrics",
#     appointment_date="2026-09-09",
#     status="Cancelled",
#     consultation_fee=500.00
# )

# patient.post(
#     patient_name="Rahul Krishnan",
#     phone_number="8899123456",
#     assigned_doctor="Dr. Arun Das",
#     department="Neurology",
#     appointment_date="2026-09-10",
#     status="Pending",
#     consultation_fee=1200.00
# )

# patient.post(
#     patient_name="Fathima Nazeer",
#     phone_number="9034567891",
#     assigned_doctor="Dr. Shalini Menon",
#     department="Gynecology",
#     appointment_date="2026-09-10",
#     status="Completed",
#     consultation_fee=900.00
# )

# patient.post(
#     patient_name="Akhil Mohan",
#     phone_number="9988776655",
#     assigned_doctor="Dr. Vivek Kumar",
#     department="General Medicine",
#     appointment_date="2026-09-11",
#     status="Pending",
#     consultation_fee=400.00
# )

# patient.get()
# patient.retrieve(patient_name="akhil mohan")
patient.put(patient_id=2,status="pending")
