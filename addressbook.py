from createcontacts import CreateContacts


class AddressBook:
    addressbook = []

    def add_person(self, dict_person):
        """
        Description:
            This function is getting details from user input and store it in list
        parameter :
            first_name, last_name, address, city, state, pincode, phone_number, email
        return:
            return list of addressbook
        """
        record_dict = {"first_name": dict_person.get("First Name"),
                       "last_name": dict_person.get("Last Name"),
                       "address": dict_person.get("Address"),
                       "city": dict_person.get("City"),
                       'state': dict_person.get("State"),
                       "pincode": dict_person.get("Pincode"),
                       "phone_number": dict_person.get("Phone Number"),
                       "email": dict_person.get("Email")}
        add = CreateContacts(record_dict)

        self.addressbook.append(add)
        return self.addressbook

    def display_person(self):
        """
        Description:
            This function is printing address book person details
        :return:
        """
        i = 1
        print("\nContact details present in Address Book : ")
        for detail in self.addressbook:
            print(f"\nRecord - {i}")
            print(f"First name : {detail.first_name}")
            print(f"Last name : {detail.last_name}")
            print(f"Address : {detail.address}")
            print(f"City : {detail.city}")
            print(f"State : {detail.state}")
            print(f"Pincode : {detail.pincode}")
            print(f"Phone Number : {detail.phone_number}")
            print(f"Email : {detail.email}")
            i += 1

    def find_person(self, first_name):
        """
        This function is finding addressbook records based on first name
        :param first_name:
        :return: bool
        """
        for record in self.addressbook:
            if record.first_name == first_name:
                return True
            return False

    def update_records(self, old_fname,dict_person):
        """
        Description:
            This function is updating address book records
        Parameter:
            It takes self and first name as argument
        Return:
            returns list of records
        """
        for record in self.addressbook:
            if record.first_name == old_fname:
                record.first_name = dict_person.get("First Name")
                record.last_name = dict_person.get("Last Name")
                record.address = dict_person.get("Address")
                record.city = dict_person.get("City")
                record.state = dict_person.get("State")
                record.pincode = dict_person.get("Pincode")
                record.phone_number = dict_person.get("Phone Number")
                record.email = dict_person.get("Email")
                print("\nRecord Updated Successfully !!")
        return self.addressbook

    def delete_record(self,first_name):
        """
        Description:
            This function is deleting address book records
        Parameter:
            It takes self and first name as argument
        Return:
            returns list of records
        """
        for record in self.addressbook:
            if record.first_name == first_name:
                self.addressbook.remove(record)
                print("\nRecord Deleted Successfully")
            return self.addressbook

    def add_multiple_person(self):
        pass