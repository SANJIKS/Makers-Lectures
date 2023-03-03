from datetime import date

class dates(date):
    def __str__(self):
        return date()

datee = dates()
print(datee.__str__())