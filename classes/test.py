class PhoneBook(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.peopleList = []

    def phoneBookEmpty(self):
        if len(self.peopleList) == 0:
            print "Phonebook empty"
            return False

    def lookUpEntry(self):
        name = raw_input("name to lookup: ")
        self.phoneBookEmpty()
        for person in self.peopleList:
            if person.name == name:
                print (person.name, person.phone)

    def createContact(self):
        name = raw_input("input name: ")
        phone = raw_input("input phone: ")
        newContact = PhoneBook(name, phone)
        allContacts.peopleList.append(newContact)

    def delEntry(self):
        name = raw_input("name to delete: ")
        self.phoneBookEmpty()
        for i in range(len(self.peopleList)):
            person = self.peopleList[i]
            if person.name == name:
                del self.peopleList[i]

    def listAllEntries(self):
        self.phoneBookEmpty()
        for person in self.peopleList:
            print (person.name, person.phone)


allContacts = PhoneBook("allContacts", "null")


def menu():
    print """    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit"""


def main():
    while True:
        menu()
        answer = int(raw_input("What do you want to do (1-5)? "))
        if answer == 1:
            allContacts.lookUpEntry()
        elif answer == 2:
            allContacts.createContact()
        elif answer == 3:
            allContacts.delEntry()
        elif answer == 4:
            allContacts.listAllEntries()
        elif answer == 5:
            print "Have a Good Day"
            return False


main()
