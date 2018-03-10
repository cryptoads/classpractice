class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []
        self.greeting_count = 0
        self.unique_count = 0
        self.unique_greet = []

    def num_friend(self):
        print len(self.friend)

    def add_friend(self, friends):
        self.friend.append(friends)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        print self.greeting_count
        if other_person not in self.unique_greet:
            self.unique_greet.append(other_person)
            self.unique_count += 1

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.email, self.phone)

    def unique_peep_greet(self):
        print self.unique_count





sonny = Person('Sonny', 'sonny@hotmail.com', '483.485.4948')
jordan = Person('Jordan', 'jordan@aol.com', '495.586.3456')
dee = Person('dee', 'dee@deez.com', '123.456.789')
Person.greet(sonny, jordan)
Person.greet(jordan, sonny)
Person.greet(sonny, jordan)
print 'Email %s phone %s' % (sonny.email, sonny.phone)
print 'email %s phone %s' % (jordan.email, jordan.phone)
sonny.print_contact_info()
# jordan.friend.append(sonny)
# sonny.friend.append(jordan)
jordan.add_friend(sonny)
sonny.add_friend(jordan)

sonny.num_friend()
print jordan
Person.greet(sonny, dee)
sonny.unique_peep_greet()