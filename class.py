class car:
	def __init__(self,x,y):
		self.tank=x
		self.eng=y
		print(id(self), "Constructor invoked")
	def speed(x):
		return x.tank*x.eng
alto=car(20,800)
print(alto.speed())
dezire=car(30,2000)
print(dezire.speed())

class AUDI(car):
	def __init__(self,a,b):
		self.tyrewidth=a
		self.tyreradius=b
		self.tank=a
		self.eng=b
	
	def tyresize(y):
		return y.tyrewidth-y.tyreradius
kaliaudi=AUDI(40,3000)
print("tyresize of AUDI is", kaliaudi.tyresize())
safedaudi=AUDI(40,20)
print("speed of AUDI is", safedaudi.speed())

class BMW(AUDI,car):
	pass
BADIBMW=BMW(40,300)
print("tyresize of BMW is", BADIBMW.tyresize())
Chotibmw=BMW(10,200)
print("speed of BMW is", Chotibmw.speed())

