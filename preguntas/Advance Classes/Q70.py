#  Write a Python class to represent a contact book with methods to add, 
# remove, update, and search contacts.
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        """Add a new contact to the contact book."""
        if name in self.contacts:
            raise ValueError(f"Contact with name '{name}' already exists.")
        self.contacts[name] = Contact(name, phone, email)

    def remove_contact(self, name):
        """Remove a contact from the contact book."""
        if name in self.contacts:
            del self.contacts[name]
        else:
            raise KeyError(f"Contact with name '{name}' not found.")

    def update_contact(self, name, phone=None, email=None):
        """Update the phone number and/or email of an existing contact."""
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
        else:
            raise KeyError(f"Contact with name '{name}' not found.")

    def search_contact(self, name):
        """Search for a contact by name."""
        return self.contacts.get(name, None)

    def list_contacts(self):
        """Return a list of all contacts."""
        return [str(contact) for contact in self.contacts.values()]

    def __str__(self):
        """Return a string representation of the contact book."""
        if not self.contacts:
            return "Contact book is empty."
        return "\n".join([str(contact) for contact in self.contacts.values()])


contact_book = ContactBook()
contact_book.add_contact("John", "55-1234-5678", "john@asdrome.com")
contact_book.add_contact("Isaac", "55-7365-4321", "isaac@asdrome.com")
print("Contact Book:")
print(contact_book)
print("\nUpdating John phone number...")
contact_book.update_contact("John", phone="56-2222-3333")
print(contact_book)
print("\nSearching for Isaac...")
contact = contact_book.search_contact("Isaac")
print(contact if contact else "Contact not found.")
print("\nRemoving Isaac...")
contact_book.remove_contact("Isaac")
print(contact_book)
print("\nListing all contacts:")
for contact in contact_book.list_contacts():
    print(contact)