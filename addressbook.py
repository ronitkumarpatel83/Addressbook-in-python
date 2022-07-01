import logging


class AddressBook:
    def __init__(self, ab_name):
        self.ab_name = ab_name
        self.person_record = {}

    def add_contact(self, contact_obj):
        try:
            self.person_record.update({contact_obj.first_name: contact_obj})
            return self.person_record
        except Exception as e:
            print(e)
            logging.exception(e)

    def display_person(self):
        try:
            for record in self.person_record:
                person_obj = self.person_record.get(record)
                print(person_obj.details())
        except Exception as e:
            print(e)
            logging.exception(e)

    def update_person(self, contact_obj):
        try:
            self.person_record.update({contact_obj.first_name: contact_obj})
            return self.person_record
        except Exception as e:
            print(e)
            logging.exception(e)

    def delete_person(self, first_name):
        try:
            self.person_record.pop(first_name)
        except Exception as e:
            print(e)
            logging.exception(e)