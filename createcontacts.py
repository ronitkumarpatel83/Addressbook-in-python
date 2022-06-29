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
    def __init__(self, book_dict):
        self.first_name = book_dict.get("first_name")
        self.last_name = book_dict.get("last_name")
        self.address = book_dict.get("address")
        self.city = book_dict.get("city")
        self.state = book_dict.get("state")
        self.pincode = book_dict.get("pincode")
        self.phone_number = book_dict.get("phone_number")
        self.email = book_dict.get("email")
