"""
    @Name = Ronit kumar Patel
    @Title = Address book
"""
import json
import logging
import os

from addressbook import AddressBook
from contact import Contact

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='address_book.log', filemode='a', format=log, level=logging.DEBUG)

logging.debug("Address Book Program running................")


def create_addressbook():
    """
    In this hanging function i create addressbook name
    :return:addressbook_dict
    """
    book = input("Enter addressbook name : ")
    book_obj = AddressBook(book)
    addressbook_dict.update({book_obj.ab_name: book_obj})
    return addressbook_dict


def display_list_of_addressbook():
    """
    Here displaying the addressbook name and addressbook object
    :return:
    """
    print(addressbook_dict)


def add_person():
    """
    In this hanging function i create addressbook name and add person details
    :return:
    """
    book = input("Enter addressbook name : ")
    book_obj = addressbook_dict.get(book)
    if book_obj is None:
        book_obj = AddressBook(book)
        addressbook_dict.update({book_obj.ab_name: book_obj})
    first_name = input("\nEnter your First Name : ")
    last_name = input("Enter your Last Name : ")
    address = input("Enter your Address : ")
    city = input("Enter your City Name : ")
    state = input("Enter your State Name : ")
    pincode = input("Enter your Zip Code : ")
    phone_number = input("Enter your Phone Number : ")
    email = input("Enter your Email : ")
    dict_person = {"first_name": first_name, "last_name": last_name, "address": address, "city": city,
                   "state": state, "pincode": pincode, "phone_number": phone_number, "email": email}
    contact_obj = Contact(dict_person)
    book_obj.add_contact(contact_obj=contact_obj)


def display_person():
    """
    Here display the address-books and person details
    :return:
    """
    book = input("Enter addressbook name : ")
    book_obj = addressbook_dict.get(book)
    if book_obj is None:
        print("Addressbook doesn't exit")
        return
    book_obj.display_person()


def delete_person():
    """
    Here deleting the person details using addressbook name
    :return:
    """
    book = input("Enter addressbook name : ")
    book_obj = addressbook_dict.get(book)
    if book_obj is None:
        print("Addressbook doesn't exit")
        return
    person_name = input("Enter person name : ")
    book_obj.delete_person(person_name)


def json_write():
    """
    Here, Creating a Json file for storing all details of addressbook
    :return:
    """
    ab = {}
    for k, v in addressbook_dict.items():
        ab.update({k: v.json_write()})
    with open('json_file.json', 'w') as file:
        file.write(json.dumps(ab, indent=4))


def json_read():
    """
    Is there reading json data
    :return:
    """
    with open('json_file.json', 'r') as file:
        data = json.loads(file.read())
        print(data)


def json_delete():
    """
    Here deleting the json file
    :return:
    """
    if os.path.exists("json_file.json"):
        os.remove("json_file.json")
    else:
        print("The file does not exist")


if __name__ == '__main__':
    print("********************************************************************************")
    print("<<<<<<<<<<<<----- Welcome to Address Book Program----->>>>>>>>>>>>> ")
    print("********************************************************************************")
    addressbook_dict = {}
    try:
        while True:
            print("1.Create AddressBook \n2.Display list of Addressbook\n3.Add Person\n4.Display persons record"
                  "\n5.Update person record \n6.Delete person \n7.Add record in json file"
                  "\n8.Read json file data\n9.Delete json file\n0.Exit")
            switcher = {
                1: create_addressbook,
                2: display_list_of_addressbook,
                3: add_person,
                4: display_person,
                5: add_person,
                6: delete_person,
                7: json_write,
                8: json_read,
                9: json_delete
            }
            a = int(input("Enter your choice : "))
            if a == 0:
                break
            switcher.get(a)()

    except Exception as e:
        print(e)
        logging.exception(e)
