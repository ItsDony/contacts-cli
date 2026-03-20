import json
# ===== CLASS =====
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __str__(self):
        return f"Имя: {self.name}\n   Номер: {self.number}\n"
    def to_dict(self):
        return {
            "name": self.name,
            "number": self.number
        }

# ===== LOAD_TXT =====
def load_contact():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Contact(contacts["name"], contacts["number"]) for contacts in data]
    except FileNotFoundError:
        return []

# ===== SAVE_TXT =====
def save_contact(contacts):
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump([contacts.to_dict() for contacts in contacts], file, ensure_ascii=False, indent=4)

# ===== GET_CHOISE =====
def get_choise(text):
    while True:
        choise = str(input(text))
        if choise in ("1", "2", "3", "4", "5"):
            return choise
        else:
            print("\nSuch an action does not exist!")

# ===== GET_CHOISE_SEARCH =====
def get_choise_search(text):
    while True:
        choise_search = str(input(text))
        if choise_search in ("1", "2", "3"):
            return choise_search
        else:
            print("\nSuch an action does not exist!")

# =====GET_INDEX=====
def get_index(max_len):
    while True:
        try:
            delite = int(input("Enter what you want to delete: ")) - 1
            if 0 <= delite <= max_len:
                return delite
            else:
                print("\nSuch an action does not exist!")
        except ValueError:
            print("\nYou made a mistake!")

# ===== ADD CONTACT IN LIST =====
def add_contact(contacts):
    name = str(input("\nEnter name: "))
    number = str(input("Enter number: "))
    contacts.append(Contact(name, number))
    save_contact(contacts)
    print(f"\nContact {name} successfully added!")

# ===== LIST CONTACT =====
def list_contacts(contacts):
    if not contacts:
        print("The contact list is empty.")
        return
    for i, j in enumerate(contacts, 1):
        print(f"{i}. {j}")

# ===== SEARCH IN LIST CONTACT =====
def search(contacts):
    if not contacts:
        print("\nThe contact list is empty.")
        return
    else:
        print("===Search===\n")
        print("1. Search by name.\n2. Search by number.\n3. Exit.")
        choise = get_choise_search("Select an action: ")
        if choise == "1":                                               # <--- SEARCH BY NUMBER
            search_name = str(input("\nEnter name: ")).lower()
            found = False

            for user in contacts:
                if search_name in user.name:
                    print(f"\nName: {user.name}\nNumber: {user.number}")
                    found = True

            if not found:
                print("\nContact not found.")
        elif choise == "2":                                             # <--- SEARCH BY NUMBER
            search_number = str(input("\nEnter number: ")).lower()
            found = False

            for user in contacts:
                if search_number in user.number:
                    print(f"\nName: {user.name}\nNumber: {user.number}")
                    found = True

            if not found:
                print("\nContact not found.")
        elif choise == "3":                                             # <--- EXIT
            return

# ===== DELETED CONTACT =====
def deleted_contact(contacts):
    if not contacts:
        print("\nThe contact list is empty.")
        return
    else:
        print("===Delete contact===\n")
        list_contacts(contacts)
        index = get_index(len(contacts))
        deleted = contacts.pop(index)
        save_contact(contacts)
        print(f"\nYou have successfully deleted {deleted.name}!")

# ===== MAIN =====
def main():
    contacts = load_contact()
    while True:
        print("\n====MENU====\n1. Add contact.\n2. List contacts.\n3. Search.\n4. Remove contact.\n5. Exit.")
        choise = get_choise("\nChoise an action: ")
        if choise == "1":                              # <--- ACTION 1
            add_contact(contacts)
        elif choise == "2":                            # <--- ACTION 2
            print("==List contacts==\n")
            list_contacts(contacts)
            input("\nPress enter to continue...")
        elif choise == "3":                            # <--- ACTION 3
            search(contacts)
        elif choise == "4":                            # <--- ACTION 4
            deleted_contact(contacts)
        elif choise == "5":                            # <--- ACTION 5
            print("\nGood luck!")
            break

# ===== START =====
if __name__ == "__main__":
    main()
