"""
    @Name = Ronit kumar Patel
    @Title = Address book
"""
import logging
from addressbook import AddressBook
from contact import Contact

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='address_book.log', filemode='a', format=log, level=logging.DEBUG)

logging.debug("Address Book Program running................")


def create_addressbook():
    book = input("Enter addressbook name : ")
    book_obj = AddressBook(book)
    addressbook_dict.update({book_obj.ab_name: book_obj})
    return addressbook_dict


def display_list_of_addressbook():
    print(addressbook_dict)


def add_person():
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
    book = input("Enter addressbook name : ")
    book_obj = addressbook_dict.get(book)
    if book_obj is None:
        print("Addressbook doesn't exit")
        return
    book_obj.display_person()


def update_person():
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
    dict_person = {"First Name": first_name, "Last Name": last_name, "Address": address, "City": city,
                   "State": state, "Pincode": pincode, "Phone Number": phone_number, "Email": email}
    contact_obj = Contact(dict_person)
    book_obj.update_person(contact_obj=contact_obj)


def delete_person():
    book = input("Enter addressbook name : ")
    book_obj = addressbook_dict.get(book)
    if book_obj is None:
        print("Addressbook doesn't exit")
        return
    person_name = input("Enter person name : ")
    book_obj.delete_person(person_name)


if __name__ == '__main__':
    print("********************************************************************************")
    print("<<<<<<<<<<<<----- Welcome to Address Book Program----->>>>>>>>>>>>> ")
    print("********************************************************************************")
    addressbook_dict = {}
    try:
        while True:
            print("1.Create AddressBook \n2.Display list of Addressbook\n3.Add Person\n4.Display persons record"
                  "\n5.Update person record \n6.Delete person\n0.Exit")
            switcher = {
                1: create_addressbook,
                2: display_list_of_addressbook,
                3: add_person,
                4: display_person,
                5: update_person,
                6: delete_person
            }
            a = int(input("Enter your choice : "))
            if a == 0:
                break
            switcher.get(a)()

    except Exception as e:
        print(e)
        logging.exception(e)
