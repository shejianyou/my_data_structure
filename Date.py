  """
Operator Interface
This module exports a set of functions corresponding to the intrinsic
operators of Python,Actually,i divide these functions to two kinds of classes,which is Mathematical/Bitwise 
Operation,Comparsion Operations.
The function names are those used for special
methods; variants without leading and trailing '__' are also provided
for convenience.
Date interface
This module exports a set of functions correspomding to the intrisic date's operators of Python. 
    """
from datetime import date
class extensionError(ValueError):
    pass
class Date(object):
    def __init__(self, year,month,day,leap_month,floor_month):
        if (not isinstance(year,int))and year > 9999:
            """
            if the input,coming from users,has error in type or extension of value,and the stop 
            of the program is unexpected by me,more importantly,i want to aware the user to input
            a correct number,i should use the structure of the try statement.
            """
            try:
                year = int(year)
            except:
                raise extensionError("the number of year is between 1 and 9999!!!")
        if (not isinstance(month,int)) and month > 12:
            try:
                month = int(month)
            except:
                raise extensionError("the number of year is between 1 and 9999!!!")
        if (not isinstance(day,int)) and day > 31:
            #1 <= day <= number of days in the given month and year
            try:
                day = int(day)
            except:
                raise extensionError("the number of year is between 1 and 9999!!!")
        self.year = year
        self.month = month
        self.day = day
        self.leap_month = [2,4,6,8,10,12]
        self.foor_month = [1,3,5,7,9,11]
        return datetime.date(self.year,self.month,self.day)


    def __difference__(self,another):
        #双下划线表示：这是我的方法，请使用者不要修改
        self._year = abs(self.year - another.year)
        #为了保险起见，我还是加上self.year，为何要用self.语法？
        self._month = abs(self.month - another.month)
        self._day = abs(self.day - another.day)
        return datetime.date(self._year,self._month,self._day)
    
    def __add__(self,another):
        self._year = self.year + another.year#how to deal with the century?
        self._month = self.month + another.month
        """
is there better algorithmetic about this question? we can classify this problem as branch?
i can import datetime and use the classmethod to advance conditions of jugde untill now,so not using datastruture!
        """
        if 1<=self._month // 12 < 2:
            self.year = self.year + 1
            self.month = self.month - 12
        if self.month // 12 == 2:
            self.year = self.year + 2
            self.month = self.month - 24
        if self.month in self.leap_month:
            self.day = self.day + another.day
            if 1 <= self.day // 31 < 2:
                self.month = self.month + 1
                self.day = self.day - 31
            if self.day // 31 == 2:
                self.month = self.month + 2
                self.day = 0
        if self.month in self.floor_month:
            self.day = self.day + another.day
            if 1 <= self.day // 30 < 2:
                self.month = self.month + 1
                self.day = self.day - 30
            if self.day // 30 == 2:
                self.month = self.month + 2
                self.day = 0
        return datetime.date(self.year,self.month,self.day)
    
    def __caclulator__(self):
        """
        it is so diffcult to get complete ways at first,and althoug you find some defects,you have no method to 
        solve them.
        """
        x = self.day / 31
        y = self.day / 31
        z = self.day / 365
        if isinstance(x,int) or isinstance(y,int) or isinstance(z,int):
            if isinstance(x,int):
                self.day = 0
                self.month += x
            elif isinstance(z,int):
                self.year += z
    def __caclulator__(self):
        self.month

                

        

                 



                
        
            
