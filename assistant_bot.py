from address_book import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid command format."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner


class AssistantBot:
    def __init__(self):
        self.address_book = AddressBook()

    @input_error
    def add_contact(self, name, phone):
        record = Record(name)
        record.add_phone(phone)
        self.address_book.add_record(record)
        return "Contact added."

    @input_error
    def find_contact(self, name):
        found_record = self.address_book.find(name)
        if found_record:
            return str(found_record)
        return "No matching records found."

    @input_error
    def delete_contact(self, name):
        if name in self.address_book.data:
            self.address_book.delete(name)
            return "Record removed."
        return "Record not found."

    @input_error
    def show_all_contacts(self):
        if self.address_book.data:
            return "\n".join([str(record) for record in self.address_book.data.values()])
        return "No records in the address book."

    @input_error
    def edit_contact_phone(self, name, operation, old_phone=None, new_phone=None):
        found_record = self.address_book.find(name)
        if not found_record:
            return "No matching records found."

        if operation == "Add":
            found_record.add_phone(new_phone)
            return "Phone added."
        elif operation == "Remove":
            found_record.remove_phone(old_phone)
            return "Phone removed."
        elif operation == "Edit":
            found_record.edit_phone(old_phone, new_phone)
            return "Phone edited."
        else:
            return "Invalid phone operation."


def main():
    assistant = AssistantBot()
    print("Welcome to the Assistant Bot!")

    while True:
        print("Commands:")
        print("1. Add contact")
        print("2. Find contact by name")
        print("3. Delete contact")
        print("4. Show all contacts")
        print("5. Edit contact phone (Add/Remove/Edit)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            print(assistant.add_contact(name, phone))
        elif choice == "2":
            name = input("Enter name to search: ")
            print(assistant.find_contact(name))
        elif choice == "3":
            name = input("Enter name to remove: ")
            print(assistant.delete_contact(name))
        elif choice == "4":
            print(assistant.show_all_contacts())
        elif choice == "5":
            name = input("Enter name to edit phone: ")
            phone_choice = input("Choose an option (Add/Remove/Edit): ")
            if phone_choice in ["Add", "Remove", "Edit"]:
                if phone_choice == "Add":
                    new_phone = input("Enter the new phone number: ")
                    print(assistant.edit_contact_phone(name, phone_choice, new_phone=new_phone))
                elif phone_choice == "Remove":
                    old_phone = input("Enter the phone number to remove: ")
                    print(assistant.edit_contact_phone(name, phone_choice, old_phone=old_phone))
                else:
                    old_phone = input("Enter the old phone number: ")
                    new_phone = input("Enter the new phone number: ")
                    print(assistant.edit_contact_phone(name, phone_choice, old_phone=old_phone, new_phone=new_phone))
            else:
                print("Invalid phone operation.")
        elif choice == "6":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
