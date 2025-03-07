class Money():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        if num2 <10:
            self.num2str = str('0')+str(num2)
        else:
            self.num2str = str(self.num2)
    def __str__(self):
        return f"{str(self.num1)}.{self.num2str}"
    
    def __eq__(self, another:'Money'):
        return self.__str__() == another.__str__()
    
    def __lt__(self, another:'Money'):
        return self.__str__() < another.__str__()
    def __gt__(self, another:'Money'):
        return self.__str__() > another.__str__()
    def __ne__(self, another:'Money'):
        return self.__str__() != another.__str__()
    def __add__(self, another:'Money'):
        return str(int(self.__str__())+int(another.__str__()))
    def __sub__(self, another:'Money'):
        return str(float(self.__str__())-float(another.__str__()))

e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2-e1