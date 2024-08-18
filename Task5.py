# Contact list to store contacts
contacts = []

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        contact = {}
        contact['name'] = input("Enter contact name: ")
        contact['phone'] = input("Enter contact phone number: ")
        contact['email'] = input("Enter contact email: ")
        contact['address'] = input("Enter contact address: ")
        contacts.append(contact)
        print("Contact added successfully!")
    elif choice == '2':
        print("\nContact List:")
        if contacts:
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email:{contact['email']}, Address:{contact['address']}")
        else:
            print("No contacts available.")
    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                print(f"\nFound Contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                found = True
        if not found:
            print("No contact found.")
    elif choice == '4':
        search_term = input("Enter the name or phone number of the contact to update: ")
        found = False
        for contact in contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                print(f"\nUpdating Contact: Name: {contact['name']}, Phone: {contact['phone']}")
                contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
                contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact['phone']
                contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
                contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
                print("Contact updated successfully!")
                found = True
                break
        if not found:
            print("No contact found.")
    elif choice == '5':
        search_term = input("Enter the name or phone number of the contact to delete: ")
        for contact in contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("No contact found.")
    elif choice == '6':
        running = False
        print("Exiting the Contact Management System.")
    else:
        print("Invalid choice. Please try again.")

