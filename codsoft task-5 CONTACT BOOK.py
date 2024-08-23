

contacts = {}  

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"{name} added to contacts.")

def view_contacts():
    print("\nContact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
