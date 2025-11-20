'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name

    def set_name(self, staff_name):
        if not isinstance(staff_name, str) or not staff_name.strip():
            raise ValueError("Staff name must be a non-empty string.")
        self.__name = staff_name

    staff_name = property(get_name, set_name)

    def get_role(self):
        return self.__role

    def set_role(self, staff_role):
        if not isinstance(staff_role, str) or not staff_role.strip():
            raise ValueError("Role must be a non-empty string.")
        self.__role = staff_role

    staff_role = property(get_role, set_role)