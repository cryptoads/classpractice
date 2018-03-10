pbook = {}


def menu():
    print "Electronic Phone Book"
    print "====================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"
    select = raw_input("What do you want? ")
    selection(select)


def selection(select):
    if select == '1':
        person = raw_input("Who are you looking for? ").title()
        if pbook.get(person):
            print ''.join(pbook[person])
            menu()
        else:
            print "Not in directory"
            menu()
    elif select == '2':
        key = raw_input("Name? ").title()
        value = raw_input("Number? ")
        pbook[key] = [value]
        menu()
    elif select == '3':
        person = raw_input("who would you like to delete? ").title()
        if pbook.get(person):
            del pbook[person]
            menu()
        else:
            print "Not in directory"
            menu()
    elif select == '4':
        for x, y in pbook.items():
            print x
            print ''.join(y)
        menu()
    elif select == '5':
        print "Bye"
    else:
        print "Please select 1 - 5"
        menu()


menu()
