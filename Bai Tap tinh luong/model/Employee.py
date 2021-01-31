from datetime import datetime, date, timedelta
import math

from Constants.index import DATE_DB, DATE_FORMAT


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

    def getAge(self):
        birth_date = datetime.strptime(str(self.__dob), DATE_DB)
        age = (date.today() - birth_date.date()) // timedelta(days=365.2425)
        return age

    def getTimeWorked(self):
        startDate = datetime.strptime(str(self.__startDate), DATE_DB)
        differnce = date.today() - startDate.date()
        year = int(differnce.days / 365.25)
        month = (differnce.days-year*365.25)//(365.25/12)
        day = ((differnce.days-year*365.25) - month*(365.25/12))
        return [int(year), int(month), int(math.ceil(day))]

    def getSalaryCurent(self):
        year = self.getTimeWorked()[0]
        coefficientsSalary = 1 + year * 6/100
        curentValue = float(self.__salary) * coefficientsSalary
        return round(curentValue, 2)
