class Contact:
    def __init__(self, book_dict):
        """
        This function is the class initialize the object's attributes
        :param book_dict:
        """
        self.first_name = book_dict.get("first_name")
        self.last_name = book_dict.get("last_name")
        self.address = book_dict.get("address")
        self.city = book_dict.get("city")
        self.state = book_dict.get("state")
        self.pincode = book_dict.get("pincode")
        self.phone_number = book_dict.get("phone_number")
        self.email = book_dict.get("email")

    def details(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "address": self.address,
                "city": self.city, "state": self.state, "pincode": self.pincode,
                "phone_number": self.phone_number, "email": self.email}
