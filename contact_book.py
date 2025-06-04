contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved.")

def view_contacts():
    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
