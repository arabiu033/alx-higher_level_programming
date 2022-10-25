#!/usr/bin/python3
""" No module imported """


class MyList(list):
    """ Simple class extending from list classs """
    def print_sorted(self):
        """ Print the list in sorted way """
        newVal = list(self.copy())
        newVal.sort()
        print(newVal)
