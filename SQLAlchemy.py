from sqlalchemy import Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id, name):
        self.id = id
        self.name = name
        


class Student_subject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student = relationship("Student")
    subject = relationship("Subject")

    def __init__(self, id, student_id, subject_id):
        self.id = id
        self.subject_id = subject_id
        self.student_id = student_id


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='students',
        user='postgres',
        password='admin123',
        port=5432,
    )
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

# student1 = Student(101, "Sofia", 21)
# student2 = Student(102, "Kyrylo", 25)
# student3 = Student(103, "Dmytro", 19)
# student4 = Student(104, "Viktoria", 22)
# student5 = Student(105, "Sanji", 23)

# session.add(student1)
# session.add(student2)
# session.add(student3)
# session.add(student4)
# session.add(student5)
# session.commit()

# subject1 = Subject(1001, "English")
# subject2 = Subject(2001, "Math")
# subject3 = Subject(3001, "History")

# session.add(subject1)
# session.add(subject2)
# session.add(subject3)
# session.commit()

# student_subject1 = Student_subject(1, 101, 1001)
# student_subject2 = Student_subject(2, 102, 1001)
# student_subject3 = Student_subject(3, 103, 1001)
# student_subject4 = Student_subject(4, 104, 1001)
# student_subject5 = Student_subject(5, 104, 2001)
# student_subject6 = Student_subject(6, 101, 2001)
# student_subject7 = Student_subject(7, 105, 2001)
# student_subject8 = Student_subject(8, 104, 3001)
# student_subject9 = Student_subject(9, 105, 3001)
# student_subject10 = Student_subject(10, 102, 3001)

# session.add(student_subject1)
# session.add(student_subject2)
# session.add(student_subject3)
# session.add(student_subject4)
# session.add(student_subject5)
# session.add(student_subject6)
# session.add(student_subject7)
# session.add(student_subject8)
# session.add(student_subject9)
# session.add(student_subject10)
# session.commit()

results = (
    session.query(Student)
    .join(Student_subject, Student_subject.student_id == Student.id)
    .join(Subject, Student_subject.subject_id == Subject.id)
    .filter(Subject.name == "English")
    .all()
)

for result in results:
    print(result.name)

session.close()