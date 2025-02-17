import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    contacts = load_contacts()
    results = [c for c in contacts if query in c['name'] or query in c['phone']]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
    print()

def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input(f"Enter new phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    contacts = [c for c in contacts if c['name'] != name]
    save_contacts(contacts)
    print("Contact deleted successfully!\n")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
