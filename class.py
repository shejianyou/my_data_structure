# -*- coding: utf-8 -*-
"""
Created on Mon Nov 4 21:05:43 2019

@author: 佘建友

"""
import datetime

class PersonTypeError(TypeError):#to define a class of exception from Python's bultin exception
    pass
class PersonValueError(ValueError):
    pass



class Person(obeject):
    _num = 0 #to represent the data attribute adds 1 when creating a object which derives from the class.
    def __init__(self,name,sex,birthday,ident):
        """
    to check the legal of parameters,it can be thinked as data attributes of object which is accessity.

        """
        if not(isinstance(name,str) and sex not in ('男','女')):
            raise ValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise ValueError("Wrong date:",birthday)
        self._name = name
        self._sex = sex
        self._birthday = birthday
        self._id = ident
        Person._num += 1

    @classmethod   
    def id(self):
        return self._ident

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def age(self):
        return (datetime.date.today().year -
                self._birthday.year)

    def set_name(self, name):
        """
        to change the name of Person
        """
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self,another):
        """
        to give the sequence of objects
        """
        if not isinstance(another,Person):
            raise ValueError(another)
        return self._id < another._id
    
    def num(cls):
        return Person._num

    def __str__(self):
        return " ".join((self._ident,self._name,self._sex,str(self._birthday) ))
    def details(self):
        return ",".join(("编号:"self._ident", 
                         "姓名:"self._name",
                         "性别:"self._sex,
                         "生日:"str(self._birthday)
                         ))



class Student(Person):
    _id._num = 0

    @classmethod
    def _id_gen(self):
        "the rule of studentnumber"
        self._id = _id._num
        enroll_year = datetime.date.today().year
        __id_gen__ = "1{:04}{:05}".format(self._id,enroll_year)

    def __init__(self,name,sex,birthday,department):
        Person.__init__(self,Student.__id_gen__(),name,sex,birthday,Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self.courses = {} # an empty dict

    def set_courses(self,courses_name):
        return self.courses[courses_name] = None

    def score_course(self,courses_name,score):
        if courses_name not in self.courses:
            raise ValueError("Warning!!!,the student do not select the course")
        return self.courses[courses_name] = score

    def list_score(self):
        return [(cname,cname in self.courses)
        for cname in self.courses
        ]
    
    def deatils(self):
        return 
              ", ".join((
                  Person.details(self),
                  "入学日期: " + str(self._enroll_date),
                  "院系: " + self._department,
                  "课程记录: " + str(self.scores())
                        ))



class Graduate(Student):

    @classmethod
    def _id_gen(cls):
        return "研{0}".format(Student._id_gen)   

    def __init__(self, name, sex, birthday, department):
        Student.__init__(self,name,sex,birthday,department)
        self.Award_recording = {}
    
    def set_course(self, course_name):
        Student.set_course()

    def set_score(self, course_name, score):
        Student.set_score()

    def score(self):
        Student.score()
    
    def score_course(self,courses_name,score):
        Student.score_course(self,courses_name,score)
    
    def list_score(self):
        Student.list_score(self)
    
    def Award_recording(self,kind,date):
        try:
            date = datetime.date(*date)
        except:
            raise PersonValueError("wrong date:"
                                               ,date)
        finally:
            self.Award_recording = Award_recording.setdefault(date,kind)
    
    def details(self):
        return Student.deatils(self)



class Staff(Person):
    _id_num = 0
    @classmethod
    def _id_gen_(self,birthday):  
        """
    the rule of staffnumber
        """
        self._id_num += 1
        birthyear = datetime.date.today().year
        return "0{:04}{:05}".formate(self._id_num,birthyear)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday,
                                    Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise ValueError("wrong date:",entry_date)
        else:
            "the basic informations about staff"
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._department = "未定"
        self._position = "未定"
        self._ever_unit = {} #an empty dict

    def set_salary(self,amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self,position):
        self._position = position

    def set_department(self,department):
        self._department = department

    def details(self):
        return ",".join("入职日期"+self._entry_date,
        "职位"+self._position,
        "部门"+ self._departement,
        "薪水"+self._salary)



class Teacher(Person,Staff):

    @classmethod
    def _id_gen(self):
        return "师{0}".format(Staff._id_gen(birthday))
    
    def __init__(self, name, sex, birthday, entry_date=None):
        Staff.__init__(self, name, sex, birthday, entry_date=None)
        self._ever_unit = {}
         
    def set_salary(self,amount):
        return Staff.set_salary(self,amount)
    
    def set_position(self,position):
        return Staff.set_position(self,position)
    
    def set_department(self,department):
        return Staff.set_department(self,department)

    def details(self):
        return Staff.details(self)

    def ever_worked(self,unit,datetime):
        self._ever_unit = self._ever_unit.setdefault(datetime,unit)
        return self._ever_unit



class Workers(Person,Staff):

    @classmethod
    def __id_gen__(self):
        return "工{0}".format(Staff.__id_gen__(birthday))
    
    def __init__(self):
        Staff.__init__(self,name, sex, birthday, entry_date=None)
        self._ever_init = {}
        self._Recruitment_platform = "未定"
    
    def set_salary(self,amount):
        return Staff.set_salary(self,amount)
    
    def set_position(self,position):
        return Staff.set_position(self,position)
    
    def set_department(self,department):
        return Staff.set_department(self,department)

    def ever_worked(self,unit,datetime):
        self._ever_unit = self._ever_unit.setdefault(datetime,unit)
        return self._ever_unit
    
    def set_salary(self,Recruitment_platform):
        if Recruitment_platform not in ("智联招聘","Boss直聘","猎聘网","领英","斗米网","直选会"):
            try:
                print("请输入其他平台或者介绍人！")
                return Recruitment_platform = input()
    
    def details(self):
        return Staff.details(self) + ",Recruitment_platform"

                

    


        
    




        
    




        









        
    
        
        
