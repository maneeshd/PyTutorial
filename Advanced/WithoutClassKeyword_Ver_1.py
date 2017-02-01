# Using 'type' to create Class


class Parent(object):

    def p_name(self):
        print("This is Parent Class")


def name(self):
    print("This is Child Class")


Child = type('Child', (Parent,), {'name': name})
c = Child()
c.name()
c.p_name()
