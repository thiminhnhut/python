from marshmallow import Schema, fields, post_load, ValidationError, EXCLUDE


class Course:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f'Student(id={self.id},name={self.name})'


class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f'Student(id={self.id},name={self.name}, email={self.email})'


class StudentSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    email = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_student(self, data, **kwargs):
        return Student(**data)


class CourseSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)


def serialization():
    print('Serialization')
    student = Course(id=1, name='Thi Minh Nhut', price=1000)
    try:
        result = CourseSchema().dump(student)
        print(result)
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)


def deserializing():
    print('Deserializing')
    data = dict(id=1, name='Thi Minh Nhut', email='thiminhnhut@gmail.com')
    try:
        student = StudentSchema().load(data, unknown=EXCLUDE)
        print(student)
    except ValidationError as error:
        print(error.messages)
        print(error.valid_data)


if __name__ == '__main__':
    # deserializing()
    serialization()
