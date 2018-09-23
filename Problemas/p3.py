from pyevolve import G1DList #Se importa el objeto genoma tipo lista (general)
from pyevolve import GSimpleGA
from pyevolve import Initializators
from pyevolve import Selectors
from pyevolve import Mutators
from pyevolve import Crossovers
from pyevolve import GAllele #Se importan las funciones para usar alelos
from pyevolve import Statistics
import pyevolve

#Debe implementar una distancia entre letras, existen varias formas de hacer esto, pero puede serle util crear una lista
#o string con todo el abecedario y luego recuperar la posicion de cada letra en particular usando la funcion find().
#Recuerde que debe ser considerado 'ciclico', como fue dicho en el enunciado, lo que no quiere decir que debe ser una
#lista circular, solo la distancia debe serlo.
#Funcion de evaluacion
def eval_func(chromosome):
	score = 0.0



	return score


#El ocupar las utilidades para alelos en el algoritmo permite que cada gen solo pueda tomar un alfabeto personalizado,
#pueden usarse numeros especificos, letras, listas, tuplas, diccionarios, objetos personalizados, otros, y combinaciones 
#de todos los anteriores; el limite lo pone quien programa.
#Un ejemplo de definicion de uso de alelos en pyevolve, podria ser:

#setOfAlleles = GAllele.GAlleles()  #En este caso se usaran 20 genes
#for x in xrange(20):      #Iteracion para agregar el alfabeto a cada gen 
#	a = GAllele.GAlleleList(['a', 24.2685, [1,2,3,4], Objeto()])       #Se define el alfabeto (puede ser cambiante)
#	setOfAlleles.add(a)    #Se agrega al set de alelos, para el gen en cuestion
#   
#genome = G1DList.G1DList(20)   #se crea el tipo de genoma, en este caso de 20 genes
#genome.setParams(allele=setOfAlleles)    #se usa el set de alelos para este genoma


# Se definen los alelos (alfabeto) a utilizar, y se asigna a cada gen (se puede asignar alfabetos distintos para cada gen)
setOfAlleles = GAllele.GAlleles()
for x in xrange(): 
	a = GAllele.GAlleleList() #Defina el alfabeto
	setOfAlleles.add(a)
   
genome = G1DList.G1DList()

# Se agrega la lista de alelos como parametro del genoma
genome.setParams(allele=setOfAlleles) 

# Defina que funcion evaluadora, initializator, mutator y crossover utilizara. Busque los ultimos 3 en el Anexo
genome.evaluator.set()
genome.initializator.set()
genome.mutator.set()
genome.crossover.set()

ga = GSimpleGA.GSimpleGA(genome)

# Defina el tipo de seleccion del algoritmo. Busquelo en el anexo
ga.selector.set()

# Numero de generaciones
ga.setGenerations(500)

ga.evolve()

print 