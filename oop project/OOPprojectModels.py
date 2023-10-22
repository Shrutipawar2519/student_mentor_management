from abc import ABC,abstractmethod

class Person(ABC):
    name = ''
    age = 0
    gender = ''
    __mono = ''

    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g

    def __str__(self):
        return f'Name:{self.name},Age:{self.age},Gender:{self.gender}'

    @abstractmethod
    def setMono(self,mn):
        pass
    
    @abstractmethod
    def getMono(self):
        pass


class Student(Person):
    rn = 0
    marks = 0.0

    def __init__(self,n,a,g,r,m):
        super().__init__(n,a,g)
        self.rn = r
        self.marks = m

    def __str__(self):
        data = super().__str__()
        return f'{data},Rn:{self.rn},Marks:{self.marks}'

    def setMono(self,mn):
        self.__mono = mn
    
    def getMono(self):
        return self.__mono


class Mentor(Person):
    eid = 0
    esal = 0.0

    def __init__(self,n,a,g,i,s):
        super().__init__(n,a,g)
        self.eid = i
        self.esal = s

    def __str__(self):
        data = super().__str__()
        return f'{data},Eid:{self.eid},CTC:{self.esal}'

    def setMono(self,mn):
        self.__mono = mn
    
    def getMono(self):
        return self.__mono
    




    
