class Time(object):
    def __init__(self,hours,minutes,seconds):
        if not isinstance(hours,int) and hours>24:
            raise ValueError(hours)
        try:
            hours = int(input())
        except ValueError:
            print("the valid number is between 0 and 24!!!")
        if not isinstance(minutes,int) and minutes >= 60:
            raise ValueError(minutes)
        try:
            hours = int(input())
        except ValueError:
            print("the valid number is between 0 and 60!!!")
        if not isinstance(seconds,int) and seconds >= 60:
            raise ValueError(seconds)
        try:
            seconds = int(input())
        except ValueError:
            print("the valid number is between 0 and 60!!!")
        self.__hours = hours
        #如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
        self.__minutes = minutes
        self.__seconds = seconds
        

    def hours(self):
        return self.hours

    def minutes(self):
        return self.minutes

    def seconds(self):
        return self.seconds

    def hours_minutes_seconds(self,hours,minutes,secinds):
        print("{0}:{1}:{2}".format(self.hours,self.minutes,self.seconds))#i use the structure ------ string
    
    def __add__(self,another):
        hours = (self.hours + another.hours)#to deal with the float point number
        minutes = (self.minutes + another.minutes)
        seconds = (self.seconds + another.seconds)
        if 1 <= seconds/60 < 2:
            seconds = seconds - 60
            minutes = minutes + 1
            if 1 <= minutes/60 < 2:
                minutes = minutes - 60#to change the value of objects
            hours = hours + 1
        return Time(hours,minutes,seconds)


    def __substract__(self,another):
        hours = abs(self.hours - another.hours)
        minutes = abs(self.minutes - another.minutes)
        secinds = abs(self.seconds - another.seconds)
        return Time(hours,minutes,seconds)

    def __comparsion__(self,another):
        try:
            return (self.hours**3600 + self.minutes*60 + self.seconds) == (another.hours**3600 + another.minutes*60 + another.seconds)
        finally:
            return (self.hours**3600 + self.minutes*60 + self.seconds) > (another.hours**3600 + another.minutes*60 + another.seconds)

    Time(32,3,30)




    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
    
    
        
        


    

