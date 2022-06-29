from addressbook import AddressBook
from createcontacts import logging


if __name__ == "__main__":
    print("\nWelcome to Address Book System")

    records = AddressBook()
    try:
        dict_person = {}
        while True:
            print("\n1. Add a new Record\n2. Update record\n0. Exit")
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
            elif ch == 2:
                old_fname = input("\nEnter your First Name : ")
                check = records.find_person(old_fname)
                if check:
                    first_name = input("\nEnter your new First Name : ")
                    last_name = input("Enter your new Last Name : ")
                    address = input("Enter your new Address : ")
                    city = input("Enter your new City Name : ")
                    state = input("Enter your new State Name : ")
                    pincode = input("Enter your new Zip Code : ")
                    phone_number = input("Enter your new Phone Number : ")
                    email = input("Enter your new Email : ")
                    dict_person = {"First Name": first_name, "Last Name": last_name, "Address": address, "City": city,
                                   "State": state, "Pincode": pincode, "Phone Number": phone_number, "Email": email}
                    records.update_records(old_fname,dict_person)
                    records.display_person()
                else:
                    print("Record Not Found!!")
            elif ch == 0:
                break
            else:
                print("Choice is invalid")
    except Exception as e:
        print(e)
        logging.exception(e)
