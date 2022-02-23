# Hello World program in Python
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
print "Hello World!\n"

class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
      
      
   def __init__(self):
      """ Virtually private constructor. """
      print("===== Singleton.__instance ", Singleton.__instance)
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
s = Singleton()
print s

# b = Singleton()
# print b

s1 = Singleton.getInstance()
print s1

s2 = Singleton.getInstance()
print s2
