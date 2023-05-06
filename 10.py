from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def validate(self):
        raise NotImplementedError("Validation logic must be implemented in the subclass.")

class Name(Field):
    def validate(self):
        if not self.value:
            raise ValueError("Name field is required.")

class Phone(Field):
    def validate(self):
        if self.value and not isinstance(self.value, str):
            raise ValueError("Phone field must be a string.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        phone_obj.validate()
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                break

    def edit_phone(self, old_phone, new_phone):
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone
                phone_obj.validate()
                break

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[Record.name.value] = record
