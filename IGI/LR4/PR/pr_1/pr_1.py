import csv
import pickle

class PhoneBook:
    def __init__(self, filename="phonebook.csv"):
        self.filename = filename
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.data[row["Name"]] = row["Phone"]
        except FileNotFoundError:
            pass 

    def save_data(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["Name", "Phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for name, phone in self.data.items():
                writer.writerow({"Name": name, "Phone": phone})

    def add_contact(self, name, phone):
        self.data[name] = phone
        self.save_data()
        print(f"Contact {name} added!")

    def find_contact(self, name):
        if name in self.data:
            print(f"Telephone {name}: {self.data[name]}")
        else:
            print(f"Contact {name} not found")

    def find_by_prefix(self, prefix):
        matches = [name for name, phone in self.data.items() if phone.startswith(prefix)]
        if matches:
            print("Contacts:")
            for name in matches:
                print(f"{name}: {self.data[name]}")
        else:
            print("Not found")

    def sort_contacts(self):
        sorted_data = dict(sorted(self.data.items()))
        print("Sorted:")
        for name, phone in sorted_data.items():
            print(f"{name}: {phone}")

class PhoneBookPickle(PhoneBook):
    def __init__(self, filename="phonebook.pickle"):
        super().__init__(filename)

    def load_data(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file)

def task1():
    # CSV 
    phonebook_csv = PhoneBook()
    phonebook_csv.add_contact("Ivan Ivanov", "+79111234567")
    phonebook_csv.add_contact("Petr Petrov", "+79221112233")
    phonebook_csv.find_contact("Ivan Ivanov")
    phonebook_csv.find_by_prefix("+791")
    preg = input("Enter string:")
    phonebook_csv.find_by_prefix(preg)
    phonebook_csv.sort_contacts()

    # Pickle 
    phonebook_pickle = PhoneBookPickle()
    phonebook_pickle.add_contact("Maria Sidorova", "+79815556677")
    phonebook_pickle.find_contact("Maria Sidorova")

if __name__ == "__main__":
    task1()

