fr_all_students=open("file_operations\\all_students.txt")
fr_passed_students=open("file_operations\\passed_students.txt")
fw_failed_students=open("file_operations\\failed_students.txt","w")

all_students={name.rstrip("\n") for name in fr_all_students}
passed_students={name.rstrip("\n") for name in fr_passed_students}
failed_students=all_students.difference(passed_students)

for student in failed_students:
    fw_failed_students.write(student+'\n')


