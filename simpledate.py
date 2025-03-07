class SimpleDate():
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
        self.days = self.day + (self.month * 30) + (self.year * 360)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __gt__(self, another:'SimpleDate'):
        return self.days > another.days
        
    def __lt__(self, another:'SimpleDate'):
        return self.days < another.days
    def __eq__(self, another: 'SimpleDate'):
        return self.__str__() == another.__str__()

    def __ne__(self, another:'SimpleDate'):
        return self.__str__() != another.__str__()
  
    def days_to_date(self, total_days:int):
        years = total_days // 360
        years_remainder = total_days%360
        months = years_remainder // 30
        days = years_remainder%30
        print(f"{total_days} days is {years} years and {years_remainder} days")
        print(f"{years_remainder} days is {months} months and {days} days")
        return years, months, days

    def __add__(self, added_days:int):
        print(f"initial total days {self.days} now adding {added_days} gives {self.days + added_days}")
        total_days = self.days + added_days
        years, months, days = self.days_to_date(total_days)
        return SimpleDate(days, months, years)

    def __sub__(self, another:'SimpleDate'):
        pass

d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)

d3 = d1 + 3
d4 = d2 + 400

print(d1)
print(d2)
print(d3)
print(d4)