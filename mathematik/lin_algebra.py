import random,math,time

prefix=time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime())

#Lines are created as ax+by=c, a is expected to be not 0
class Fraction:
	def __init__(self, numerator, divisor):
		self.numerator = numerator
		self.divisor = divisor
		self.whole = self.numerator % self.divisor
		self.numerator = self.numerator - self.divisor * self.whole
	def reduce(self):
		if abs(self.numerator) < 2 or abs(self.divisor) < 2:
			return
		while self.numerator % 2 == 0 and self.divisor % 2 == 0:
			self.numerator = self.numerator / 2
			self.divisor = self.divisor/ 2
		f = 3
		print "%d,%d" % (self.numerator, self.divisor)
		while f < 1 + int(max(math.sqrt(abs(self.divisor)),math.sqrt(abs(self.numerator)))):
			print "%d,%d" % (self.numerator, self.divisor)
			while self.numerator % f == 0 and self.divisor % f == 0:
				self.numerator = self.numerator / f
				self.divisor = self.divisor/ f
			f = f + 2
		return (self.numerator, self.divisor)
	def toTxt():
		text=str(

class LineFct:
	def __init__(self, a = None, b = None, c = None):
		if type(a) == [float, int]:
			self.a = a
		else:
			self.a = random.randint(-10,10)
		if type(b) in [float, int]:
			self.b = b
		else:
			self.b = random.randint(-10,10)			
		if type(c) in [float, int]:
			self.c = c
		else:
			self.c = random.randint(-10,10)
		self.incline = Fraction(self.a, self.b)
		self.incline.reduce()
		self.yachsis = Fraction(self.c, self.b)
		self.yachsis.reduce()

	def x(self, y):
		if self.a != 0:
			return (self.c-self.b*y)/float(self.a)
		print "No solution due to a==0"
		return None
		
	def y(self, x):
		if self.b != 0:
			return (self.c-self.a*x)/float(self.b)
		print "No solution due to b==0"
		return None
		
	def genGetYForXTxt(self):
		task = ""
		solutionm = ""
		x = random.randint(-10,10)
		y = self.y(x)
		task = "P=(" + str(x) + ",	 )"
		if y == None:
			solution = "No solution (b=0)"
		else:
			solution = "P=(%d,%.3f)" % (x,y)
		return (task,solution)
		 
	def genGetXForYTxt(self):
		task = ""
		solutionm = ""
		y = random.randint(-10,10)
		x = self.x(y)
		task = "P=(	 ,%d)" % (y)
		if x == None:
			solution = "No solution (a=0)"
		else:
			solution = "P=(%d,%.3f)" % (x,y)
		return (task,solution)
		
	def genFormelTxt(self):
		text = str(self.a) + "x "
		if self.b < 0:
			text = text + " - " + str(abs(self.b)) + "y = " + str(self.c)
		else:
			text = text + " + " + str(self.b) + "y = " + str(self.c)
		return text

	def genFormelTxtY(self):
		text=""
		if 0 == self.b:
			text = "Nicht definiert wegen b=0\n"
			if 0 != self.a:
				text = "Beste Antwort: x = " + str(self.c/float(self.a))
		else:
			text = "y = " + str(0 - (self.a / float(self.b))) + "x "
			if self.c < 0:
				text = text + " - " + str(abs(self.c)) 
			else:
				text = text + " + " + str(self.c) 
		return text	


with open("tasks_" + prefix + ".txt","w") as tasks:
	with open("solutions_" + prefix + ".txt","w") as solutions:
		tasks.write("Folgende Funktionen definieren jeweils eine Gerade. Bestimme jeweils\n\t- den y-Achsen Abschnitt,\n\t- den x-Achsen Abschnitt und\n\t- stelle die Gleichung um in die Form y=mx+b\n")
		tasks.write("Ergaenze die fehlende Koordinate in den Punkten, wenn moeglich (wenn nicht, begruende, warum es nicht moeglich ist.)\n")
		for t in ['a','b','c','d','e','f']:
			l = LineFct()
			tasks.write( "" + t + ")\n")
			tasks.write("Funktion: " + l.genFormelTxt() + "\n")
			solutions.write( t + ")\n")
			solutions.write( l.genFormelTxtY() + "\n")
			for j in range(1,5):
				(task,solution) = l.genGetYForXTxt()
				tasks.write(t + str(j) + ") " + task + "\n")
				solutions.write(t + str(j) + ") " + solution + "\n")
