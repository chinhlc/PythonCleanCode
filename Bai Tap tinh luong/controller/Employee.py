import csv
from Model.Employee import ModelEmployee


class ControlEmployee():
    def __init__(self):
        pass

    def renderData(self):
        with open('employee.csv', "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for item in reader:
                data = ModelEmployee()
                data.setName(item['name'])
                data.setDob(item['dob'])
                data.setStartDate(item['startdate'])
                data.setSalary(item['salary'])
                timeWorked = data.getTimeWorked()
                print(
                    f'Nhan vien: {data.getName()} - Tuoi: {data.getAge()} - Luong {data.getSalaryCurent()} - Nam lam viec: {timeWorked[0]} nam, {timeWorked[1]} thang, {timeWorked[2]} ngay')
