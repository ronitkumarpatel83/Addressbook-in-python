import pytest

from addressbook import AddressBook
from contact import Contact


@pytest.fixture
def addressbook():
    return AddressBook("book")


@pytest.fixture
def book_dict():
    return {"first_name": "Ronit", "last_name": "Patel", "address": "rld",
            "city": "sng", "state": "odisha", "pincode": "770001",
            "phone_number": "0123456789", "email": "ronitkumarpatel143@gmail.com"}


@pytest.fixture
def contact(book_dict):
    return Contact(book_dict)


class TestAddressbook:
    def test_add_contact(self, addressbook, contact):
        assert len(addressbook.person_record) == 0
        addressbook.add_contact(contact)
        assert len(addressbook.person_record) == 1

    def test_delete_person(self, addressbook, contact):
        addressbook.add_contact(contact)
        assert len(addressbook.person_record) == 1
        addressbook.delete_person("Ronit")
        assert len(addressbook.person_record) == 0

    def test_contact_obj(self, book_dict, contact):
        assert contact.first_name == book_dict.get("first_name")

    def test_addressbook_obj(self, addressbook):
        assert addressbook.ab_name == "book"
        assert len(addressbook.person_record) == 0
