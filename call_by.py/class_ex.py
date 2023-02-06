class School:
    name="Dayamayi"
    def school_name(cls):
        print("School name is :", cls.name)

# create class method
School.school_name=classmethod(School.school_name)

# call class method
School.school_name()