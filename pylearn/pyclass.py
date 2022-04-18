from __future__ import annotations
import dataclasses


class Student:
    def __init__(self, first_name: str, last_name: str, age: int, person_id: int):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.person_id: int = person_id

    def __repr__(self):
        repr_str = "Student(first_name='{}', last_name='{}', age={}, person_id={})"
        formatted = repr_str.format(self.first_name, self.last_name, self.age, self.person_id)
        return formatted


student1 = Student(first_name="Abc", last_name="Def", age=47, person_id=545645)
# print(student1.person_id)
# print(student1.last_name)
print("Student 1 Class")
print(student1)

test_str = str(student1)
print("Student 3 Class")
student3 = eval(test_str)
student3.age = student3.age + 3
print(student3)


@dataclasses.dataclass
class Student2:
    first_name: str
    last_name: str
    age: int
    personal_id: int


student2 = Student2("Abc", "Def", 47, 545645)
print("Student 2 Class")
print(student2)
new_evaled = eval(str(student2))

print("Afer eval")
new_evaled.age = new_evaled.age + 3
print(new_evaled)

name = "asdf asdf asdf"
name_list = ["asdf", "asdf", "asdf"]
print(len(name))
print(len(name_list))