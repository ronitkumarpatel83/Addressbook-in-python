from addressbook import AddressBook
from contact import Contact

ab = AddressBook("book")
book_dict = {"first_name": "Ronit", "last_name": "Patel", "address": "rld",
             "city": "sng", "state": "odisha", "pincode": "770001",
             "phone_number": "0123456789", "email": "ronitkumarpatel143@gmail.com"}
cont = Contact(book_dict)


class TestAddressbook:
    def test_add_contact(self):
        assert len(ab.person_record) == 0
        ab.add_contact(cont)
        assert len(ab.person_record) == 1

    def test_delete_person(self):
        ab.add_contact(cont)
        assert len(ab.person_record) == 1
        ab.delete_person("Ronit")
        assert len(ab.person_record) == 0
