# 30. Write a Python class to create a basic contact management 
# system with methods to add, remove, and search for contacts.

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} removed.")
                return
        print(f"Contact {name} not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print(f"Contact {name} not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)


manager = ContactManager()
manager.add_contact("John", "1232344", "john@example.com")
manager.add_contact("Juan", "98734141", "juan@example.com")
print("\nAll contacts:")
manager.display_contacts()
print("\nSearch for John:")
manager.search_contact("John")
print("\nRemove Juan")
manager.remove_contact("Juan")
print("\nAll contacts after removing Juan")
manager.display_contacts()
