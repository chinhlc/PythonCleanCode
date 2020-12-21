from datetime import date
from constants.index import DATE_FORMAT


class ModelEmployee():

    def __init__(self):
        self.__name = None
        self.__dob = None
        self.__role = None
        self.__salary = None
        self.__startDate = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setDob(self, dob):
        self.__dob = dob

    def getDob(self):
        return self.__dob

    def setRole(self, role):
        self.__role = role

    def getRole(self):
        return self.__role

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def setStartDate(self, startdate):
        self.__startDate = startdate

    def getStartDate(self):
        return self.__startDate

    def getAge(self, role):
        birth_date = self.__dob

        dateCheck = date.today().strftime(DATE_FORMAT)
        return self.__role
