   # -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:05:43 2019

@author: 佘建友

Operator Interface
This module exports a set of functions corresponding to the intrinsic
operators of Python,Actually,i divide these functions to three kinds of classes,which is Mathematical/Bitwise 
Operation,Comparsion Operations,logical Operations.
The function names are those used for special
methods; variants without leading and trailing '__' are also provided
for convenience.
    """
__all__ = []
from builtins import abs as _abs
from decimal import Decimal as D
class Rational(object):
    @staticmethod
    def __gcd(m,n):
        if n == 0:
            m, n = n, m#the den is not zero!
        while m != 0:
            m , n = n % m ,m#to simplify the rational number
        return n

    def __init__(self, num, den=1):
        if not isinstance(num,int) or not isinstance(den,int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num , sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        if isinstance(num,float) or isinstance(den,float):
            #to call a classmethod deriving a more big class which have more broad namespace.
            num = D('num').as_integer_ratio()
            den = D('den').as_integer_ratio()
        g = Rational.__gcd(num, den)
        #call function gcd defined in this class
        self._num = sign * (num//g)
        self.num = den//g
    
    @classmethod
    def num(self):
        return self._num

    def den(self):
        return self._den

    def abs(self):
        self._num = _abs(num)
        self._den = _abs(den)
        return self._num
        return self._den

     
    def convert_to_int(self): 
        return int(self._num / self._den)
      
    def convert_to_float(self):
        return float(self._num / self._den)


    
    """
Mathematical/Bitwise Operations.

    """
    def __add__(self,another):   # mimic + operator
        den = self._den * another.den()
        num = (self._num * another.den()+
                self._den * another.num())
        return Rational(num, den)

    def __product__(self,another):  #mimic * operator
        return Rational(self._num * another.num(),
                            self._den * another.den()
            )

    def __floordiv__(self,another): #mimic // operator
        if another.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * another.den(),
                            self._den * another.num()
                            )

    def __sub__(self,another): #mimic - operator
        den = self._den * another.den()
        num = (self._num * another.den()
                      -
               self._den * another.den()
               ) 
        return Rational(num,den)

    def __trudiv__(self,another): #mimic / operator
        den = float(self._den * another.num())
        num = float(self.num * another.den())
        return Rational(num,den)

    def __floor__(self,another): #mimic % operator
        b = int(__trudiv__(self,another))
        return self._b  #i can return directivly?

    def __mod__(self,another):
        mod = (__trudiv__(self,another)) - (__floor__(self,another))
        return self._mod

    def __divmod__(self,another):
        a_tuple = (__floor__(self,another),__mod__(self,another))
        return a_tuple


    """
comparison operatios 
!=:__ne__, <=:__le__, >:__gt__, >=:__ge__,to return a boolean value,'True' or 'False'.
    """
    def __eq__(self,another ):  #mimic = operator
        return self._num * another.den() == self._den * another.num()

    def __lt__(self,another):   #mimic < operator
        return self._num * another.den() < self._den * another.num()

    def __ne__(self,another):   #mimic != operator
        return self._num * another.den() != self.den * another.num()

    def __le__(self,another):   #mimic <= operator
        return self._num * another.den() <= self._den * another.num()

    def __gt__(self,another):   #mimic > operator
        return self._num * another.den() > self._den * another.num()

    def __ge__(self,another):   #mimic >= operator
        return self._num * another.den() >= self._den * another.num()
    
    """
to give the rational number a formating of string.
    """
    def __str__(self):    
            return str(self._num) + "/" + str(self._den)
    def print(self):
        print(self._num, "/", self._den)
        


