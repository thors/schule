# -*- coding: utf-8 -*-
import random,math,time,os,sys

prefix=time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime())

def get_repo_root():
	rel_script=sys.argv[0]
	if rel_script[0]=='/':
		repo_root = os.path.dirname(sys.argv[0])
	else:
		repo_root = os.path.dirname(os.path.join(os.getcwd(),sys.argv[0]))
	repo_root = repo_root[:repo_root.rfind("/")]
	return repo_root

	
repo_root=get_repo_root()
output_folder = os.path.join(repo_root,"aufgaben","physik")
template_folder = os.path.join(repo_root,"aufgaben","physik")

class Laws:
	laws = {
		'units': "$[U]=V$ (Volt), $[R]=\\Omega$ (Ohm), $[I]=A$ (Ampere), $[P]=W$ (Watt), $[Q]=J (Joule)$",
		'uri': "Ohmsches Gesetz: $U=R\cdot I$",
		'p_el' : "Elektrische Leistung $P=U\cdot I$",
		'p' : "Leistung is Arbeit pro Zeit $P=Q/t [J/s]$",
		'c' : "Wärmekapazität $c=\\frac{\Delta Q}{m\cdot \Delta T}$, Einheit $[c]=\\frac{J}{g\cdot K}$"
	}
	def __init__(self):
		self.required = ['units','uri','p_el','p','c']
	
	def allToTex(self):
		text = ""
		for k in self.required:
			text=text+self.laws[k] + "\\\\"
		return text

l = Laws()

class TaskHeizplatte:
	def __init__(self):
		self.u = 10 * random.randint(5,10)		# Spannung der Spannungsquelle
		self.i = random.randint(4,10) 				# Strom
		self.p = self.u * self.i # Leistung der Heizplatte
		self.r = self.u / float(self.i)		 # Widerstand der Heizplatte, k
		self.m = 1000 * random.randint(1,4) / 2 # Menge Wasser in Gramm 
		self.c = random.randint(1,4)			#Waermekapazitaet Joule pro Gramm Kelvin
		self.dT = random.randint(10,20)		 #Temperaturanstieg
		self.dt = (self.dT * self.m * self.c) / self.p # Dauer des Experimentes
		self.known = []
		self.known.append(['strom','spannung'][random.randint(0,1)])
		tmp = ['capacity','warming','duration']
		del tmp[random.randint(0,1)]
		self.known += tmp
		self.known.append(['leistung','widerstand'][random.randint(0,1)])
		self.solutions = ["$P=%dW$" % (self.p),
					 "$U=%dV$" %(self.u),
					 "$I=%dA$" % (self.i),
					 "$R=%.2fA$" % (self.r),
					 "$\Delta t=%ds$" % (self.dt),
					 "$\Delta T=%dK$" % (self.dT),
					 "$c=%d\\frac{J}{g\cdot K}$" % (self.c)
					 ]
	def genTex(self):
		tasks = []
		solutions = []
		solution = ""
		description = "Auf einer Heizplatte steht ein Topf mit %dml Fl\\\"ussigkeit.\n"% (self.m)
		if 'capacity' in self.known:
			description = description + "Die Fl\\\"ussigkeit hat eine W\\\"armekapazit\\\"at von $c=%d\\frac{J}{g\cdot K}$ .\n" % (self.c)

		if 'warming' in self.known:
			description = description + "Die Fl\\\"ussigkeit erwärmt sich um $\Delta T=%dK$.\n" % (self.dT)

		if 'duration' in self.known:
			description = description + "Die Flüssigkeit wird für einen Zeitraum von $t=%ds$ erhitzt.\n" % (self.dt)

		if 'leistung' in self.known:
			description = description + "Die Heizplatte hat eine Leistung $P$ von $%dW$.\n" % (self.p)
		else:
			description = description + "Die Heizplatte hat einen Widerstand $R$ von $%.1f\\Omega$.\n" % (self.r)
			
		if 'strom' in self.known:
			description = description + "Durch die Heizplatte fließt ein Strom von $%dA$." % (self.i)
		else:
			description = description + "An der Heizplatte liegt eine Spannung von $%dV$ an." % (self.u)

		description = description + "\\\\Der Topf und die Heizplatte sind als ideal anzunehmen. Das heißt, es geht keine Wärme verloren, alle Wärme wird in die Flüssigkeit übertragen."

		if 'spannung' in self.known:
			if 'leistung' in self.known:
				tasks.append("Berechne den Strom $I$, der durch die Heizplatte fließt")
				tasks.append("Berechne den Widerstand $R$ der Heizplatte")
			else:
				#Widerstand bekannt
				tasks.append("Berechne die Leistung $P$ der Heizplatte")
				tasks.append("Berechne den Strom $I$, der durch die Heizplatte fließt")
		else:
			#Strom bekannt 
			tasks.append("Berechne die Spannung $U$, die über die Heizplatte abfällt")
			if 'leistung' in self.known:
				tasks.append("Berechne den Widerstand $R$ der Heizplatte")
			else:
				#Widerstand bekannt
				tasks.append("Berechne die Leistung $P$ der Heizplatte")
				
		if not 'capacity' in self.known:
			tasks.append("Berechne die Wärmekapazität c der Flüssigkeit")

		if not 'warming' in self.known:
			tasks.append("Berechne, um wie viel Grad die Flüssigkeit sich erwärmt ($\Delta T$)")

		if not 'duration' in self.known:
			tasks.append("Berechne, wie lang die Heizplatte aktiv ist ($\Delta t$)")

		return (description,tasks,self.solutions)
			
class WiderstandsNetzwerk:
	def __init__(self):
		self.R = []
		


tasks_file = "tasks_" + prefix + ".tex"
solutions_file = "solutions_" + prefix + ".tex"
with open("content.tex","w") as content:
	content.write("\\input{%s}\n\\vfill\n\\pagebreak\n\\input{%s}\n" % (tasks_file, solutions_file))
	
with open("laws.tex","w") as lawsf:
	lawsf.write(l.allToTex())
	
with open(tasks_file,"w") as tasksf:
	with open(solutions_file,"w") as solutionsf:
		tasksf.write("\\section{Heizplatte}")
		solutionsf.write("\\section{Heizplatte}")
		t = TaskHeizplatte()		
		(description, tasks, solutions) =  t.genTex()
		tasksf.write(description.replace("\n","\\\\\n"))
		tasksf.write("\\\\\\\\")
		i = 1
		for task in tasks:
			tasksf.write("\subsection{%s}\n\\vfill\n" % (task))
		for solution in solutions:
			solutionsf.write(solution + "\\\\")

pdffilename = "physik_elektrezitaet_" + prefix + ".pdf"
os.system("latex ../template/mathe_template.tex; dvipdf mathe_template.dvi %s " % (pdffilename))
