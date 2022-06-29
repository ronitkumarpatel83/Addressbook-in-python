"""
    @Name = Ronit kumar Patel
    @Title = Address book
"""
import logging

print("********************************************************************************")
print("<<<<<<<<<<<<----- Welcome to Address Book Program----->>>>>>>>>>>>> ")
print("********************************************************************************")

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='address_book.log', filemode='a', format=log, level=logging.DEBUG)

logging.debug("Address Book Program running................")


class CreateContacts:
    def __init__(self, first_name, last_name, address, city, state, pincode,
                 phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode
        self.phone_number = phone_number
        self.email = email
