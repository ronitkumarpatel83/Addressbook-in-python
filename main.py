from addressbook import AddressBook
from createcontacts import logging

print("\nWelcome to Address Book System")

records = AddressBook()
try:
    print("\n1. Add a new Record\n")
    ch = int(input("\nEnter your choice : "))
    if ch == 1:
        first_name = input("\nEnter your First Name : ")
        last_name = input("Enter your Last Name : ")
        address = input("Enter your Address : ")
        city = input("Enter your City Name : ")
        state = input("Enter your State Name : ")
        pincode = int(input("Enter your Pincode : "))
        phone_number = int(input("Enter your Phone Number : "))
        email = input("Enter your Email : ")
        dict_person = {"First Name": first_name, "Last Name": last_name, "Address": address, "City": city,
                       "State": state, "Pincode": pincode, "Phone Number": phone_number, "Email": email}
        records.add_person(dict_person)
        records.display_person()
    else:
        print("Choice is invalid")
except Exception as e:
    print(e)
    logging.exception(e)
