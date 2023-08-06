import os
import json
import pyautogui

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}

def search_contact(contacts, name):
    return contacts.get(name)

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        return True
    return False

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        return True
    return False

def get_contact_from_whatsapp():
    print("Please open WhatsApp and focus on the chat window with the contact.")
    name = input("Enter contact name: ")
    phone = pyautogui.prompt("Enter contact phone number:")
    email = pyautogui.prompt("Enter contact email (optional):")
    return name, phone, email

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Get Contact from WhatsApp")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
            save_contacts(contacts)
            print(f"Contact '{name}' added successfully!")

        elif choice == "2":
            name = input("Enter name to search: ")
            contact = search_contact(contacts, name)
            if contact:
                print(f"Contact: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            if update_contact(contacts, name, phone, email):
                save_contacts(contacts)
                print(f"Contact '{name}' updated successfully!")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "4":
            name = input("Enter name to delete: ")
            if delete_contact(contacts, name):
                save_contacts(contacts)
                print(f"Contact '{name}' deleted successfully!")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "5":
            name, phone, email = get_contact_from_whatsapp()
            add_contact(contacts, name, phone, email)
            save_contacts(contacts)
            print(f"Contact '{name}' added successfully!")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
