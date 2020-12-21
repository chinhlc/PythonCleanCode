# Hướng dẫn cách chạy

1. Chạy chương trình
   Mở cmd chạy lệnh:

```
python -b index.py
```

kết quả hiển thị trên command line:

```
Nhan vien: Trịnh Minh Cường - Tuoi: 45 - Luong 10400000.0 - Nam lam viec: 5 nam, 10 thang, 9 ngay
Nhan vien: Nguyễn Văn X - Tuoi: 48 - Luong 24900000.0 - Nam lam viec: 11 nam, 0 thang, 10 ngay
Nhan vien: Đoàn Văn Y - Tuoi: 21 - Luong 9540000.0 - Nam lam viec: 1 nam, 8 thang, 18 ngay
Nhan vien: Nguyễn Thị A - Tuoi: 25 - Luong 70000000.0 - Nam lam viec: 0 nam, 11 thang, 17 ngay
Nhan vien: Đoàn Văn B - Tuoi: 30 - Luong 9130000.0 - Nam lam viec: 11 nam, 1 thang, 9 ngay
Nhan vien: Bùi Thị C - Tuoi: 26 - Luong 8960000.0 - Nam lam viec: 2 nam, 2 thang, 11 ngay
```

2. Cách tính số năm khoảng cách giữa 2 thời điểm như sau:

```
def getAge(self):
        birth_date = datetime.strptime(str(self.__dob), DATE_DB)
        age = (date.today() - birth_date.date()) // timedelta(days=365.2425)
        return age
```

3. Cách tính số năm, số tháng, số ngày đã làm việc:

```
def getTimeWorked(self):
        startDate = datetime.strptime(str(self.__startDate), DATE_DB)
        differnce = date.today() - startDate.date()
        year = int(differnce.days / 365.25)
        month = (differnce.days-year*365.25)//(365.25/12)
        day = ((differnce.days-year*365.25) - month*(365.25/12))
        return [int(year), int(month), int(math.ceil(day))]
```
