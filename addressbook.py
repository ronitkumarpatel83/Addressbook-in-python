import logging


class AddressBook:
    def __init__(self, ab_name):
        """
        This function is the class initialize the object's attributes
        :param ab_name:
        """
        self.ab_name = ab_name
        self.person_record = {}

    def add_contact(self, contact_obj):
        """
        this function is working for add person details in dictionary
        :param contact_obj:
        :return: self.person_record
        """
        try:
            self.person_record.update({contact_obj.first_name: contact_obj})
            return self.person_record
        except Exception as e:
            print(e)
            logging.exception(e)

    def display_person(self):
        """
        This function is working for display person details
        :return:
        """
        try:
            for record in self.person_record:
                person_obj = self.person_record.get(record)
                print(person_obj.details())
        except Exception as e:
            print(e)
            logging.exception(e)

    def delete_person(self, first_name):
        """
        This deletes function is delete person details from dictionary
        :param first_name:
        :return:
        """
        try:
            self.person_record.pop(first_name)
        except Exception as e:
            print(e)
            logging.exception(e)

    def json_write(self):
        """
        This function is working for json here i am adding all dictionary data into json file
        :return:
        """
        try:
            records_dict = {}
            for key, value in self.person_record.items():
                records_dict.update({key: value.details()})
            return {"name": self.ab_name, "records": records_dict}
        except Exception as e:
            print(e)
            logging.exception(e)