class Character(object):
    """docstring for Character"""

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def attack(self, oponent):
        oponent.health -= self.power
        print "%s does %d damage to %s." % (self.name, self.power, oponent.name)
        if oponent.alive() == False:
            print "%s is dead." % (oponent.name)

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


class Zombie(Character):
    def __init__(self, name, health, power):
        super(Character, self).__init__()
        self.health = health
        self.name = name
        self.power = power

    def alive(self):
        if self.health > 0:

            return True
        else:
            return True

hero = Character("Barry Da God", 10, 5)
goblin = Character("Steve The Goblin", 6, 2)
zombie = Zombie("dat dead dude",50,  1)


while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        hero.attack(goblin)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if goblin.alive():
        # Goblin attacks hero
        goblin.attack(hero)
        
while zombie.alive() and hero.alive():
    hero.print_status()
    zombie.print_status()
    print
    print "What do you want to do?"
    print "1. fight zombie"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        hero.attack(zombie)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if zombie.alive():
        # Goblin attacks hero
        zombie.attack(hero)