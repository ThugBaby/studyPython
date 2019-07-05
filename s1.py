class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print("%s:%s" % (self.name,self.score))
bart=Student("Bart Simpson",90)
bart.print_score()
class Animal(object):
	def run(self):
		print("Animal is ruuning...")
class Dog(Animal):
	pass
class Cat(Animal):
	pass
dog=Dog()
cat=Cat()
dog.run()
cat.run()

a=list()
b=Animal()
c=Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
