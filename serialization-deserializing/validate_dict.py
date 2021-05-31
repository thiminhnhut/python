from marshmallow import Schema, ValidationError, fields


class DictSchema(Schema):
    command = fields.Integer(required=True,
                             validate=lambda command: command == 1)
    clientID = fields.String(required=True,
                             validate=lambda clientID: len(clientID) == 6)


def main():
    data = dict(command=1, clientID='123456')

    try:
        DictSchema().load(data)
        print("Valid success!")
    except ValidationError as error:
        print(error.messages)


if __name__ == '__main__':
    main()
